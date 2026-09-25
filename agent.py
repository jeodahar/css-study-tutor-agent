"""
agent.py
The Study Tutor "agent" - a set of functions that call Groq directly for
study explanations, question analysis, study plans, and current affairs
briefings. (An earlier version used CrewAI for orchestration, but CrewAI
pulls in chromadb, which currently breaks on Streamlit Cloud's Python
version - Groq handles single-task calls like these fine on its own.)
"""

from groq import Groq

from config import GROQ_API_KEY, GROQ_MODEL
from prompts import (
    STUDY_PROMPT,
    QUESTION_ANALYSIS_PROMPT,
    STUDY_PLAN_PROMPT,
    QUESTION_GENERATION_PROMPT,
)
from tools import web_search, format_search_results


def _ask(prompt: str, temperature: float = 0.4, max_tokens: int = 1500) -> str:
    client = Groq(api_key=GROQ_API_KEY)
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a seasoned CSS (Central Superior Services, Pakistan) exam "
                    "coach who has helped many candidates pass. Explain concepts clearly, "
                    "focus on what examiners actually reward, and give concrete, actionable "
                    "advice."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content.strip()


def study_topic(subject: str, topic: str) -> str:
    prompt = STUDY_PROMPT.format(subject=subject, topic=topic)
    return _ask(prompt)


def analyze_question(subject: str, question: str) -> str:
    prompt = QUESTION_ANALYSIS_PROMPT.format(subject=subject, question=question)
    return _ask(prompt)


def make_study_plan(subject: str, days: int, weak_areas) -> str:
    weak_str = ", ".join(weak_areas) if weak_areas else "None recorded yet"
    prompt = STUDY_PLAN_PROMPT.format(subject=subject, days=days, weak_areas=weak_str)
    return _ask(prompt)


def generate_question(subject: str, topic: str) -> str:
    prompt = QUESTION_GENERATION_PROMPT.format(subject=subject, topic=topic)
    return _ask(prompt, temperature=0.7, max_tokens=200)


def current_affairs_briefing(query: str) -> str:
    """Combines a live web search with the tutor's summary - useful for the
    Current Affairs subject where the syllabus itself is 'today's news'."""
    results = web_search(query, max_results=5)
    context = format_search_results(results)
    prompt = (
        f"Using the search results below, write a CSS-exam-style current affairs "
        f"briefing on: {query}\n\nSearch results:\n{context}\n\n"
        f"Structure it as: Background, Key Developments, Pakistan's Angle/Relevance, "
        f"Possible Exam Angle."
    )
    return _ask(prompt)
