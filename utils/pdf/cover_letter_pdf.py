from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import HexColor


styles = getSampleStyleSheet()

title_style = styles["Heading1"]
title_style.alignment = TA_CENTER
title_style.textColor = HexColor("#1F4E79")

normal = styles["BodyText"]


def create_cover_letter_pdf(
    cover_letter,
    filename="AI_Cover_Letter.pdf",
):

    doc = SimpleDocTemplate(filename)

    story = []

    story.append(
        Paragraph(
            "AI Generated Cover Letter",
            title_style,
        )
    )

    story.append(Spacer(1, 20))

    paragraphs = cover_letter.split("\n")

    for para in paragraphs:

        if para.strip():

            story.append(
                Paragraph(
                    para,
                    normal,
                )
            )

            story.append(
                Spacer(1, 12)
            )

    doc.build(story)

    return filename