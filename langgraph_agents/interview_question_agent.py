from langgraph_agents.state import InterviewAceState

from utils.langchain.chain import run_question_chain


def interview_question_agent(
    state: InterviewAceState
) -> InterviewAceState:

    """
    Interview Question Agent

    Responsibilities
    ----------------
    1. Read the retrieved resume context.
    2. Generate interview questions.
    3. Update the shared LangGraph state.
    """

    print("\n========== Interview Question Agent ==========\n")

    try:

        # ---------------------------------------------
        # Read State
        # ---------------------------------------------

        context = state["context"]

        job_description = state["job_description"]

        # ---------------------------------------------
        # Generate Questions
        # ---------------------------------------------

        questions = run_question_chain(

            context=context,

            job_description=job_description

        )

        # ---------------------------------------------
        # Update State
        # ---------------------------------------------

        state["interview_questions"] = questions

        state["current_agent"] = "Interview Question Agent"

        state["workflow_status"] = "RUNNING"

        print("Interview Questions Generated Successfully")

    except Exception as e:

        state["interview_questions"] = ""

        state["errors"].append(str(e))

        print(f"Interview Question Agent Failed : {e}")

    print("\n==============================================\n")

    return state