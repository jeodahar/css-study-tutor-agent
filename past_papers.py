"""
past_papers.py
A small, growing bank of real FPSC CSS past-paper questions, so students can
practice on genuine exam questions instead of only AI-generated ones.

Verified sources: FPSC past-paper archives and past-paper analysis sites
(cssprep.com.pk, cssprepforum.com). Wording is reconstructed from published
summaries where the original paper wasn't directly accessible, so treat the
exact phrasing as close-but-not-guaranteed-verbatim to the official paper -
the year, topic and substance are accurate. Add more entries here over time
as you collect verified papers (e.g. from FPSC's own past-papers archive).

Structure: PAST_PAPERS[subject] = [ {year, topic, question}, ... ]
"""

PAST_PAPERS = {
    "Pakistan Affairs": [
        {
            "year": 2023,
            "topic": "Political Evolution Since 1971",
            "question": (
                "There is an opinion that some subjects handed over to the "
                "provinces under the 18th Amendment should be reviewed. "
                "Discuss the 18th Amendment and the question of provincial "
                "autonomy in this context."
            ),
        },
        {
            "year": 2023,
            "topic": "Ideology of Pakistan",
            "question": (
                "Discuss the evolution and development of the separate "
                "electorate system in British India. Can it be considered a "
                "foundation for the Two-Nation Theory?"
            ),
        },
        {
            "year": 2023,
            "topic": "Economic Challenges",
            "question": (
                "Give a resume of the mineral resources of Pakistan and "
                "comment on why these resources remain under-exploited."
            ),
        },
        {
            "year": 2023,
            "topic": "Hydro Politics / Water Issues",
            "question": (
                "What policy options should Pakistan exercise to effectively "
                "address its vulnerability to global warming?"
            ),
        },
        {
            "year": 2024,
            "topic": "Hydro Politics / Water Issues",
            "question": (
                "Discuss the impact of global warming on Pakistan and the "
                "policy measures needed to address it."
            ),
        },
    ],
    "Current Affairs": [
        {
            "year": 2021,
            "topic": "Recent national developments",
            "question": (
                "Should new provinces be created in Pakistan? Discuss in "
                "light of political parties' commitments on this issue."
            ),
        },
        {
            "year": 2022,
            "topic": "International relations & global powers",
            "question": (
                "Write a short note on the 2022 FIFA World Cup and the "
                "politics of the Arab world."
            ),
        },
        {
            "year": 2023,
            "topic": "International relations & global powers",
            "question": (
                "Write a note on the expansion of BRICS and its attempts "
                "towards de-dollarization."
            ),
        },
    ],
}


def get_random_question(subject, topic=None):
    """Return one past-paper question dict for the subject (optionally
    filtered to a topic), or None if none are available yet."""
    import random

    pool = PAST_PAPERS.get(subject, [])
    if topic:
        filtered = [q for q in pool if q["topic"] == topic]
        pool = filtered or pool  # fall back to any question for the subject
    if not pool:
        return None
    return random.choice(pool)


def has_any_questions(subject):
    return bool(PAST_PAPERS.get(subject))
