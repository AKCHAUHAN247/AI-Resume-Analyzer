import os
import json

from dotenv import load_dotenv
from google import genai

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# -----------------------------
# Gemini Client
# -----------------------------
client = genai.Client(api_key=api_key)


# -----------------------------
# Resume Analyzer
# -----------------------------
def analyze_resume(resume_text: str, job_description: str):

    prompt = f"""
You are an expert ATS Resume Analyzer, Senior Technical Recruiter, and Career Coach.

Your task is to compare the resume against the provided job description and generate a realistic ATS analysis.

==============================
RESUME
==============================

{resume_text}

==============================
JOB DESCRIPTION
==============================

{job_description}

==============================
INSTRUCTIONS
==============================

Return ONLY a valid JSON object.

Do NOT return markdown.

Do NOT wrap the response inside ```json.

Do NOT explain anything.

Use ONLY this JSON schema:

{{
    "ats_score": 0,

    "job_match": "",

    "hire_recommendation": "",

    "resume_summary": "",

    "skill_scores": {{
        "Python": 0,
        "Machine Learning": 0,
        "Deep Learning": 0,
        "LLMs": 0,
        "LangChain": 0,
        "RAG": 0,
        "SQL": 0,
        "REST APIs": 0,
        "Git": 0,
        "Docker": 0,
        "AWS": 0,
        "GCP": 0,
        "Azure": 0,
        "Communication": 0
    }},

    "strengths": [],

    "weaknesses": [],

    "missing_skills": [],

    "suggestions": [],

    "cover_letter": "",

    "interview_questions": [],

    "interview_probability": 0,

    "offer_probability": 0,

    "expected_salary": "",

    "resume_quality": "",

    "top_strengths": [],

    "top_concerns": [],

    "resume_rewrite": {{

    "professional_summary": "",

    "experience": [],

    "projects": [],

    "skills": []
    }}

}}

==============================
SCORING RULES
==============================

ATS Score:
- Between 0 and 100.
- Be realistic.
- Never give 100 unless nearly perfect.

Job Match:
Choose ONLY one:

Low Match

Moderate Match

High Match

Excellent Match

Hire Recommendation:
Choose ONLY one:

Reject

Consider

Hire

Strong Hire

Resume Summary:
Write 2-4 professional recruiter-style sentences.

Skill Scores:
Every skill must have a value between 0 and 100.

If missing:
0-20

Basic:
20-40

Intermediate:
40-60

Good:
60-80

Strong:
80-95

Exceptional:
95-100

Strengths:
5-8 bullet points.

Weaknesses:
3-6 bullet points.

Missing Skills:
List only skills actually missing.

Suggestions:
Provide 5-8 actionable improvements.

==============================
AI RESUME REWRITER
==============================

Rewrite the resume professionally.

Improve grammar.

Improve ATS optimization.

Rewrite weak bullet points.

Use STAR format wherever possible.

Do NOT invent fake work experience.

Do NOT add certifications that do not exist.

Do NOT add fake companies.

Only improve the wording of the existing resume.

Return the rewritten resume inside:

resume_rewrite

professional_summary:
Create a recruiter-quality professional summary.

experience:
Rewrite every experience bullet professionally.

projects:
Rewrite every project professionally using action verbs and measurable impact where possible.

skills:
Return an optimized skills list.

cover_letter:

Generate a professional cover letter.

Requirements:

- Address the hiring manager professionally.
- Tailor it to the provided job description.
- Highlight the candidate's strongest skills.
- Explain why the candidate is a strong fit.
- Keep it between 250–350 words.
- Do NOT use markdown.
- Return it as a plain string.

==============================
INTERVIEW QUESTIONS
==============================

Generate 20 interview questions based on the resume and job description.

Return them as a list.

Each item must contain:

Each item must contain:

{{
    "question":"",
    "difficulty":"",
    "answer":"",
    "tip":""
}}

Difficulty should be one of:

Easy
Medium
Hard

==============================
RECRUITER DASHBOARD
==============================

Estimate:

Interview Probability (0-100)

Offer Probability (0-100)

Expected Salary

Resume Quality

Choose one:

Poor

Average

Good

Excellent

Top Strengths

Return 3-5 items.

Top Concerns

Return 3-5 items.

Be realistic.

Return ONLY valid JSON.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    clean_text = response.text.strip()

    # Remove markdown if Gemini accidentally returns it
    clean_text = clean_text.replace("```json", "")
    clean_text = clean_text.replace("```", "")
    clean_text = clean_text.strip()

    try:
        return json.loads(clean_text)

    except json.JSONDecodeError:

        print("========== GEMINI RESPONSE ==========")
        print(clean_text)
        print("=====================================")

        raise Exception("Gemini returned invalid JSON.")