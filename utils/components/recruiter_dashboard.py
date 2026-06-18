import streamlit as st


def get_quality_color(quality):

    quality = quality.lower()

    if quality == "excellent":
        return "🟢"

    if quality == "good":
        return "🟢"

    if quality == "average":
        return "🟡"

    return "🔴"


def show_recruiter_dashboard(result):

    st.divider()

    st.header("👨‍💼 Recruiter Intelligence Dashboard")

    st.caption(
        "AI-powered hiring insights generated from your resume."
    )

    # =============================================
    # TOP METRICS
    # =============================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "🎯 Interview Probability",
            f"{result.get('interview_probability',0)}%"
        )

    with c2:

        st.metric(
            "💼 Offer Probability",
            f"{result.get('offer_probability',0)}%"
        )

    with c3:

        st.metric(
            "💰 Expected Salary",
            result.get("expected_salary","N/A")
        )

    with c4:

        quality = result.get(
            "resume_quality",
            "Good"
        )

        st.metric(
            "⭐ Resume Quality",
            quality
        )

    st.divider()

    # =============================================
    # PROGRESS BARS
    # =============================================

    st.subheader("📊 Hiring Confidence")

    interview = result.get(
        "interview_probability",
        0
    )

    offer = result.get(
        "offer_probability",
        0
    )

    st.markdown(
        f"**Interview Probability — {interview}%**"
    )

    st.progress(interview)

    st.markdown(
        f"**Offer Probability — {offer}%**"
    )

    st.progress(offer)

    st.divider()

    # =============================================
    # QUALITY
    # =============================================

    emoji = get_quality_color(
        result.get(
            "resume_quality",
            "Good"
        )
    )

    st.subheader(
        f"{emoji} Overall Resume Quality"
    )

    st.info(
        result.get(
            "resume_quality",
            "Good"
        )
    )

    st.divider()

    # =============================================
    # STRENGTHS & CONCERNS
    # =============================================

    left, right = st.columns(2)

    with left:

        st.subheader("✅ Top Strengths")

        strengths = result.get(
            "top_strengths",
            []
        )

        if strengths:

            for item in strengths:
                st.success(item)

        else:

            st.info("No strengths detected.")

    with right:

        st.subheader("⚠ Top Concerns")

        concerns = result.get(
            "top_concerns",
            []
        )

        if concerns:

            for item in concerns:
                st.warning(item)

        else:

            st.success("No major concerns.")

    st.divider()

    # =============================================
    # FINAL DECISION
    # =============================================

    recommendation = result.get(
        "hire_recommendation",
        "Consider"
    )

    st.subheader("🏁 Recruiter Decision")

    if recommendation == "Strong Hire":

        st.success("🟢 STRONG HIRE")

    elif recommendation == "Hire":

        st.success("🟢 HIRE")

    elif recommendation == "Consider":

        st.warning("🟡 CONSIDER")

    else:

        st.error("🔴 REJECT")