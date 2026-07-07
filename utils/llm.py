import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def analyze_resume_jd(
    resume_text,
    job_description
):

    prompt = f"""
You are an expert recruiter and interview coach.

Analyze the following resume against the job description.

Provide:

1. Job Match Score
2. Matched Skills
3. Missing Skills
4. Candidate Strengths
5. Areas for Improvement
6. Final Recommendation

Resume:
{resume_text}

Job Description:
{job_description}
"""

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return f"Error: {str(e)}"