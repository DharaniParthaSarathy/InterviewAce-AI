"""
InterviewAce AI Workflow

This module connects

Resume
    ↓
Chunking
    ↓
Embeddings
    ↓
FAISS
    ↓
RAG
    ↓
LangGraph
    ↓
Return Final State
"""

from langgraph_agents.graph import graph

from utils.pdf_loader import extract_text
from utils.chunker import chunk_text
from utils.embedder import get_embeddings
from utils.faiss_store import create_faiss_index
from utils.rag import retrieve_context


def run_interviewace_workflow(

    resume_path,

    job_description,

    candidate_answer=""

):
    """
    Complete InterviewAce AI Pipeline

    Parameters
    ----------
    resume_path : str

    job_description : str

    candidate_answer : str

    Returns
    -------
    final_state : dict
    """

    # =====================================================
    # STEP 1
    # Extract Resume
    # =====================================================

    resume_text = extract_text(
        resume_path
    )

    # =====================================================
    # STEP 2
    # Chunk Resume
    # =====================================================

    chunks = chunk_text(
        resume_text
    )

    # =====================================================
    # STEP 3
    # Generate Embeddings
    # =====================================================

    embeddings = get_embeddings(
        chunks
    )

    # =====================================================
    # STEP 4
    # Create FAISS
    # =====================================================

    faiss_index = create_faiss_index(
        embeddings
    )

    # =====================================================
    # STEP 5
    # Retrieve Context
    # =====================================================

    context = retrieve_context(

        query=job_description,

        index=faiss_index,

        chunks=chunks,

        top_k=3

    )

    # =====================================================
    # STEP 6
    # Create Initial State
    # =====================================================

    initial_state = {

        # ----------------------------
        # Inputs
        # ----------------------------

        "resume_text": resume_text,

        "resume_file": resume_path,

        "job_description": job_description,

        # ----------------------------
        # RAG
        # ----------------------------

        "chunks": chunks,

        "retrieved_chunks": chunks[:3],

        "context": context,

        "faiss_index": faiss_index,

        # ----------------------------
        # Resume Analysis
        # ----------------------------

        "match_score": 0,

        "analysis": "",

        # ----------------------------
        # Resume Optimizer
        # ----------------------------

        "optimized_resume": "",

        "optimized_resume_pdf": "",

        # ----------------------------
        # Skill Gap
        # ----------------------------

        "skill_gap": "",

        "missing_skills": [],

        "recommended_skills": [],

        # ----------------------------
        # Interview Questions
        # ----------------------------

        "interview_questions": "",

        "selected_question": "",

        # ----------------------------
        # Candidate Answers
        # ----------------------------

        "text_answer": candidate_answer,

        "voice_transcript": "",

        # ----------------------------
        # Evaluation
        # ----------------------------

        "evaluation": "",

        "voice_evaluation": "",

        "interview_score": 0,

        # ----------------------------
        # Career Coach
        # ----------------------------

        "career_advice": "",

        "learning_roadmap": "",

        # ----------------------------
        # Report
        # ----------------------------

        "report_path": "",

        # ----------------------------
        # Workflow
        # ----------------------------

        "workflow_status": "Started",

        # ----------------------------
        # Errors
        # ----------------------------

        "errors": []

    }

    # =====================================================
    # STEP 7
    # Run LangGraph
    # =====================================================

    final_state = graph.invoke(
        initial_state
    )

    # =====================================================
    # STEP 8
    # Return
    # =====================================================

    return final_state