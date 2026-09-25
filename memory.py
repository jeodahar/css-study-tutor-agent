"""
memory.py
Persistent storage for the student's assessment history, using Supabase
(a free hosted Postgres database) so results survive closing the app or
redeploying it - Streamlit Cloud's own disk is NOT persistent.

Table needed (see supabase_schema.sql):
    assessments(id, student_id, subject, question, answer_text, assessment, created_at)
"""

import datetime

from config import SUPABASE_URL, SUPABASE_KEY

_client = None
_client_error = None


def get_client():
    """Lazily create and cache the Supabase client. Returns None if not configured."""
    global _client, _client_error
    if _client is not None:
        return _client
    if not SUPABASE_URL or not SUPABASE_KEY:
        _client_error = "Supabase is not configured (missing SUPABASE_URL / SUPABASE_KEY)."
        return None
    try:
        from supabase import create_client
        _client = create_client(SUPABASE_URL, SUPABASE_KEY)
        return _client
    except Exception as e:
        _client_error = str(e)
        return None


def is_connected():
    return get_client() is not None


def connection_error():
    return _client_error


def save_assessment(student_id, subject, question, answer_text, assessment_result, topic=None):
    """Save one assessment record. Returns True on success, False otherwise."""
    client = get_client()
    if client is None:
        return False
    data = {
        "student_id": student_id,
        "subject": subject,
        "topic": topic,
        "question": question,
        "answer_text": answer_text,
        "assessment": assessment_result,
        "created_at": datetime.datetime.utcnow().isoformat(),
    }
    try:
        client.table("assessments").insert(data).execute()
        return True
    except Exception as e:
        global _client_error
        _client_error = str(e)
        return False


def get_history(student_id, subject=None, limit=20):
    """Return the student's past assessments, most recent first."""
    client = get_client()
    if client is None:
        return []
    try:
        query = (
            client.table("assessments")
            .select("*")
            .eq("student_id", student_id)
            .order("created_at", desc=True)
            .limit(limit)
        )
        if subject:
            query = query.eq("subject", subject)
        res = query.execute()
        return res.data or []
    except Exception as e:
        global _client_error
        _client_error = str(e)
        return []


def get_covered_topics(student_id, subject):
    """Set of topic names the student has already practiced for this subject."""
    history = get_history(student_id, subject, limit=200)
    return {item.get("topic") for item in history if item.get("topic")}


def get_all_history(student_id, limit=200):
    """All of a student's assessments across every subject (for the dashboard overview)."""
    return get_history(student_id, subject=None, limit=limit)


def get_weak_topics(student_id, subject=None):
    """Count how often each 'area to improve' shows up, most frequent first."""
    history = get_history(student_id, subject, limit=50)
    weakness_count = {}
    for item in history:
        assessment = item.get("assessment") or {}
        if isinstance(assessment, dict):
            weaknesses = assessment.get("areas_to_improve", [])
            for w in weaknesses:
                weakness_count[w] = weakness_count.get(w, 0) + 1
    return sorted(weakness_count.items(), key=lambda x: -x[1])
