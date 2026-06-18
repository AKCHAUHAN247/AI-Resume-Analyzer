import streamlit as st


def show_interview_questions(result):

    st.divider()

    st.header("🎤 AI Interview Coach")

    st.caption(
        "Practice interview questions generated specifically for this role."
    )

    questions = result.get("interview_questions", [])

    if not questions:
        st.info("No interview questions generated.")
        return

    for i, q in enumerate(questions, 1):

        with st.expander(f"Question {i}"):

            st.markdown(f"### ❓ {q.get('question','')}")

            st.write(
                f"**Difficulty:** {q.get('difficulty','')}"
            )

            st.markdown("### ✅ Suggested Answer")

            st.write(q.get("answer",""))

            st.markdown("### 💡 Recruiter Tip")

            st.info(q.get("tip",""))