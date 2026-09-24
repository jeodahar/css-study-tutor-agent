"""
curriculum.py
CSS subjects and their key syllabus topics.
This is a starting list you can expand over time.
"""

SUBJECTS = {
    "Essay": [
        "Outline writing", "Thesis statement", "Argument development",
        "Current global issues", "Philosophical essays",
    ],
    "Precis & Composition": [
        "Precis writing", "Comprehension", "Grammar", "Sentence correction",
        "Vocabulary",
    ],
    "General Science & Ability": [
        "Basic science concepts", "Logical reasoning", "Analytical ability",
        "Mental ability",
    ],
    "Pakistan Affairs": [
        "Ideology of Pakistan", "Constitutional history", "1973 Constitution",
        "Federalism", "Foreign policy", "Economic challenges",
    ],
    "Current Affairs": [
        "Regional politics", "International relations", "Economy",
        "Security issues", "Recent developments",
    ],
    "Islamic Studies": [
        "Sources of Islamic law", "History of Islam", "Islamic Political System",
        "Contemporary issues in Islam",
    ],
    "Political Science I": [
        "Political theory", "Concepts: State, sovereignty, liberty",
        "Classical political thinkers",
    ],
    "Political Science II": [
        "Government systems", "Political development", "International politics",
    ],
    "Gender Studies": [
        "Gender and development", "Gender and law", "Feminist theory",
    ],
    "Criminology": [
        "Theories of crime", "Criminal justice system", "Juvenile delinquency",
    ],
    "History of Indo-Pak": [
        "Pre-partition history", "Freedom movement", "Partition of India",
    ],
    "Sindhi": [
        "Grammar", "Composition", "Literature",
    ],
}


def get_subjects():
    return list(SUBJECTS.keys())


def get_topics(subject):
    return SUBJECTS.get(subject, [])
