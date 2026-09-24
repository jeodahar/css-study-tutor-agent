"""
agent.py
The CrewAI Study Tutor Agent. One agent, used for several tasks
(study explanations, question analysis, study plans) via different prompts.
Handwritten assessment (assessment.py) and OCR (ocr.py) call Groq directly
for speed and reliable JSON output, and don't need the full crew.
"""

import os

from crewai import Agent, Task, Crew

from config import GROQ_API_KEY, GROQ_MODEL
from prompts import STUDY_PROMPT, QUESTION_ANALYSIS_PROMPT, STUDY_PLAN_PROMPT
from tools import web_search, format_search_results

os.environ.setdefault("GROQ_API_KEY", GROQ_API_KEY or "")


def _llm():
    # crewai (via litellm) expects "groq/<model-name>"
    return f"groq/{GROQ_MODEL}"


def build_tutor_agent() -> Agent:
    return Agent(
        role="CSS Exam Study Tutor",
        goal="Help the student master CSS syllabus topics and write better exam answers",
        backstory=(
            "A seasoned CSS (Central Superior Services) coach who has helped many "
            "candidates pass. Explains concepts clearly, focuses on what examiners "
            "actually reward, and gives concrete, actionable advice."
        ),
        llm=_llm(),
        verbose=False,
    )


def _run_single_task(description: str, expected_output: str) -> str:
    agent = build_tutor_agent()
    task = Task(description=description, expected_output=expected_output, agent=agent)
    crew = Crew(agents=[agent], tasks=[task], verbose=False)
    result = crew.kickoff()
    return str(result)


def study_topic(subject: str, topic: str) -> str:
    prompt = STUDY_PROMPT.format(subject=subject, topic=topic)
    return _run_single_task(prompt, "A clear, exam-focused explanation of the topic.")


def analyze_question(subject: str, question: str) -> str:
    prompt = QUESTION_ANALYSIS_PROMPT.format(subject=subject, question=question)
    return _run_single_task(prompt, "A breakdown of the question with a suggested outline.")


def make_study_plan(subject: str, days: int, weak_areas) -> str:
    weak_str = ", ".join(weak_areas) if weak_areas else "None recorded yet"
    prompt = STUDY_PLAN_PROMPT.format(subject=subject, days=days, weak_areas=weak_str)
    return _run_single_task(prompt, "A day-by-day study plan.")


def current_affairs_briefing(query: str) -> str:
    """Combines a live web search with the tutor agent's summary - useful for
    the Current Affairs subject where the syllabus itself is 'today's news'."""
    results = web_search(query, max_results=5)
    context = format_search_results(results)
    description = (
        f"Using the search results below, write a CSS-exam-style current affairs "
        f"briefing on: {query}\n\nSearch results:\n{context}\n\n"
        f"Structure it as: Background, Key Developments, Pakistan's Angle/Relevance, "
        f"Possible Exam Angle."
    )
    return _run_single_task(description, "A structured current affairs briefing.")
