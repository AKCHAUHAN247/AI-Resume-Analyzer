def clean_text(text):
    """Clean markdown text."""

    if not text:
        return ""

    if isinstance(text, list):
        return "\n".join(f"• {item}" for item in text)

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


def format_resume(rewrite):
    """
    Returns a clean Markdown formatted resume.
    """

    resume = ""

    # ==========================================
    # SUMMARY
    # ==========================================

    summary = clean_text(
        rewrite.get("professional_summary", "")
    )

    if summary:
        resume += "# 👤 Professional Summary\n\n"
        resume += summary + "\n\n"

    # ==========================================
    # EXPERIENCE
    # ==========================================

    experience = rewrite.get("experience", [])

    if experience:

        resume += "---\n\n"
        resume += "# 💼 Experience\n\n"

        for exp in experience:

            if isinstance(exp, dict):

                title = clean_text(exp.get("title", ""))
                company = clean_text(exp.get("company", ""))
                description = clean_text(exp.get("description", ""))

                resume += f"### {title}\n"

                if company:
                    resume += f"**{company}**\n\n"

                resume += description + "\n\n"

            else:

                resume += clean_text(exp)
                resume += "\n\n"

    # ==========================================
    # PROJECTS
    # ==========================================

    projects = rewrite.get("projects", [])

    if projects:

        resume += "---\n\n"
        resume += "# 🚀 Projects\n\n"

        for project in projects:

            if isinstance(project, dict):

                name = clean_text(project.get("name", ""))
                description = clean_text(project.get("description", ""))

                resume += f"### {name}\n\n"
                resume += description + "\n\n"

            else:

                resume += clean_text(project)
                resume += "\n\n"

    # ==========================================
    # SKILLS
    # ==========================================

    skills = rewrite.get("skills", [])

    if skills:

        resume += "---\n\n"
        resume += "# 🛠 Skills\n\n"

        if isinstance(skills, list):

            for skill in skills:
                resume += f"- {skill}\n"

        else:

            resume += clean_text(skills)

    return resume