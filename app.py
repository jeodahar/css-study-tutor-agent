"""
app.py
CSS Study Tutor Agent - Streamlit front end.

Modes: Study, Question Analysis, Answer Practice (typed), AI Practice Question
(agent sets the question), Handwritten Answer (OCR + assessment),
Study Plan, Dashboard.

Assessment reports are saved to Supabase (see memory.py) so a student's
history, topic coverage, and weak-topic tracking survive closing the app
or a redeploy.
"""

import streamlit as st

import agent
import assessment
import memory
import ocr
import past_papers
from curriculum import get_subjects, get_topics, get_subtopics, get_compulsory_subjects

st.set_page_config(page_title="CSS Study Tutor Agent", page_icon="🎓", layout="centered")

# --- Student identity (simple, no login system for MVP) -------------------
if "student_id" not in st.session_state:
    st.session_state.student_id = ""

with st.sidebar:
    st.title("🎓 CSS Study Tutor")
    st.session_state.student_id = st.text_input(
        "Your name / student ID",
        value=st.session_state.student_id,
        help="Used to save and load your assessment history.",
    )
    if not memory.is_connected():
        st.warning("Progress won't be saved - Supabase connection issue.")
        with st.expander("Show details"):
            st.write("SUPABASE_URL set:", bool(memory.SUPABASE_URL))
            st.write("SUPABASE_KEY set:", bool(memory.SUPABASE_KEY))
            st.write("Error:", memory.connection_error())

    mode = st.radio(
        "Mode",
        [
            "📖 Study",
            "🔍 Question Analysis",
            "✍️ Answer Practice",
            "🎯 AI Practice Question",
            "📷 Handwritten Answer",
            "📅 Study Plan",
            "📊 Dashboard",
        ],
    )

if mode != "📊 Dashboard":
    subject = st.selectbox("Subject", get_subjects())


def render_assessment(result: dict):
    """Shared display for an assessment result dict."""
    st.subheader("📊 Assessment")
    ratings = result.get("ratings", {})
    for k, v in ratings.items():
        st.write(f"**{k.title()}**: {v}")
    if result.get("strengths"):
        st.markdown("**✅ Strengths**")
        for s in result["strengths"]:
            st.write(f"- {s}")
    if result.get("areas_to_improve"):
        st.markdown("**⚠️ Areas to improve**")
        for w in result["areas_to_improve"]:
            st.write(f"- {w}")
    if result.get("next_practice"):
        st.markdown(f"**🎯 Next practice:** {result['next_practice']}")
    if result.get("raw_response"):
        st.caption("Raw model response (couldn't parse as structured JSON):")
        st.text(result["raw_response"])
    st.caption("This is an AI practice assessment, not an official CSS examiner score.")


def save_button(key: str):
    """Shared 'save this assessment' button, using whatever is in st.session_state['last_assessment']."""
    if not st.session_state.student_id:
        st.info("Enter your name / student ID in the sidebar to save this.")
        return
    if st.button("💾 Save this assessment", key=key):
        a = st.session_state["last_assessment"]
        ok = memory.save_assessment(
            st.session_state.student_id, a["subject"], a["question"],
            a["answer"], a["result"], topic=a.get("topic"),
        )
        if ok:
            st.success("Saved to your history.")
        else:
            st.error(memory.connection_error() or "Could not save - check Supabase setup.")


# ---------------------------------------------------------------------------
if mode == "📖 Study":
    st.header("📖 Study")
    topic = st.selectbox("Topic", get_topics(subject))
    subtopics = get_subtopics(subject, topic)
    subtopic = None
    if subtopics:
        subtopic_choice = st.selectbox("Sub-topic (optional)", ["Overview (all sub-topics)"] + subtopics)
        subtopic = None if subtopic_choice == "Overview (all sub-topics)" else subtopic_choice
    if st.button("Explain this topic"):
        with st.spinner("Thinking..."):
            result = agent.study_topic(subject, topic, subtopic)
        st.markdown(result)

# ---------------------------------------------------------------------------
elif mode == "🔍 Question Analysis":
    st.header("🔍 Question Analysis")
    question = st.text_area("Paste the exam question")
    if st.button("Analyze question") and question.strip():
        with st.spinner("Analyzing..."):
            result = agent.analyze_question(subject, question)
        st.markdown(result)

# ---------------------------------------------------------------------------
elif mode == "✍️ Answer Practice":
    st.header("✍️ Answer Practice")
    topic = st.selectbox("Topic (optional, for tracking)", ["General"] + get_topics(subject))
    question = st.text_area("Question")
    answer = st.text_area("Your answer", height=250)
    if st.button("Assess my answer") and question.strip() and answer.strip():
        with st.spinner("Assessing..."):
            result = assessment.assess_answer(subject, question, answer)
        st.session_state["last_assessment"] = {
            "subject": subject, "question": question, "answer": answer,
            "result": result, "topic": None if topic == "General" else topic,
        }

    if "last_assessment" in st.session_state:
        render_assessment(st.session_state["last_assessment"]["result"])
        save_button("save_typed")

