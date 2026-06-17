from utils.gemini_client import analyze_resume

result = analyze_resume(
    "Python developer with Streamlit and Machine Learning experience.",
    "Looking for a Python AI Engineer with Streamlit, Gemini API and Machine Learning."
)

print(result)