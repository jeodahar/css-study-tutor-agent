# CSS Study Tutor Agent

A Streamlit + CrewAI + Groq app to help CSS (Central Superior Services, Pakistan)
candidates study, analyze exam questions, practice answers (typed or handwritten
photo via OCR), get AI examiner-style assessments, and track weak areas over time.

## Features
- 📖 Study mode - topic explanations per subject
- 🔍 Question analysis - breaks down what a question is really asking
- ✍️ Answer practice - type an answer, get a structured AI assessment
- 📷 Handwritten answer - upload a photo, OCR extracts the text, then assess it
- 📅 Study plan - day-by-day plan, prioritizing your recorded weak areas
- 📊 Progress - history of assessments and repeated weak areas (saved in Supabase,
  so it survives closing the app or a redeploy)

## 1. Get your free API keys

**Groq (LLM + vision OCR)**
1. Go to https://console.groq.com → API Keys → Create key
2. Copy it - you'll need it as `GROQ_API_KEY`

**Supabase (free database, for persistent history)**
1. Go to https://supabase.com → New project (free tier)
2. Once created: Project Settings → API → copy the `Project URL` (`SUPABASE_URL`)
   and the `anon public` key (`SUPABASE_KEY`)
3. Go to SQL Editor → New query → paste the contents of `supabase_schema.sql` → Run

## 2. Put the code on GitHub
1. Create a new repo on GitHub (e.g. `css-study-tutor-agent`)
2. Upload all files in this folder via the GitHub web UI ("Add file" → "Upload files")
3. Commit

## 3. Deploy on Streamlit Community Cloud (free)
1. Go to https://share.streamlit.io → New app
2. Pick your repo, branch `main`, main file `app.py`
3. Before/after deploying, go to **Settings → Secrets** and paste:

```toml
GROQ_API_KEY = "your-groq-key"
GROQ_MODEL = "openai/gpt-oss-120b"
GROQ_VISION_MODEL = "llama-3.2-90b-vision-preview"
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-supabase-anon-key"
```

4. Deploy. The app will be live at a `*.streamlit.app` URL.

## Notes
- If Supabase isn't configured yet, the app still works - it just won't save
  progress between sessions (you'll see a warning in the sidebar).
- The "student ID" field is a simple name/ID, not a real login - good enough
  for personal use; add real auth later if you share this with others.
- Assessment scores are AI practice feedback, not an official CSS examiner score.

## Project structure
```
app.py              Streamlit UI
agent.py             CrewAI Study Tutor Agent (study, question analysis, study plan)
tools.py             Web search helper (current affairs)
memory.py            Supabase persistence (assessment history, weak topics)
curriculum.py         CSS subjects + topics
ocr.py               Handwritten answer OCR (Groq vision model)
assessment.py         Answer assessment logic (structured JSON output)
config.py             API/model configuration
prompts.py             Prompt templates
requirements.txt       Dependencies
supabase_schema.sql     Run once in Supabase SQL editor
.gitignore
```
