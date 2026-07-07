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

def extract_skills(text):

    prompt = f"""
Extract professional skills from the following text.

Return one skill per line.

Text:
{text[:3000]}
"""

    try:

        response = model.generate_content(prompt)

        print("\n===== GEMINI RESPONSE =====")
        print(response.text)
        print("===========================\n")

        skills = []

        for line in response.text.split("\n"):

            line = line.strip()

            if line:
                skills.append(line)

        return skills

    except Exception as e:

        print("\n===== ERROR =====")
        print(e)
        print("=================\n")

        return []