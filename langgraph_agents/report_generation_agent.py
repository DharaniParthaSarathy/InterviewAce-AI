from langgraph_agents.state import InterviewAceState

from utils.pdf_report import generate_pdf_report


def report_generation_agent(
    state: InterviewAceState
) -> InterviewAceState:

    """
    Report Generation Agent

    Responsibilities
    ----------------
    1. Collect outputs from all previous agents.
    2. Generate the InterviewAce AI PDF Report.
    3. Save the report path into the shared state.
    """

    print("\n========== Report Generation Agent ==========\n")

    try:

        # -------------------------------------------------
        # Read State
        # -------------------------------------------------

        score = state["match_score"]

        analysis = state["analysis"]

        optimized_resume = state["optimized_resume"]

        questions = state["interview_questions"]

        evaluation = state["evaluation"]

        career_advice = state["career_advice"]

        skill_gap = state["skill_gap"]

        # -------------------------------------------------
        # Generate Report
        # -------------------------------------------------

        report_path = generate_pdf_report(

            score=score,

            analysis=analysis,

            optimized_resume=optimized_resume,

            questions=questions,

            evaluation=evaluation,

            career_advice=career_advice,

            skill_gap=skill_gap

        )

        # -------------------------------------------------
        # Update State
        # -------------------------------------------------

        state["report_path"] = report_path

        state["current_agent"] = "Report Generation Agent"

        state["workflow_status"] = "COMPLETED"

        print("InterviewAce Report Generated Successfully")

    except Exception as e:

        state["report_path"] = ""

        state["errors"].append(str(e))

        print(f"Report Generation Failed : {e}")

    print("\n=============================================\n")

    return state