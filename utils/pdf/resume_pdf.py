from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import HexColor


# -----------------------------
# Styles
# -----------------------------
styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.alignment = TA_CENTER
title_style.textColor = HexColor("#1F4E79")

heading = styles["Heading2"]
heading.textColor = HexColor("#1F4E79")

normal = styles["BodyText"]


# -----------------------------
# PDF Generator
# -----------------------------
def create_resume_pdf(rewrite, filename="AI_Rewritten_Resume.pdf"):

    doc = SimpleDocTemplate(filename)

    story = []

    # -----------------------------
    # Title
    # -----------------------------
    story.append(Paragraph("AI Rewritten Resume", title_style))
    story.append(Spacer(1, 20))

    # -----------------------------
    # Professional Summary
    # -----------------------------
    story.append(Paragraph("Professional Summary", heading))

    story.append(
        Paragraph(
            rewrite.get("professional_summary", ""),
            normal,
        )
    )

    story.append(Spacer(1, 18))

    # -----------------------------
    # Experience
    # -----------------------------
    story.append(Paragraph("Experience", heading))

    experiences = rewrite.get("experience", [])

    if not experiences:
        story.append(Paragraph("No experience available.", normal))

    for exp in experiences:

        if isinstance(exp, dict):

            title = exp.get("title", "")
            company = exp.get("company", "")
            description = exp.get("description", "")

            if title:
                story.append(
                    Paragraph(f"<b>{title}</b>", normal)
                )

            if company:
                story.append(
                    Paragraph(company, normal)
                )

            if description:
                story.append(
                    Paragraph(
                        description.replace("\n", "<br/>"),
                        normal,
                    )
                )

        else:

            story.append(
                Paragraph(
                    str(exp).replace("\n", "<br/>"),
                    normal,
                )
            )

        story.append(Spacer(1, 10))

    story.append(Spacer(1, 10))

    # -----------------------------
    # Projects
    # -----------------------------
    story.append(Paragraph("Projects", heading))

    projects = rewrite.get("projects", [])

    if not projects:
        story.append(Paragraph("No projects available.", normal))

    for project in projects:

        if isinstance(project, dict):

            name = project.get("name", "")
            description = project.get("description", "")

            if name:
                story.append(
                    Paragraph(f"<b>{name}</b>", normal)
                )

            if description:
                story.append(
                    Paragraph(
                        description.replace("\n", "<br/>"),
                        normal,
                    )
                )

        else:

            story.append(
                Paragraph(
                    str(project).replace("\n", "<br/>"),
                    normal,
                )
            )

        story.append(Spacer(1, 10))

    story.append(Spacer(1, 10))

    # -----------------------------
    # Skills
    # -----------------------------
    story.append(Paragraph("Skills", heading))

    skills_list = rewrite.get("skills", [])

    if isinstance(skills_list, list):
        skills = ", ".join(map(str, skills_list))
    else:
        skills = str(skills_list)

    story.append(
        Paragraph(skills, normal)
    )

    story.append(Spacer(1, 20))

    # -----------------------------
    # Build PDF
    # -----------------------------
    doc.build(story)

    return filename