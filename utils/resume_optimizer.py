import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API Key
load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def optimize_resume(
    resume_text,
    job_description
):

    prompt = f"""
You are an expert ATS Resume Writer.

Optimize the resume according to the Job Description.

IMPORTANT RULES:

1. Do NOT add fake experience.
2. Do NOT add fake projects.
3. Do NOT add fake certifications.
4. Do NOT invent skills.
5. Only improve wording.
6. Improve ATS keyword alignment.
7. Keep original meaning.

Return the complete optimized resume.

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