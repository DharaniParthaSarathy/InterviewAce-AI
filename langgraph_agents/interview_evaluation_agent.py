from langgraph_agents.state import InterviewAceState

from utils.langchain.chain import run_evaluation_chain


def interview_evaluation_agent(
    state: InterviewAceState
) -> InterviewAceState:

    """
    Interview Evaluation Agent

    Responsibilities
    ----------------
    1. Evaluate candidate's answer.
    2. Support both text and voice answers.
    3. Store evaluation in shared state.
    """

    print("\n========== Interview Evaluation Agent ==========\n")

    try:

        # -------------------------------------------------
        # Read State
        # -------------------------------------------------

        question = state["selected_question"]

        text_answer = state["text_answer"]

        voice_answer = state["voice_transcript"]

        # -------------------------------------------------
        # Prefer Voice Answer if Available
        # -------------------------------------------------

        if voice_answer.strip():

            answer = voice_answer

            print("Using Voice Transcript")

        else:

            answer = text_answer

            print("Using Text Answer")

        # -------------------------------------------------
        # Evaluate Answer
        # -------------------------------------------------

        evaluation = run_evaluation_chain(

            question=question,

            answer=answer

        )

        # -------------------------------------------------
        # Update State
        # -------------------------------------------------

        state["evaluation"] = evaluation

        state["voice_evaluation"] = evaluation

        state["current_agent"] = "Interview Evaluation Agent"

        state["workflow_status"] = "RUNNING"

        print("Interview Evaluation Completed Successfully")

    except Exception as e:

        state["evaluation"] = ""

        state["voice_evaluation"] = ""

        state["errors"].append(str(e))

        print(f"Interview Evaluation Failed : {e}")

    print("\n===============================================\n")

    return state