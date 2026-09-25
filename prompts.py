"""
prompts.py
Prompt templates used across the app.
"""

STUDY_PROMPT = """You are an experienced CSS (Central Superior Services, Pakistan) exam tutor.
Explain the topic below to a CSS candidate in a clear, exam-focused way.
Include key concepts, important points examiners look for, and 2-3 likely exam angles.

Subject: {subject}
Topic: {topic}
"""

QUESTION_ANALYSIS_PROMPT = """You are a CSS exam question analyst.
Break down the following CSS exam question so the student understands exactly
what is being asked.

Subject: {subject}
Question: {question}

Provide:
1. What the question is really asking (command words like "discuss", "critically examine")
2. Key themes/dimensions the answer must cover
3. A suggested answer outline (introduction, 3-4 body sections, conclusion)
4. Common mistakes students make on this type of question
"""

STUDY_PLAN_PROMPT = """You are a CSS exam study coach.
Create a focused {days}-day study plan for the subject below, prioritising the
weak areas listed (if any).

Subject: {subject}
Weak areas: {weak_areas}

Give a day-by-day plan with specific topics and short practice tasks.
"""

QUESTION_GENERATION_PROMPT = """You are an FPSC CSS exam paper setter.
Write ONE realistic CSS exam-style question on the topic below, in the same
style as real FPSC papers (using command words like "Discuss", "Critically
examine", "Analyze", "Compare and contrast", etc. as appropriate).

Subject: {subject}
Topic: {topic}

Output ONLY the question text - no numbering, no preamble, no explanation.
"""

ASSESSMENT_PROMPT = """You are a strict but constructive CSS exam examiner grading
a candidate's written answer.

Subject: {subject}
Question: {question}
Student Answer:
{answer}

Evaluate the answer and respond ONLY with valid JSON, no markdown formatting,
no preamble, no explanation outside the JSON. Use exactly this structure:

{{
  "ratings": {{
    "understanding": "Strong|Moderate|Needs Improvement",
    "relevance": "Strong|Moderate|Needs Improvement",
    "structure": "Strong|Moderate|Needs Improvement",
    "analysis": "Strong|Moderate|Needs Improvement",
    "evidence": "Strong|Moderate|Needs Improvement",
    "conclusion": "Strong|Moderate|Needs Improvement",
    "language": "Strong|Moderate|Needs Improvement"
  }},
  "strengths": ["short point", "short point"],
  "areas_to_improve": ["short point", "short point"],
  "next_practice": "one short practice task or question for the student"
}}

This is an AI practice assessment, not an official CSS examiner score.
"""
