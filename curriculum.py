"""
curriculum.py
CSS subjects, topics AND sub-topics, aligned with the official FPSC
"Revised Syllabi for CSS Competitive Examination, CE-2016 and onwards".
Compulsory subjects use the full official topic/sub-topic breakdown;
optional subjects use their standard FPSC headings (expand over time).

Structure: SUBJECTS[subject] = [ {"topic": str, "subtopics": [str, ...]}, ... ]
"""

SUBJECTS = {
    # --- Compulsory (600 marks total, 100 each) ---
    "Pakistan Affairs": [
        {"topic": "Ideology of Pakistan", "subtopics": [
            "Historical aspects: Muslim rule in the Sub-Continent and its downfall",
            "Reform movements: Shaikh Ahmad Sarhindi, Shah Waliullah, Sayyid Ahmad Shaheed",
            "Aligarh, Deoband, Nadwah and other educational institutions",
            "Ideology in the speeches of Allama Iqbal and Quaid-i-Azam",
        ]},
        {"topic": "Land and People of Pakistan", "subtopics": [
            "Geography", "Society", "Natural resources", "Agriculture", "Industry", "Education",
        ]},
        {"topic": "Pakistan and Changing Regional Apparatus", "subtopics": []},
        {"topic": "Nuclear Program of Pakistan", "subtopics": ["Safety and security", "International concerns"]},
        {"topic": "Regional Cooperation Organizations", "subtopics": ["SAARC", "ECO", "SCO", "Role of Pakistan"]},
        {"topic": "Civil-Military Relations in Pakistan", "subtopics": []},
        {"topic": "Economic Challenges in Pakistan", "subtopics": []},
        {"topic": "Non-Traditional Security Threats", "subtopics": ["Role of non-state actors"]},
        {"topic": "Pakistan's Role in the Region", "subtopics": []},
        {"topic": "The Palestine Issue", "subtopics": []},
        {"topic": "Changing Security Dynamics", "subtopics": ["Challenges to national security"]},
        {"topic": "Political Evolution Since 1971", "subtopics": []},
        {"topic": "Pakistan and the US War on Terror", "subtopics": []},
        {"topic": "Foreign Policy of Pakistan Post 9/11", "subtopics": []},
        {"topic": "Evolution of the Democratic System", "subtopics": []},
        {"topic": "Ethnic Issues and National Integration", "subtopics": []},
        {"topic": "Hydro Politics / Water Issues", "subtopics": ["Domestic context", "Regional context"]},
        {"topic": "Pakistan's National Interest", "subtopics": []},
        {"topic": "Challenges to Sovereignty", "subtopics": []},
        {"topic": "Pakistan's Energy Problems", "subtopics": ["Effects on economy and society"]},
        {"topic": "Relations with Neighbors (excluding India)", "subtopics": []},
        {"topic": "Pakistan-India Relations Since 1947", "subtopics": []},
        {"topic": "The Kashmir Issue", "subtopics": []},
        {"topic": "War in Afghanistan Since 1979", "subtopics": ["Impact on Pakistan", "Post-2014 challenges"]},
        {"topic": "Proxy Wars", "subtopics": ["Role of external elements"]},
        {"topic": "Economic Conditions of Pakistan", "subtopics": ["Recent economic survey", "Budgets", "Major sectors"]},
        {"topic": "Constitutional and Legal Debates", "subtopics": ["Recent amendments", "Important legislation", "Role of higher courts"]},
        {"topic": "Social Problems of Pakistan", "subtopics": ["Poverty", "Education", "Health and sanitation"]},
    ],

    "Islamic Studies": [
        {"topic": "Introduction to Islam", "subtopics": [
            "Concept of Islam", "Importance of Deen in human life",
            "Difference between Deen and religion", "Distinctive aspects of Islam",
            "Impact of Islamic beliefs on individual and social life",
            "Spiritual, moral and social impacts of Islamic worships",
        ]},
        {"topic": "Study of Seerah as a Model", "subtopics": [
            "Individual life", "Diplomacy", "Teacher of mankind",
            "Military strategist/planner", "Prophet of peace",
        ]},
        {"topic": "Human Rights and Status of Women in Islam", "subtopics": [
            "Human dignity: respect and honor of men and women",
        ]},
        {"topic": "Islamic Civilization and Culture", "subtopics": [
            "Meaning and main elements", "Role in character building of society and individual",
            "Distinctive features: monotheism, self-purification, human dignity, equality, "
            "social justice, moral values, tolerance, rule of law",
        ]},
        {"topic": "Islam and the World", "subtopics": [
            "Impact of Islamic civilization on the West and other civilizations",
            "Status of Islam in the modern world", "Challenges of the modern era",
            "Promotion of extremism",
        ]},
        {"topic": "Public Administration and Islamic Governance", "subtopics": [
            "Islamic concept of public administration", "Quranic teachings for good governance",
            "Structure of Islamic governance (Shura, legislature, sources of law)",
            "Governance style of the pious Caliphs", "Responsibilities of civil servants",
            "System of accountability in Islam",
        ]},
        {"topic": "Islamic Code of Life", "subtopics": [
            "Social system", "Political system", "Economic system",
            "Judicial system", "Administrative system", "Principles of Ijma and Ijtihad",
        ]},
    ],

    "Current Affairs": [
        {"topic": "Pakistan's Domestic Affairs", "subtopics": ["Political", "Economic", "Social"]},
        {"topic": "Pakistan's External Affairs", "subtopics": [
            "Relations with neighbors: India, China, Afghanistan, Russia",
            "Relations with the Muslim world: Iran, Saudi Arabia, Indonesia, Turkey",
            "Relations with the United States",
            "Relations with regional/international organizations: UN, SAARC, ECO, OIC, WTO, GCC",
        ]},
        {"topic": "Global Issues", "subtopics": [
            "International security", "International political economy", "Human rights",
            "Environment: global warming, Kyoto Protocol, Copenhagen Accord",
            "Population: world trends and policies", "Terrorism and counter-terrorism",
            "Global energy politics", "Nuclear proliferation and security",
            "Nuclear politics in South Asia", "International trade: Doha Round, Bali Package",
            "Cooperation/competition in the Arabian Sea, Indian & Pacific Oceans",
            "Millennium Development Goals", "Globalization",
            "Middle East crisis", "Kashmir issue", "Palestine issue",
        ]},
    ],

    "General Science & Ability": [
        {"topic": "Physical Sciences", "subtopics": [
            "Universe, galaxy, solar system", "Matter and energy", "Basic physics principles",
            "Basic chemistry principles",
        ]},
        {"topic": "Biological Sciences", "subtopics": [
            "Human body systems", "Diseases and nutrition", "Basic genetics",
        ]},
        {"topic": "Environmental Science", "subtopics": [
            "Ecosystems", "Climate", "Pakistan's environmental challenges",
        ]},
        {"topic": "Food Science", "subtopics": []},
        {"topic": "Quantitative Ability", "subtopics": [
            "Arithmetic", "Ratio & percentage", "Algebra", "Geometry", "Data interpretation",
        ]},
        {"topic": "Logical Reasoning", "subtopics": []},
        {"topic": "Analytical Reasoning", "subtopics": []},
        {"topic": "Mental Abilities", "subtopics": ["Verbal", "Mechanical", "Numerical", "Social ability"]},
    ],

    "English Essay": [
        {"topic": "Philosophy, Abstract & Moral Quotes", "subtopics": []},
        {"topic": "International Relations & Global Issues", "subtopics": []},
        {"topic": "Economy & Poverty Alleviation", "subtopics": []},
        {"topic": "Science, Technology & AI", "subtopics": []},
        {"topic": "Environment & Energy Crisis", "subtopics": []},
        {"topic": "Democracy & Politics in Pakistan", "subtopics": []},
        {"topic": "Education & Literacy", "subtopics": []},
        {"topic": "Essay Writing Skills", "subtopics": [
            "Outline writing", "Thesis statement development", "Argument development & structure",
            "Coherence, style & vocabulary",
        ]},
    ],

    "Precis & Composition": [
        {"topic": "Precis Writing", "subtopics": []},
        {"topic": "Comprehension", "subtopics": []},
        {"topic": "Grammar & Sentence Correction", "subtopics": []},
        {"topic": "Vocabulary", "subtopics": [
            "Synonyms & antonyms", "Grouping words by meaning", "Distinguishing similarly spelled words",
        ]},
        {"topic": "Translation & Composition", "subtopics": ["Urdu to English translation"]},
    ],

    # --- Optional subjects (student's selected group) ---
    "Political Science I": [
        {"topic": "Political Theory", "subtopics": [
            "Concepts: state, sovereignty, liberty, equality, justice",
        ]},
        {"topic": "Classical Political Thinkers", "subtopics": ["Plato", "Aristotle", "Machiavelli"]},
        {"topic": "Modern Political Thinkers", "subtopics": ["Hobbes", "Locke", "Rousseau", "Montesquieu"]},
    ],
    "Political Science II": [
        {"topic": "Comparative Government Systems", "subtopics": []},
        {"topic": "Political Development & Modernization", "subtopics": []},
        {"topic": "International Politics", "subtopics": []},
        {"topic": "Political Institutions", "subtopics": []},
    ],
    "Gender Studies": [
        {"topic": "Gender and Development", "subtopics": []},
        {"topic": "Gender and Law", "subtopics": []},
        {"topic": "Feminist Theory", "subtopics": []},
        {"topic": "Gender in Pakistani Society", "subtopics": []},
    ],
    "Criminology": [
        {"topic": "Theories of Crime", "subtopics": []},
        {"topic": "Criminal Justice System", "subtopics": []},
        {"topic": "Juvenile Delinquency", "subtopics": []},
        {"topic": "Crime Prevention & Policy", "subtopics": []},
    ],
    "History of Indo-Pak": [
        {"topic": "Muslim Rule and Heritage in India (712-1857)", "subtopics": [
            "Arrival, foundation and consolidation of Muslim rule",
            "Slave Dynasty and the Mughals", "Art, architecture and literature",
            "Public administration under Muslim rule",
        ]},
        {"topic": "Decline of Muslim Rule and Rise of British Power", "subtopics": []},
        {"topic": "Muslim Reform and Revivalist Movements", "subtopics": []},
        {"topic": "Freedom Movement & Partition of India", "subtopics": []},
    ],
    "Sindhi": [
        {"topic": "Grammar", "subtopics": []},
        {"topic": "Composition", "subtopics": []},
        {"topic": "Literature", "subtopics": []},
    ],
}


def get_subjects():
    return list(SUBJECTS.keys())


def get_topics(subject):
    """Top-level topic names for a subject (used for selection & coverage tracking)."""
    return [t["topic"] for t in SUBJECTS.get(subject, [])]


def get_subtopics(subject, topic):
    """Sub-topics for a given topic, or [] if there aren't any / topic not found."""
    for t in SUBJECTS.get(subject, []):
        if t["topic"] == topic:
            return t["subtopics"]
    return []


def get_compulsory_subjects():
    return [
        "English Essay", "Precis & Composition", "General Science & Ability",
        "Current Affairs", "Pakistan Affairs", "Islamic Studies",
    ]
