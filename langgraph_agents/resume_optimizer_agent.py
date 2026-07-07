from langgraph_agents.state import InterviewAceState

from utils.langchain.chain import run_optimizer_chain


def resume_optimizer_agent(
    state: InterviewAceState
) -> InterviewAceState:

    """
    Resume Optimizer Agent

    Responsibilities
    ----------------
    1. Read retrieved RAG context.
    2. Optimize the resume using LangChain.
    3. Update the shared LangGraph state.
    """

    print("\n========== Resume Optimizer Agent ==========\n")

    try:

        # ---------------------------------------------
        # Read State
        # ---------------------------------------------

        context = state["context"]

        job_description = state["job_description"]

        # ---------------------------------------------
        # Run Resume Optimization
        # ---------------------------------------------

        optimized_resume = run_optimizer_chain(

            context=context,

            job_description=job_description

        )

        # ---------------------------------------------
        # Update State
        # ---------------------------------------------

        state["optimized_resume"] = optimized_resume

        state["current_agent"] = "Resume Optimizer Agent"

        state["workflow_status"] = "RUNNING"

        print("Resume Optimization Completed Successfully")

    except Exception as e:

        state["optimized_resume"] = ""

        state["errors"].append(str(e))

        print(f"Resume Optimization Failed : {e}")

    print("\n===========================================\n")

    return state