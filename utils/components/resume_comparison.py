import streamlit as st
from utils.format_resume import format_resume


def show_resume_comparison(original_resume, rewritten_resume):
    """
    Display the original resume and AI rewritten resume side-by-side.
    """

    st.divider()

    st.header("📊 Resume Before vs After")

    st.caption(
        "Compare your uploaded resume with the AI-optimized version."
    )

    col1, col2 = st.columns(2)

    # ======================================================
    # ORIGINAL RESUME
    # ======================================================

    with col1:

        st.subheader("📄 Original Resume")

        st.text_area(
            label="",
            value=original_resume,
            height=650,
            key="original_resume_compare",
            disabled=True,
        )

    # ======================================================
    # AI REWRITTEN RESUME
    # ======================================================

    with col2:

        st.subheader("✨ AI Optimized Resume")

        formatted_resume = format_resume(rewritten_resume)

        st.text_area(
            label="",
            value=formatted_resume,
            height=650,
            key="rewritten_resume_compare",
            disabled=True,
        )

    st.success("✅ Resume Comparison Complete")