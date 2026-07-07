import re

from langgraph_agents.state import InterviewAceState

from utils.rag import retrieve_context

from utils.langchain.chain import (
    run_analysis_chain
)


def resume_analysis_agent(
    state: InterviewAceState
) -> InterviewAceState:

    print("\n========== Resume Analysis Agent ==========\n")

    # ---------------------------------------------
    # Read Inputs
    # ---------------------------------------------

    resume_text = state["resume_text"]

    job_description = state["job_description"]

    faiss_index = state["faiss_index"]

    chunks = state["chunks"]

    # ---------------------------------------------
    # Retrieve Resume Context using RAG
    # ---------------------------------------------

    context = retrieve_context(

        query=job_description,

        index=faiss_index,

        chunks=chunks,

        top_k=5

    )

    state["context"] = context

    state["retrieved_chunks"] = context.split("\n\n")

    # ---------------------------------------------
    # Run LangChain Analysis
    # ---------------------------------------------

    analysis = run_analysis_chain(

        context=context,

        job_description=job_description

    )

    state["analysis"] = analysis

    # ---------------------------------------------
    # Extract Match Score
    # ---------------------------------------------

    score = 0.0

    try:

        match = re.search(

            r'(\d+(\.\d+)?)\s*%',

            analysis

        )

        if match:

            score = float(

                match.group(1)

            )

    except Exception:

        score = 0.0

    state["match_score"] = score

    # ---------------------------------------------
    # Workflow Info
    # ---------------------------------------------

    state["current_agent"] = "Resume Analysis Agent"

    print(f"Match Score : {score:.2f}%")

    print("\n========== Resume Analysis Completed ==========\n")

    return state