from langgraph_agents.state import InterviewAceState


def supervisor_agent(
    state: InterviewAceState
) -> InterviewAceState:
    """
    Supervisor Agent

    Responsible for deciding the next agent
    after Resume Analysis.
    """

    print("\n========== Supervisor Agent ==========")

    score = state.get("match_score", 0)

    print(f"Match Score : {score:.2f}%")

    # -----------------------------------------
    # High Match
    # -----------------------------------------

    if score >= 80:

        state["next_agent"] = "interview_question"

        print("Decision : Strong Resume")

        print("Next Agent : Interview Question Agent")

    # -----------------------------------------
    # Medium Match
    # -----------------------------------------

    elif score >= 60:

        state["next_agent"] = "resume_optimizer"

        print("Decision : Resume needs optimization")

        print("Next Agent : Resume Optimizer Agent")

    # -----------------------------------------
    # Low Match
    # -----------------------------------------

    else:

        state["next_agent"] = "skill_gap"

        print("Decision : Large Skill Gap")

        print("Next Agent : Skill Gap Agent")

    state["current_agent"] = "Supervisor Agent"

    state["workflow_status"] = "RUNNING"

    print("======================================\n")

    return state