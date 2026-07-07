import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from utils.langchain.prompt import (
    analysis_prompt,
    optimizer_prompt,
    question_prompt,
    skill_gap_prompt,
    career_coach_prompt,
    evaluation_prompt
)

# ---------------------------------------------------------
# Load Environment Variables
# ---------------------------------------------------------

load_dotenv()

# ---------------------------------------------------------
# Initialize Gemini Model
# ---------------------------------------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.3
)

# ---------------------------------------------------------
# Generic LLM Function
# ---------------------------------------------------------

def invoke_llm(prompt):

    """
    Sends the formatted prompt to Gemini
    and returns the generated response.
    """

    try:

        response = llm.invoke(prompt)

        return response.content

    except Exception as e:

        return f"Error: {str(e)}"

# ---------------------------------------------------------
# Resume Analysis Chain
# ---------------------------------------------------------

def run_analysis_chain(
    context,
    job_description
):

    prompt = analysis_prompt.format(
        context=context,
        job_description=job_description
    )

    return invoke_llm(prompt)

# ---------------------------------------------------------
# Resume Optimization Chain
# ---------------------------------------------------------

def run_optimizer_chain(
    context,
    job_description
):

    prompt = optimizer_prompt.format(
        context=context,
        job_description=job_description
    )

    return invoke_llm(prompt)

# ---------------------------------------------------------
# Skill Gap Chain
# ---------------------------------------------------------

def run_skill_gap_chain(
    context,
    job_description
):

    prompt = skill_gap_prompt.format(
        context=context,
        job_description=job_description
    )

    return invoke_llm(prompt)

# ---------------------------------------------------------
# Interview Question Chain
# ---------------------------------------------------------

def run_question_chain(
    context,
    job_description
):

    prompt = question_prompt.format(
        context=context,
        job_description=job_description
    )

    return invoke_llm(prompt)

# ---------------------------------------------------------
# Interview Evaluation Chain
# ---------------------------------------------------------

def run_evaluation_chain(
    question,
    answer
):

    prompt = evaluation_prompt.format(
        question=question,
        answer=answer
    )

    return invoke_llm(prompt)

# ---------------------------------------------------------
# Career Coach Chain
# ---------------------------------------------------------

def run_career_coach_chain(
    context,
    job_description
):

    prompt = career_coach_prompt.format(
        context=context,
        job_description=job_description
    )

    return invoke_llm(prompt)