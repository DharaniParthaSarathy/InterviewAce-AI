from langgraph_agents.state import InterviewAceState

from utils.langchain.chain import run_question_chain


def interview_question_agent(
    state: InterviewAceState
) -> InterviewAceState:
    """
    Interview Question Agent

    Responsibilities
    ----------------
    1. Read retrieved resume context.
    2. Read uploaded Job Description.
    3. Generate:
        - Technical Questions
        - Project Questions
        - HR Questions
        - Job Description Specific Questions
    4. Update shared LangGraph state.
    """

    print("\n========== Interview Question Agent ==========\n")

    try:

        # -------------------------------------------------
        # Read Shared State
        # -------------------------------------------------

        context = state.get("context", "")

        job_description = state.get("job_description", "")

        # -------------------------------------------------
        # Generate Interview Questions
        # -------------------------------------------------

        questions = run_question_chain(
            context=context,
            job_description=job_description
        )

        # -------------------------------------------------
        # Update LangGraph State
        # -------------------------------------------------

        state["interview_questions"] = questions

        state["current_agent"] = "Interview Question Agent"

        state["workflow_status"] = "RUNNING"

        print("✓ Technical Questions Generated")
        print("✓ Project Questions Generated")
        print("✓ HR Questions Generated")
        print("✓ Job Description Specific Questions Generated")

    except Exception as e:

        state["interview_questions"] = ""

        state["errors"].append(str(e))

        print(f"❌ Interview Question Agent Failed: {e}")

    print("\n==============================================\n")

    return state