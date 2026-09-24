"""
assessment.py
Turns a (question, answer) pair into a structured AI assessment,
using Groq directly for a fast, reliable JSON response.
"""

import json

from groq import Groq

from config import GROQ_API_KEY, GROQ_MODEL
from prompts import ASSESSMENT_PROMPT


def assess_answer(subject: str, question: str, answer: str) -> dict:
    client = Groq(api_key=GROQ_API_KEY)
    prompt = ASSESSMENT_PROMPT.format(subject=subject, question=question, answer=answer)

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=1200,
    )
    raw = response.choices[0].message.content.strip()
    raw = raw.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # Fall back gracefully so the UI never crashes on a malformed response
        return {
            "ratings": {},
            "strengths": [],
            "areas_to_improve": [],
            "next_practice": "",
            "raw_response": raw,
        }
