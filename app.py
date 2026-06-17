import streamlit as st
from utils.pdf_reader import extract_text_from_pdf
from utils.gemini_client import analyze_resume
# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Resume Analyzer Pro",
    page_icon="📄",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("📄 AI Resume Analyzer Pro")
st.caption("Analyze your resume using Gemini AI")

st.divider()

# -----------------------------
# Layout
# -----------------------------
left, right = st.columns([1, 1])

with left:
    uploaded_resume = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"]
    )

with right:
    job_description = st.text_area(
        "Paste Job Description",
        height=250
    )

st.divider()

if st.button("🚀 Analyze Resume", use_container_width=True):

    if uploaded_resume is None:
        st.error("Please upload a resume.")
        st.stop()

    if job_description.strip() == "":
        st.error("Please paste the Job Description.")
        st.stop()

    with st.spinner("📄 Reading Resume..."):
        resume_text = extract_text_from_pdf(uploaded_resume)

    with st.spinner("🤖 Gemini is analyzing your resume..."):
        result = analyze_resume(
            resume_text,
            job_description
        )

    st.success("Analysis Complete!")

    st.markdown("---")

    st.markdown(result)