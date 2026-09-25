"""
curriculum.py
CSS subjects and syllabus topics, aligned with the official FPSC
"Revised Syllabi for CSS Competitive Examination, CE-2016 and onwards"
(the 6 compulsory subjects are given in full official detail;
optional subjects use their standard FPSC topic headings).
"""

SUBJECTS = {
    # --- Compulsory (600 marks total, 100 each) ---
    "English Essay": [
        "Outline writing", "Thesis statement development", "Argument development & structure",
        "Contemporary social/political/philosophical themes", "Style, coherence & vocabulary",
    ],
    "Precis & Composition": [
        "Precis writing", "Comprehension passages", "Grammar & sentence correction",
        "Vocabulary (synonyms/antonyms/idioms)", "Translation & composition",
    ],
    "General Science & Ability": [
        "Basic Physics, Chemistry & Biology concepts", "Everyday science",
        "Logical & analytical reasoning", "Quantitative ability", "Data interpretation",
    ],
    "Current Affairs": [
        "Pakistan's foreign policy", "Regional politics (South Asia, Afghanistan, Middle East)",
        "International relations & global powers", "National & global economy",
        "Security & defense issues", "Regional organizations (SAARC, SCO, CPEC, ECO)",
        "Recent national developments",
    ],
    "Pakistan Affairs": [
        "Ideology of Pakistan", "Land and people of Pakistan (geography, society, resources)",
        "Pakistan and changing regional apparatus", "Nuclear program of Pakistan",
        "Regional cooperation organizations (SAARC, ECO, SCO)", "Civil-military relations",
        "Economic challenges", "Non-traditional security threats", "Pakistan's role in the region",
        "The Palestine issue", "Changing security dynamics / national security challenges",
        "Political evolution since 1971", "Pakistan and the US war on terror",
        "Foreign policy of Pakistan post 9/11", "Evolution of the democratic system",
        "Ethnic issues and national integration", "Hydro politics / water issues",
        "Pakistan's national interest", "Challenges to sovereignty",
        "Energy problems and their effects", "Relations with neighbors (excluding India)",
        "Pakistan-India relations since 1947", "The Kashmir issue",
        "The war in Afghanistan since 1979 and its impact on Pakistan", "Proxy wars",
        "Economic conditions, recent budget & economic survey",
        "Recent constitutional and legal debates / amendments",
        "Social problems: poverty, education, health & sanitation",
    ],
    "Islamic Studies": [
        "Introduction to Islam", "Sources of Islamic legislation (Quran, Sunnah, Ijma, Qiyas)",
        "Seerah of the Prophet Muhammad (PBUH)", "Political system of Islam",
        "Economic system of Islam", "Social system of Islam", "Ethical system of Islam",
        "Islam and contemporary issues",
    ],

    # --- Optional subjects (student's selected group) ---
    "Political Science I": [
        "Political theory", "Concepts: state, sovereignty, liberty, equality",
        "Classical political thinkers (Plato, Aristotle, Machiavelli)",
        "Modern political thinkers (Hobbes, Locke, Rousseau, Montesquieu)",
    ],
    "Political Science II": [
        "Comparative government systems", "Political development & modernization",
        "International politics", "Political institutions",
    ],
    "Gender Studies": [
        "Gender and development", "Gender and law", "Feminist theory",
        "Gender in Pakistani society",
    ],
    "Criminology": [
        "Theories of crime", "Criminal justice system", "Juvenile delinquency",
        "Crime prevention & policy",
    ],
    "History of Indo-Pak": [
        "Muslim rule and heritage in India (712-1857)",
        "Decline of Muslim rule & the rise of British power",
        "Muslim reform and revivalist movements", "Freedom movement & partition of India",
    ],
    "Sindhi": [
        "Grammar", "Composition", "Literature",
    ],
}


def get_subjects():
    return list(SUBJECTS.keys())


def get_topics(subject):
    return SUBJECTS.get(subject, [])


def get_compulsory_subjects():
    return [
        "English Essay", "Precis & Composition", "General Science & Ability",
        "Current Affairs", "Pakistan Affairs", "Islamic Studies",
    ]
