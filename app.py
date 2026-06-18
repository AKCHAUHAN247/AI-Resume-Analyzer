from utils.components.resume_rewriter import show_resume_rewriter
from utils.components.radar_chart import show_radar_chart
from utils.components.gauge import show_gauge
from utils.components.skill_match import show_skill_match
from utils.components.cover_letter import show_cover_letter
from utils.components.interview_coach import show_interview_questions
from utils.components.recruiter_dashboard import show_recruiter_dashboard
from utils.components.resume_comparison import show_resume_comparison
import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.gemini_client import analyze_resume

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Load CSS
# -----------------------------
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.title("🤖 AI Resume Analyzer Pro")
st.caption("Built with Gemini AI | ATS Resume Scanner | AI Career Assistant")

st.divider()

# -----------------------------
# Upload Section
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    uploaded_resume = st.file_uploader(
        "📄 Upload Resume",
        type=["pdf"]
    )

with col2:
    job_description = st.text_area(
        "💼 Paste Job Description",
        height=220
    )

st.divider()

# -----------------------------
# Analyze
# -----------------------------
if st.button("🚀 Analyze Resume", use_container_width=True):

    if uploaded_resume is None:
        st.warning("Please upload your resume.")
        st.stop()

    if job_description.strip() == "":
        st.warning("Please paste the Job Description.")
        st.stop()

    with st.spinner("🤖 Gemini is analyzing your resume..."):

        resume_text = extract_text_from_pdf(uploaded_resume)

        result = analyze_resume(
            resume_text,
            job_description
        )

    st.success("Analysis Complete!")

    # -----------------------------
    # AI Executive Summary
    # -----------------------------
    st.subheader("📝 AI Executive Summary")

    st.info(result["resume_summary"])

    st.markdown("### 💼 Hiring Recommendation")

    recommendation = result["hire_recommendation"]

    if recommendation == "Strong Hire":
        st.success("🟢 STRONG HIRE")

    elif recommendation == "Hire":
        st.success("🟢 HIRE")

    elif recommendation == "Consider":
        st.warning("🟡 CONSIDER")

    else:
        st.error("🔴 REJECT")

    st.divider()
    st.divider()

    # -----------------------------
    # Metrics
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 ATS Score")
        show_gauge(result["ats_score"])

    with col2:
        st.subheader("💼 Job Match")
        st.success(result["job_match"])

    st.divider()
    
        # -----------------------------
    # Resume Health Dashboard
    # -----------------------------
    st.subheader("📊 Resume Health Dashboard")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "💪 Strengths",
            len(result["strengths"])
        )

    with c2:
        st.metric(
            "❌ Weaknesses",
            len(result["weaknesses"])
        )

    with c3:
        st.metric(
            "⚠ Missing Skills",
            len(result["missing_skills"])
        )

    c4, c5, c6 = st.columns(3)

    with c4:
        st.metric(
            "💡 Suggestions",
            len(result["suggestions"])
        )

    with c5:
        st.metric(
            "📈 ATS Score",
            f'{result["ats_score"]}%'
        )

    with c6:
        st.metric(
            "🎯 Job Match",
            result["job_match"]
        )

    st.divider()

    show_skill_match(result)

    st.divider()

    show_radar_chart(result)

    st.divider()

    st.subheader("✅ Strengths")

    for item in result["strengths"]:
        st.success(item)

    st.subheader("❌ Weaknesses")

    for item in result["weaknesses"]:
        st.error(item)

    st.subheader("⚠ Missing Skills")

    for item in result["missing_skills"]:
        st.warning(item)

    st.subheader("💡 Suggestions")

    for item in result["suggestions"]:
        st.info(item)
    st.divider() 
    show_resume_comparison(
    resume_text,
    result.get("resume_rewrite", {})
    )
    show_resume_rewriter(result)
    show_cover_letter(result)
    show_interview_questions(result)
    show_recruiter_dashboard(result)