# ---------------------------------------------------------------------------
elif mode == "🎯 AI Practice Question":
    st.header("🎯 AI Practice Question")
    st.caption("Practice with a real past-paper question, or let the tutor set a new one, to systematically cover every syllabus topic.")
    topics = get_topics(subject)
    covered = memory.get_covered_topics(st.session_state.student_id, subject) if st.session_state.student_id else set()
    topic = st.selectbox("Topic", topics, format_func=lambda t: f"✅ {t}" if t in covered else f"◻️ {t}")
    subtopics = get_subtopics(subject, topic)
    subtopic = None
    if subtopics:
        subtopic_choice = st.selectbox("Sub-topic (optional)", ["Any sub-topic"] + subtopics, key="ai_subtopic")
        subtopic = None if subtopic_choice == "Any sub-topic" else subtopic_choice

    source = st.radio(
        "Question source",
        ["📜 Real past paper (if available)", "🎲 New AI-generated question"],
        horizontal=True,
    )

    if st.button("Get a question"):
        if source.startswith("📜"):
            pp = past_papers.get_random_question(subject, topic)
            if pp:
                st.session_state["ai_question"] = {
                    "subject": subject, "topic": topic,
                    "question": pp["question"],
                    "source": f"FPSC {pp['year']} past paper",
                }
            else:
                st.info(f"No past-paper questions saved yet for {subject} - generating one instead.")
                with st.spinner("Setting a question..."):
                    q = agent.generate_question(subject, topic, subtopic)
                st.session_state["ai_question"] = {
                    "subject": subject, "topic": topic, "question": q, "source": "AI-generated",
                }
        else:
            with st.spinner("Setting a question..."):
                q = agent.generate_question(subject, topic, subtopic)
            st.session_state["ai_question"] = {
                "subject": subject, "topic": topic, "question": q, "source": "AI-generated",
            }

    if "ai_question" in st.session_state:
        aq = st.session_state["ai_question"]
        st.caption(f"Source: {aq.get('source', 'AI-generated')}")
        st.markdown(f"**Question:** {aq['question']}")
        answer = st.text_area("Your answer", height=250, key="ai_q_answer")
        if st.button("Assess my answer", key="assess_ai_q") and answer.strip():
            with st.spinner("Assessing..."):
                result = assessment.assess_answer(aq["subject"], aq["question"], answer)
            st.session_state["last_assessment"] = {
                "subject": aq["subject"], "question": aq["question"], "answer": answer,
                "result": result, "topic": aq["topic"],
            }

    if "last_assessment" in st.session_state:
        render_assessment(st.session_state["last_assessment"]["result"])
        save_button("save_ai_question")

# ---------------------------------------------------------------------------
elif mode == "📷 Handwritten Answer":
    st.header("📷 Handwritten Answer")
    topic = st.selectbox("Topic (optional, for tracking)", ["General"] + get_topics(subject))
    question = st.text_area("Question")
    uploaded = st.file_uploader("Upload a photo of your handwritten answer", type=["jpg", "jpeg", "png"])

    if uploaded is not None:
        st.image(uploaded, caption="Uploaded answer", use_container_width=True)
        if st.button("Extract text (OCR)"):
            with st.spinner("Reading your handwriting..."):
                extracted = ocr.extract_text_from_image(uploaded.getvalue())
            st.session_state["extracted_text"] = extracted

    if "extracted_text" in st.session_state:
        st.subheader("🔍 Extracted Answer (edit if needed)")
        edited = st.text_area("Extracted text", value=st.session_state["extracted_text"], height=250)
        if st.button("Analyze my answer") and question.strip() and edited.strip():
            with st.spinner("Assessing..."):
                result = assessment.assess_answer(subject, question, edited)
            st.session_state["last_assessment"] = {
                "subject": subject, "question": question, "answer": edited,
                "result": result, "topic": None if topic == "General" else topic,
            }

    if "last_assessment" in st.session_state:
        render_assessment(st.session_state["last_assessment"]["result"])
        save_button("save_handwritten")

# ---------------------------------------------------------------------------
elif mode == "📅 Study Plan":
    st.header("📅 Study Plan")
    days = st.slider("Plan length (days)", 3, 30, 7)
    weak_areas = []
    if st.session_state.student_id:
        weak_areas = [w for w, _ in memory.get_weak_topics(st.session_state.student_id, subject)]
    if st.button("Generate study plan"):
        with st.spinner("Building your plan..."):
            result = agent.make_study_plan(subject, days, weak_areas)
        st.markdown(result)

# ---------------------------------------------------------------------------
elif mode == "📊 Dashboard":
    st.header("📊 Dashboard")
    if not st.session_state.student_id:
        st.info("Enter your name / student ID in the sidebar to see your dashboard.")
    else:
        all_history = memory.get_all_history(st.session_state.student_id)
        subjects_touched = {h.get("subject") for h in all_history if h.get("subject")}

        col1, col2 = st.columns(2)
        col1.metric("Total answers assessed", len(all_history))
        col2.metric("Subjects started", f"{len(subjects_touched)}/{len(get_subjects())}")

        st.subheader("📚 Coverage by subject")
        for subj in get_compulsory_subjects():
            topics = get_topics(subj)
            covered = memory.get_covered_topics(st.session_state.student_id, subj)
            covered_count = len([t for t in topics if t in covered])
            st.write(f"**{subj}** - {covered_count}/{len(topics)} topics practiced")
            st.progress(covered_count / len(topics) if topics else 0)

        st.subheader("⚠️ Repeated weak areas (all subjects)")
        weak_by_subject = {}
        for subj in subjects_touched:
            weak = memory.get_weak_topics(st.session_state.student_id, subj)
            if weak:
                weak_by_subject[subj] = weak
        if weak_by_subject:
            for subj, weak in weak_by_subject.items():
                st.write(f"**{subj}**")
                for w, count in weak[:5]:
                    st.write(f"- {w} (seen {count}x)")
        else:
            st.info("No weak areas tracked yet - complete some assessments first.")

        st.subheader("🗂️ Recent history")
        for item in all_history[:30]:
            label = f"{item.get('created_at', '')[:16]} · {item.get('subject', '')} - {item.get('question', '')[:50]}"
            with st.expander(label):
                if item.get("topic"):
                    st.write("**Topic:**", item.get("topic"))
                st.write("**Question:**", item.get("question"))
                st.write("**Your answer:**", item.get("answer_text"))
                st.write("**Assessment:**", item.get("assessment"))
