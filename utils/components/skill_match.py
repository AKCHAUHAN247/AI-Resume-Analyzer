import streamlit as st


def get_color(score):
    if score >= 80:
        return "🟢"
    elif score >= 60:
        return "🟡"
    else:
        return "🔴"


def show_skill_match(result):

    st.subheader("🎯 AI Skill Match Dashboard")
    st.caption("AI evaluated every important skill against the job description.")

    skills = result.get("skill_scores", {})

    if not skills:
        st.warning("No skill scores available.")
        return

    # Highest scores first
    skills = dict(
        sorted(
            skills.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )

    for skill, score in skills.items():

        emoji = get_color(score)

        left, right = st.columns([5, 1])

        with left:
            st.markdown(
                f"### {emoji} {skill}"
            )

            st.progress(score)

        with right:
            st.metric(
                "",
                f"{score}%"
            )

        st.markdown("---")