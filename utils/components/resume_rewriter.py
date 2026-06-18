import streamlit as st
from utils.pdf.resume_pdf import create_resume_pdf


def clean_text(text):
    """Remove markdown formatting and safely handle lists."""

    if not text:
        return ""

    # If Gemini returns a list of bullet points
    if isinstance(text, list):
        text = "\n".join(f"• {item}" for item in text)

    # If Gemini returns anything else (dict, int, etc.)
    if not isinstance(text, str):
        text = str(text)

    return (
        text.replace("####", "")
            .replace("###", "")
            .replace("##", "")
            .replace("#", "")
            .replace("**", "")
            .replace("* ", "• ")
            .strip()
    )


def show_resume_rewriter(result):

    rewrite = result.get("resume_rewrite", {})

    st.header("✨ AI Resume Studio")

    st.caption(
        "AI has rewritten your resume to improve ATS compatibility and recruiter appeal."
    )

    # ==========================================================
    # PROFESSIONAL SUMMARY
    # ==========================================================

    st.subheader("📝 Professional Summary")

    summary = st.text_area(
        "Edit if needed",
        value=clean_text(rewrite.get("professional_summary", "")),
        height=150,
        key="summary"
    )

    st.divider()

    # ==========================================================
    # EXPERIENCE
    # ==========================================================

    st.subheader("💼 Experience")

    experience = ""

    for exp in rewrite.get("experience", []):

        if isinstance(exp, dict):

            title = clean_text(exp.get("title", ""))
            company = clean_text(exp.get("company", ""))
            description = clean_text(exp.get("description", ""))

            experience += f"""
{title}

{company}

{description}

"""

        else:

            experience += clean_text(exp) + "\n\n"

    experience = st.text_area(
        "",
        value=experience,
        height=260,
        key="experience"
    )

    st.divider()

    # ==========================================================
    # PROJECTS
    # ==========================================================

    st.subheader("🚀 Projects")

    projects = ""

    for project in rewrite.get("projects", []):

        if isinstance(project, dict):

            name = clean_text(project.get("name", ""))
            description = clean_text(project.get("description", ""))

            projects += f"""
{name}

{description}

"""

        else:

            projects += clean_text(project) + "\n\n"

    projects = st.text_area(
        "",
        value=projects,
        height=260,
        key="projects"
    )

    st.divider()

    # ==========================================================
    # SKILLS
    # ==========================================================

    st.subheader("🛠 Skills")

    skills = ", ".join(
        rewrite.get("skills", [])
    )

    skills = st.text_area(
        "",
        value=skills,
        height=130,
        key="skills"
    )

    st.divider()

    # ==========================================================
    # UPDATE REWRITE OBJECT
    # ==========================================================

    rewrite["professional_summary"] = summary

    rewrite["experience"] = [
        line for line in experience.split("\n\n")
        if line.strip()
    ]

    rewrite["projects"] = [
        line for line in projects.split("\n\n")
        if line.strip()
    ]

    rewrite["skills"] = [
        skill.strip()
        for skill in skills.split(",")
        if skill.strip()
    ]

    # ==========================================================
    # PDF DOWNLOAD
    # ==========================================================

    pdf_path = create_resume_pdf(rewrite)

    with open(pdf_path, "rb") as pdf:

        st.download_button(
            label="📄 Download Complete Resume",
            data=pdf,
            file_name="AI_Rewritten_Resume.pdf",
            mime="application/pdf",
            use_container_width=True,
        )

    st.success("✅ AI Resume Rewrite Complete")