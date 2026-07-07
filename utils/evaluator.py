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

def evaluate_answer(
    question,
    answer
):

    prompt = f"""
You are an expert interview evaluator.

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer and provide:

1. Technical Accuracy (Score out of 10)
2. Communication Skills (Score out of 10)
3. Confidence Level (Score out of 10)
4. Completeness (Score out of 10)
5. Strengths
6. Areas for Improvement
7. Overall Score (out of 10)

Provide the response in a professional format.
"""

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return f"Error: {str(e)}"