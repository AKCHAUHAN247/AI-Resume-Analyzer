import os
import json

from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Create Gemini client
client = genai.Client(api_key=api_key)


def analyze_resume(resume_text: str, job_description: str):
    prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze the following resume against the job description.

Resume:
{resume_text}

Job Description:
{job_description}

Return ONLY a valid JSON object.

Do NOT include markdown.

Do NOT use ```json.

Return exactly this structure:

{{
    "ats_score": 0,
    "job_match": "",
    "strengths": [],
    "weaknesses": [],
    "missing_skills": [],
    "suggestions": []
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    clean_text = response.text.strip()

    # Remove markdown if Gemini returns JSON
    clean_text = clean_text.replace("```json", "")
    clean_text = clean_text.replace("```", "")
    clean_text = clean_text.strip()

    return json.loads(clean_text)