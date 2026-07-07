from langgraph_agents.state import InterviewAceState

from utils.langchain.chain import run_career_coach_chain


def career_coach_agent(
    state: InterviewAceState
) -> InterviewAceState:

    """
    Career Coach Agent

    Responsibilities
    ----------------
    1. Analyze the candidate's profile.
    2. Provide personalized career guidance.
    3. Suggest a learning roadmap.
    4. Update the shared LangGraph state.
    """

    print("\n========== Career Coach Agent ==========\n")

    try:

        # -------------------------------------------------
        # Read State
        # -------------------------------------------------

        context = state["context"]

        job_description = state["job_description"]

        # -------------------------------------------------
        # Generate Career Advice
        # -------------------------------------------------

        career_advice = run_career_coach_chain(

            context=context,

            job_description=job_description

        )

        # -------------------------------------------------
        # Extract Learning Roadmap
        # -------------------------------------------------

        learning_roadmap = ""

        lines = career_advice.split("\n")

        capture = False

        for line in lines:

            if "Learning Roadmap" in line:

                capture = True
                continue

            if "Interview Preparation Tips" in line:

                break

            if capture:

                learning_roadmap += line + "\n"

        # -------------------------------------------------
        # Update State
        # -------------------------------------------------

        state["career_advice"] = career_advice

        state["learning_roadmap"] = learning_roadmap.strip()

        state["current_agent"] = "Career Coach Agent"

        state["workflow_status"] = "RUNNING"

        print("Career Guidance Generated Successfully")

    except Exception as e:

        state["career_advice"] = ""

        state["learning_roadmap"] = ""

        state["errors"].append(str(e))

        print(f"Career Coach Agent Failed : {e}")

    print("\n========================================\n")

    return state