import re

from langgraph_agents.state import InterviewAceState

from utils.langchain.chain import run_skill_gap_chain


def skill_gap_agent(
    state: InterviewAceState
) -> InterviewAceState:

    """
    Skill Gap Agent

    Responsibilities
    ----------------
    1. Analyze the resume against the Job Description.
    2. Identify missing skills.
    3. Recommend skills to learn.
    4. Update the LangGraph shared state.
    """

    print("\n========== Skill Gap Agent ==========\n")

    try:

        # ---------------------------------------------
        # Read State
        # ---------------------------------------------

        context = state["context"]

        job_description = state["job_description"]

        # ---------------------------------------------
        # Run Skill Gap Analysis
        # ---------------------------------------------

        skill_gap = run_skill_gap_chain(

            context=context,

            job_description=job_description

        )

        # ---------------------------------------------
        # Extract Missing Skills
        # ---------------------------------------------

        missing_skills = []

        recommended_skills = []

        lines = skill_gap.split("\n")

        collect_missing = False
        collect_recommended = False

        for line in lines:

            text = line.strip()

            if "Missing Skills" in text:

                collect_missing = True
                collect_recommended = False
                continue

            if "Recommended Skills" in text:

                collect_missing = False
                collect_recommended = True
                continue

            if collect_missing and text.startswith("-"):

                missing_skills.append(
                    text.replace("-", "").strip()
                )

            if collect_recommended and text.startswith("-"):

                recommended_skills.append(
                    text.replace("-", "").strip()
                )

        # ---------------------------------------------
        # Update State
        # ---------------------------------------------

        state["skill_gap"] = skill_gap

        state["missing_skills"] = missing_skills

        state["recommended_skills"] = recommended_skills

        state["current_agent"] = "Skill Gap Agent"

        state["workflow_status"] = "RUNNING"

        print("Skill Gap Analysis Completed Successfully")

    except Exception as e:

        state["skill_gap"] = ""

        state["missing_skills"] = []

        state["recommended_skills"] = []

        state["errors"].append(str(e))

        print(f"Skill Gap Agent Failed : {e}")

    print("\n=====================================\n")

    return state