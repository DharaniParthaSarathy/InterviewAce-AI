from typing import TypedDict
from typing import Optional
from typing import Any


class InterviewAceState(TypedDict):
    """
    Shared State for the complete InterviewAce AI
    LangGraph Multi-Agent Workflow.
    """

    # =====================================================
    # User Inputs
    # =====================================================

    resume_text: str
    job_description: str
    resume_file: str

    # =====================================================
    # RAG Components
    # =====================================================

    chunks: list[str]
    retrieved_chunks: list[str]
    context: str
    faiss_index: Any

    # =====================================================
    # Resume Analysis
    # =====================================================

    match_score: Optional[float]
    analysis: str

    # =====================================================
    # Resume Optimization
    # =====================================================

    optimized_resume: str
    optimized_resume_pdf: str

    # =====================================================
    # Skill Gap
    # =====================================================

    skill_gap: str
    missing_skills: list[str]
    recommended_skills: list[str]

    # =====================================================
    # Interview Questions
    # =====================================================

    interview_questions: str
    selected_question: str

    # =====================================================
    # Candidate Answers
    # =====================================================

    text_answer: str
    voice_transcript: str

    # =====================================================
    # Interview Evaluation
    # =====================================================

    evaluation: str
    voice_evaluation: str
    interview_score: Optional[float]

    # =====================================================
    # Career Coach
    # =====================================================

    career_advice: str
    learning_roadmap: str

    # =====================================================
    # Report
    # =====================================================

    report_path: str

    # =====================================================
    # Workflow Control
    # =====================================================

    current_agent: str
    next_agent: str
    workflow_status: str

    # =====================================================
    # Error Handling
    # =====================================================

    errors: list[str]