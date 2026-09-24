"""
app.py
CSS Study Tutor Agent - Streamlit front end.

Modes: Study, Question Analysis, Handwritten Answer (OCR + assessment),
Answer Practice (typed), Study Plan, Progress.

Assessment reports are saved to Supabase (see memory.py) so a student's
history and weak-topic tracking survive closing the app / redeploys.
"""

import streamlit as st

import agent
import assessment
import memory
import ocr
from curriculum import get_subjects, get_topics

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
            "📷 Handwritten Answer",
            "📅 Study Plan",
            "📊 Progress",
        ],
    )

subject = st.selectbox("Subject", get_subjects())

# ---------------------------------------------------------------------------
if mode == "📖 Study":
    st.header("📖 Study")
    topic = st.selectbox("Topic", get_topics(subject))
    if st.button("Explain this topic"):
        with st.spinner("Thinking..."):
            result = agent.study_topic(subject, topic)
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
    question = st.text_area("Question")
    answer = st.text_area("Your answer", height=250)
    if st.button("Assess my answer") and question.strip() and answer.strip():
        with st.spinner("Assessing..."):
            result = assessment.assess_answer(subject, question, answer)
        st.session_state["last_assessment"] = (subject, question, answer, result)

    if "last_assessment" in st.session_state:
        subj, q, a, result = st.session_state["last_assessment"]
        st.subheader("📊 Assessment")
        ratings = result.get("ratings", {})
        for k, v in ratings.items():
            st.write(f"**{k.title()}**: {v}")
        st.markdown("**✅ Strengths**")
        for s in result.get("strengths", []):
            st.write(f"- {s}")
        st.markdown("**⚠️ Areas to improve**")
        for w in result.get("areas_to_improve", []):
            st.write(f"- {w}")
        if result.get("next_practice"):
            st.markdown(f"**🎯 Next practice:** {result['next_practice']}")
        if result.get("raw_response"):
            st.caption("Raw model response (couldn't parse as structured JSON):")
            st.text(result["raw_response"])

        if st.session_state.student_id and st.button("💾 Save this assessment"):
            ok = memory.save_assessment(st.session_state.student_id, subj, q, a, result)
            if ok:
                st.success("Saved to your history.")
            else:
                st.error(memory.connection_error() or "Could not save - check Supabase setup.")

# ---------------------------------------------------------------------------
elif mode == "📷 Handwritten Answer":
    st.header("📷 Handwritten Answer")
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
            st.session_state["last_assessment"] = (subject, question, edited, result)

    if "last_assessment" in st.session_state:
        subj, q, a, result = st.session_state["last_assessment"]
        st.subheader("📊 Assessment")
        ratings = result.get("ratings", {})
        for k, v in ratings.items():
            st.write(f"**{k.title()}**: {v}")
        st.markdown("**✅ Strengths**")
        for s in result.get("strengths", []):
            st.write(f"- {s}")
        st.markdown("**⚠️ Areas to improve**")
        for w in result.get("areas_to_improve", []):
            st.write(f"- {w}")
        if result.get("next_practice"):
            st.markdown(f"**🎯 Next practice:** {result['next_practice']}")

        if st.session_state.student_id and st.button("💾 Save this assessment", key="save_handwritten"):
            ok = memory.save_assessment(st.session_state.student_id, subj, q, a, result)
            if ok:
                st.success("Saved to your history.")
            else:
                st.error(memory.connection_error() or "Could not save - check Supabase setup.")

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
elif mode == "📊 Progress":
    st.header("📊 Progress")
    if not st.session_state.student_id:
        st.info("Enter your name / student ID in the sidebar to see your progress.")
    else:
        history = memory.get_history(st.session_state.student_id, subject, limit=50)
        st.write(f"**Recent answers analyzed:** {len(history)}")

        weak = memory.get_weak_topics(st.session_state.student_id, subject)
        if weak:
            st.subheader("⚠️ Repeated weak areas")
            for w, count in weak:
                st.write(f"- {w} (seen {count}x)")
        else:
            st.info("No weak areas tracked yet - complete some Answer Practice or Handwritten Answer assessments.")

        if history:
            st.subheader("🗂️ History")
            for item in history:
                with st.expander(f"{item.get('created_at', '')[:16]} - {item.get('question', '')[:60]}"):
                    st.write("**Question:**", item.get("question"))
                    st.write("**Your answer:**", item.get("answer_text"))
                    st.write("**Assessment:**", item.get("assessment"))
