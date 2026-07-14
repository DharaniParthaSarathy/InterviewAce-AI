import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from utils.langchain.prompt import (
    analysis_prompt,
    optimizer_prompt,
    skill_gap_prompt,
    question_prompt,
    evaluation_prompt,
    career_coach_prompt
)

# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv()

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# ==========================================================
# Initialize Gemini LLM
# ==========================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.3
)

# ==========================================================
# Generic Gemini Function
# ==========================================================

def invoke_llm(prompt: str) -> str:
    """
    Sends a formatted prompt to Gemini
    and returns the generated response.
    """

    try:

        response = llm.invoke(prompt)

        return response.content

    except Exception as e:

        return f"LLM Error: {str(e)}"


# ==========================================================
# Resume Analysis Chain
# ==========================================================

def run_analysis_chain(
    context: str,
    job_description: str
) -> str:

    prompt = analysis_prompt.format(
        context=context,
        job_description=job_description
    )

    return invoke_llm(prompt)


# ==========================================================
# Resume Optimizer Chain
# ==========================================================

def run_optimizer_chain(
    context: str,
    job_description: str
) -> str:

    prompt = optimizer_prompt.format(
        context=context,
        job_description=job_description
    )

    return invoke_llm(prompt)


# ==========================================================
# Skill Gap Chain
# ==========================================================

def run_skill_gap_chain(
    context: str,
    job_description: str
) -> str:

    prompt = skill_gap_prompt.format(
        context=context,
        job_description=job_description
    )

    return invoke_llm(prompt)


# ==========================================================
# Interview Question Chain
# ==========================================================

def run_question_chain(
    context: str,
    job_description: str
) -> str:
    """
    Generates:

    • Job Description Analysis
    • Technical Questions
    • Project Questions
    • Behavioural Questions
    • HR Questions
    • Job Description Specific Questions
    """

    prompt = question_prompt.format(
        context=context,
        job_description=job_description
    )

    return invoke_llm(prompt)


# ==========================================================
# Interview Evaluation Chain
# ==========================================================

def run_evaluation_chain(
    question: str,
    answer: str
) -> str:

    prompt = evaluation_prompt.format(
        question=question,
        answer=answer
    )

    return invoke_llm(prompt)


# ==========================================================
# Career Coach Chain
# ==========================================================

def run_career_coach_chain(
    context: str,
    job_description: str
) -> str:

    prompt = career_coach_prompt.format(
        context=context,
        job_description=job_description
    )

    return invoke_llm(prompt)