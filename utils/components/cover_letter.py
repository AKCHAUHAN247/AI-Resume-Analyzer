import streamlit as st
from utils.pdf.cover_letter_pdf import create_cover_letter_pdf

def show_cover_letter(result):

    st.divider()

    st.header("💌 AI Cover Letter")

    st.caption(
        "Generated specifically for this job description."
    )

    cover = result.get("cover_letter", "")

    edited_cover = st.text_area(
        "Edit if needed",
        value=cover,
        height=400,
        key="cover_letter"
    )

    pdf_file = create_cover_letter_pdf(edited_cover)

    with open(pdf_file, "rb") as pdf:

        st.download_button(
            label="📄 Download Cover Letter PDF",
            data=pdf,
            file_name="AI_Cover_Letter.pdf",
            mime="application/pdf",
        )

    st.success("✅ Cover Letter Ready")