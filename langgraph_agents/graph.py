from langgraph.graph import StateGraph, END

from langgraph_agents.state import InterviewAceState

from langgraph_agents.resume_analysis_agent import resume_analysis_agent
from langgraph_agents.resume_optimizer_agent import resume_optimizer_agent
from langgraph_agents.skill_gap_agent import skill_gap_agent
from langgraph_agents.interview_question_agent import interview_question_agent
from langgraph_agents.interview_evaluation_agent import interview_evaluation_agent
from langgraph_agents.career_coach_agent import career_coach_agent
from langgraph_agents.report_generation_agent import report_generation_agent

# ==========================================================
# Create Workflow
# ==========================================================

workflow = StateGraph(InterviewAceState)

# ==========================================================
# Add Nodes
# ==========================================================

workflow.add_node(
    "ResumeAnalysis",
    resume_analysis_agent
)

workflow.add_node(
    "ResumeOptimizer",
    resume_optimizer_agent
)

workflow.add_node(
    "SkillGap",
    skill_gap_agent
)

workflow.add_node(
    "CareerCoach",
    career_coach_agent
)

workflow.add_node(
    "InterviewQuestion",
    interview_question_agent
)

workflow.add_node(
    "InterviewEvaluation",
    interview_evaluation_agent
)

workflow.add_node(
    "ReportGeneration",
    report_generation_agent
)

# ==========================================================
# Entry Point
# ==========================================================

workflow.set_entry_point(
    "ResumeAnalysis"
)

# ==========================================================
# Sequential Workflow
# ==========================================================

workflow.add_edge(
    "ResumeAnalysis",
    "ResumeOptimizer"
)

workflow.add_edge(
    "ResumeOptimizer",
    "SkillGap"
)

workflow.add_edge(
    "SkillGap",
    "CareerCoach"
)

workflow.add_edge(
    "CareerCoach",
    "InterviewQuestion"
)

workflow.add_edge(
    "InterviewQuestion",
    "InterviewEvaluation"
)

workflow.add_edge(
    "InterviewEvaluation",
    "ReportGeneration"
)

workflow.add_edge(
    "ReportGeneration",
    END
)

# ==========================================================
# Compile Graph
# ==========================================================

graph = workflow.compile()