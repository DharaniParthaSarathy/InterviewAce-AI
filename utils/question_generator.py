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

def generate_questions(
    resume_text,
    job_description
):

    prompt = f"""
You are an expert interviewer.

Generate personalized interview questions.

Resume:
{resume_text}

Job Description:
{job_description}

Generate:

1. 5 Technical Questions
2. 5 Project Questions
3. 5 Behavioral Questions
4. 5 HR Questions

Questions must be based on:
- Candidate skills
- Candidate projects
- Job Description requirements

Return only questions.
"""

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return f"Error: {str(e)}"