"""
==========================================================
InterviewAce AI
AI-Powered Resume Analysis & Interview Preparation Assistant

Tech Stack
----------
• Streamlit
• LangGraph
• LangChain
• Gemini 2.5 Flash
• FAISS
• Sentence Transformers
• RAG

Workflow

Upload Resume
      ↓
Analyze Resume
      ↓
Resume Analysis
ATS Resume
Skill Gap
Career Coach
Interview Questions
      ↓
Candidate Answer / Voice Answer
      ↓
Interview Evaluation
      ↓
PDF Report
==========================================================
"""

import os
import tempfile

import streamlit as st

from streamlit_mic_recorder import mic_recorder

from workflow import run_interviewace_workflow

from utils.pdf_report import generate_resume_pdf

# ==========================================================
# Streamlit Configuration
# ==========================================================

st.set_page_config(

    page_title="InterviewAce AI",

    page_icon="🎯",

    layout="wide",

    initial_sidebar_state="expanded"

)

# ==========================================================
# Session State
# ==========================================================

if "final_state" not in st.session_state:
    st.session_state.final_state = None

if "analysis_completed" not in st.session_state:
    st.session_state.analysis_completed = False

if "resume_path" not in st.session_state:
    st.session_state.resume_path = ""

if "candidate_answer" not in st.session_state:
    st.session_state.candidate_answer = ""

if "voice_transcript" not in st.session_state:
    st.session_state.voice_transcript = ""

# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.title("🎯 InterviewAce AI")

    st.markdown(
        """
AI-Powered Interview Preparation

### Features

✅ Resume Analysis

✅ ATS Resume Optimization

✅ Skill Gap Analysis

✅ Career Coach

✅ Interview Questions

✅ Voice Interview

✅ AI Evaluation

✅ PDF Report
"""
    )

    st.markdown("---")

    st.info(
        "Upload your resume, paste the Job Description and click **Analyze Resume**."
    )

# ==========================================================
# Main Title
# ==========================================================

st.title("🎯 InterviewAce AI")

st.caption(
    "AI Resume Analysis • ATS Optimization • Skill Gap Analysis • Career Coach • Interview Preparation"
)

st.markdown("---")

# ==========================================================
# Resume Upload
# ==========================================================

st.header("📄 Resume Upload")

uploaded_resume = st.file_uploader(

    "Upload Resume (PDF)",

    type=["pdf"]

)

# ==========================================================
# Job Description
# ==========================================================

st.header("💼 Job Description")

job_description = st.text_area(

    "Paste the complete Job Description",

    height=280,

    placeholder="Paste the complete Job Description here..."

)

st.markdown("---")

# ==========================================================
# Analyze Resume
# ==========================================================

analyze_clicked = st.button(

    "🚀 Analyze Resume",

    use_container_width=True

)

# ==========================================================
# Run InterviewAce Workflow
# ==========================================================

if analyze_clicked:

    # ------------------------------------------------------
    # Validate Inputs
    # ------------------------------------------------------

    if uploaded_resume is None:

        st.warning("⚠ Please upload your resume.")

        st.stop()

    if not job_description.strip():

        st.warning("⚠ Please paste the Job Description.")

        st.stop()

    # ------------------------------------------------------
    # Save Uploaded Resume
    # ------------------------------------------------------

    with tempfile.NamedTemporaryFile(

        delete=False,

        suffix=".pdf"

    ) as tmp_file:

        tmp_file.write(uploaded_resume.read())

        resume_path = tmp_file.name

    st.session_state.resume_path = resume_path

    # ------------------------------------------------------
    # Run Complete Workflow
    # ------------------------------------------------------

    with st.spinner(

        "🤖 InterviewAce AI is analyzing your resume..."

    ):

        try:

            final_state = run_interviewace_workflow(

                resume_path=resume_path,

                job_description=job_description,

                candidate_answer=""

            )

            st.session_state.final_state = final_state

            st.session_state.analysis_completed = True

            st.success(

                "✅ Resume Analysis Completed Successfully!"

            )

        except Exception as e:

            st.error(

                f"❌ Workflow Failed\n\n{e}"

            )

            st.stop()


# ==========================================================
# Wait Until Workflow Completes
# ==========================================================

if not st.session_state.analysis_completed:

    st.info(

        "👆 Upload your Resume, paste the Job Description and click **Analyze Resume**."

    )

    st.stop()


# ==========================================================
# Retrieve Final Workflow State
# ==========================================================

state = st.session_state.final_state

st.markdown("---")


# ==========================================================
# Create Professional Tabs
# ==========================================================

tab1, tab2, tab3, tab4, tab5 = st.tabs(

    [

        "📊 Analysis",

        "✨ ATS Resume",

        "📈 Skills & Career",

        "🎯 Interview",

        "📄 Reports"

    ]

)

# ==========================================================
# 📊 TAB 1 : Resume Analysis
# ==========================================================

with tab1:

    st.header("📊 Resume Analysis")

    # ------------------------------------------------------
    # Resume Preview
    # ------------------------------------------------------

    with st.expander(

        "📄 View Extracted Resume",

        expanded=False

    ):

        st.text(

            state["resume_text"]

        )

    st.markdown("---")

    # ------------------------------------------------------
    # ATS Match Score
    # ------------------------------------------------------

    match_score = float(

        state.get(

            "match_score",

            0

        )

    )

    col1, col2 = st.columns(

        [1, 3]

    )

    with col1:

        st.metric(

            "ATS Match Score",

            f"{match_score:.2f}%"

        )

    with col2:

        if match_score >= 85:

            st.success(

                "Excellent Resume Match ✅"

            )

        elif match_score >= 70:

            st.info(

                "Good Resume Match 👍"

            )

        elif match_score >= 50:

            st.warning(

                "Average Resume Match ⚠"

            )

        else:

            st.error(

                "Low Resume Match ❌"

            )

    st.progress(

        min(

            match_score / 100,

            1.0

        )

    )

    st.markdown("---")

    # ------------------------------------------------------
    # Resume Analysis
    # ------------------------------------------------------

    st.subheader(

        "🤖 AI Resume Analysis"

    )

    analysis = state.get(

        "analysis",

        ""

    )

    if analysis:

        st.markdown(

            analysis

        )

    else:

        st.warning(

            "Resume analysis not available."

        )

    st.markdown("---")

    # ------------------------------------------------------
    # Quick Summary
    # ------------------------------------------------------

    st.subheader(

        "📌 Summary"

    )

    if match_score >= 85:

        st.success(

            "Your resume is highly aligned with the Job Description."

        )

    elif match_score >= 70:

        st.info(

            "Your resume is a good match. Minor improvements are recommended."

        )

    elif match_score >= 50:

        st.warning(

            "Your resume needs optimization before applying."

        )

    else:

        st.error(

            "Consider improving your resume significantly for this role."

        )

# ==========================================================
# ✨ TAB 2 : ATS Optimized Resume
# ==========================================================

with tab2:

    st.header("✨ ATS Optimized Resume")

    optimized_resume = state.get(

        "optimized_resume",

        ""

    )

    # ------------------------------------------------------
    # Optimized Resume Preview
    # ------------------------------------------------------

    if optimized_resume:

        with st.expander(

            "📄 View Optimized Resume",

            expanded=True

        ):

            st.markdown(

                optimized_resume

            )

    else:

        st.warning(

            "Optimized resume not available."

        )

    st.markdown("---")

    # ------------------------------------------------------
    # Download Optimized Resume
    # ------------------------------------------------------

    if optimized_resume:

        resume_pdf = generate_resume_pdf(

            optimized_resume

        )

        with open(

            resume_pdf,

            "rb"

        ) as pdf:

            st.download_button(

                label="📥 Download Optimized Resume",

                data=pdf,

                file_name="Optimized_Resume.pdf",

                mime="application/pdf",

                use_container_width=True

            )

    st.markdown("---")

    # ------------------------------------------------------
    # ATS Resume Tips
    # ------------------------------------------------------

    st.subheader("💡 ATS Optimization Tips")

    tips = [

        "✅ Include keywords from the Job Description.",

        "✅ Highlight measurable achievements.",

        "✅ Use standard section headings (Skills, Projects, Experience).",

        "✅ Keep formatting ATS-friendly (avoid tables and excessive graphics).",

        "✅ Quantify project outcomes whenever possible.",

        "✅ Keep technical skills updated and relevant.",

        "✅ Tailor your resume for each application."

    ]

    for tip in tips:

        st.write(tip)

    st.markdown("---")

    # ------------------------------------------------------
    # Resume Improvement Status
    # ------------------------------------------------------

    st.subheader("📈 Resume Improvement Status")

    match_score = float(

        state.get(

            "match_score",

            0

        )

    )

    if match_score >= 85:

        st.success(

            "🎉 Your resume is well optimized for ATS."

        )

    elif match_score >= 70:

        st.info(

            "👍 Your resume is good. A few improvements can increase your ATS score."

        )

    elif match_score >= 50:

        st.warning(

            "⚠ Resume needs moderate optimization."

        )

    else:

        st.error(

            "❌ Resume requires significant improvement before applying."

        )

# ==========================================================
# 📈 TAB 3 : Skills & Career
# ==========================================================

with tab3:

    st.header("📈 Skills & Career")

    # ======================================================
    # ATS Skill Gap Analysis
    # ======================================================

    st.subheader("📊 ATS Skill Gap Analysis")

    skill_gap = state.get(

        "skill_gap",

        ""

    )

    if skill_gap:

        st.markdown(

            skill_gap

        )

    else:

        st.info(

            "Skill Gap Analysis not available."

        )

    st.markdown("---")

    # ======================================================
    # Missing & Recommended Skills
    # ======================================================

    st.subheader("🛠 Skills Overview")

    missing_skills = state.get(

        "missing_skills",

        []

    )

    recommended_skills = state.get(

        "recommended_skills",

        []

    )

    col1, col2 = st.columns(2)

    # ------------------------------------------------------
    # Missing Skills
    # ------------------------------------------------------

    with col1:

        st.markdown("### ❌ Missing Skills")

        if missing_skills:

            for skill in missing_skills:

                st.write(f"• {skill}")

        else:

            st.success(

                "No missing skills detected."

            )

    # ------------------------------------------------------
    # Recommended Skills
    # ------------------------------------------------------

    with col2:

        st.markdown("### ✅ Recommended Skills")

        if recommended_skills:

            for skill in recommended_skills:

                st.write(f"• {skill}")

        else:

            st.info(

                "No additional recommendations."

            )

    st.markdown("---")

    # ======================================================
    # Learning Roadmap
    # ======================================================

    st.subheader("📚 Personalized Learning Roadmap")

    roadmap = state.get(

        "learning_roadmap",

        ""

    )

    if roadmap:

        st.markdown(

            roadmap

        )

    else:

        st.info(

            "Learning roadmap not generated."

        )

    st.markdown("---")

    # ======================================================
    # Career Coach
    # ======================================================

    st.subheader("👨‍💼 AI Career Coach")

    career_advice = state.get(

        "career_advice",

        ""

    )

    if career_advice:

        st.markdown(

            career_advice

        )

    else:

        st.info(

            "Career advice not available."

        )

    st.markdown("---")

    # ======================================================
    # Career Readiness Meter
    # ======================================================

    st.subheader("🎯 Career Readiness")

    match_score = float(

        state.get(

            "match_score",

            0

        )

    )

    if match_score >= 85:

        st.success(

            "🎉 You are highly prepared to apply for this role."

        )

    elif match_score >= 70:

        st.info(

            "👍 You're close! A few improvements will strengthen your profile."

        )

    elif match_score >= 50:

        st.warning(

            "⚠ Improve your resume and skills before applying."

        )

    else:

        st.error(

            "❌ Significant improvements are recommended before applying."

        )

# ==========================================================
# 🎯 TAB 4 : Interview Preparation
# ==========================================================

with tab4:

    st.header("🎯 AI Interview Preparation")

    # ======================================================
    # Interview Questions
    # ======================================================

    st.subheader("📝 AI Generated Interview Questions")

    questions = state.get(

        "interview_questions",

        ""

    )

    if questions:

        st.markdown(

            questions

        )

    else:

        st.warning(

            "Interview questions not generated."

        )

    st.markdown("---")

    # ======================================================
    # Candidate Answer
    # ======================================================

    st.subheader("✍ Type Your Answer")

    candidate_answer = st.text_area(

        "Answer one of the above interview questions.",

        height=220,

        key="candidate_answer"

    )

    st.markdown("---")

    # ======================================================
    # Voice Recording
    # ======================================================

    st.subheader("🎤 Voice Mock Interview")

    st.info(

        "Instead of typing, you may answer using your microphone."

    )

    audio = mic_recorder(

        start_prompt="🎤 Start Recording",

        stop_prompt="⏹ Stop Recording",

        just_once=False,

        use_container_width=True,

        key="voice_recorder"

    )

    # ======================================================
    # Speech to Text
    # ======================================================

    if audio:

        from utils.voice_interview import speech_to_text

        with tempfile.NamedTemporaryFile(

            delete=False,

            suffix=".wav"

        ) as temp_audio:

            temp_audio.write(

                audio["bytes"]

            )

            audio_path = temp_audio.name

        with st.spinner(

            "Converting speech to text..."

        ):

            transcript = speech_to_text(

                audio_path

            )

        st.session_state.voice_transcript = transcript

        st.success(

            "Voice converted successfully."

        )

    # ======================================================
    # Transcript
    # ======================================================

    if st.session_state.voice_transcript:

        st.subheader("📝 Voice Transcript")

        st.text_area(

            "",

            value=st.session_state.voice_transcript,

            height=180,

            disabled=True

        )

    st.markdown("---")

    # ======================================================
    # Evaluate Button
    # ======================================================

    if st.button(

        "🚀 Evaluate My Answer",

        use_container_width=True

    ):

        # ---------------------------------------------
        # Voice Answer gets higher priority
        # ---------------------------------------------

        if st.session_state.voice_transcript:

            state["text_answer"] = (

                st.session_state.voice_transcript

            )

        else:

            state["text_answer"] = (

                candidate_answer

            )

        # ---------------------------------------------
        # Validation
        # ---------------------------------------------

        if state["text_answer"].strip() == "":

            st.warning(

                "Please type an answer or record your voice."

            )

            st.stop()

        # ---------------------------------------------
        # Run Evaluation Agent
        # ---------------------------------------------

        from langgraph_agents.interview_evaluation_agent import (

            interview_evaluation_agent

        )

        with st.spinner(

            "Evaluating your interview answer..."

        ):

            state = interview_evaluation_agent(

                state

            )

        st.session_state.final_state = state

        st.success(

            "Interview evaluation completed."

        )

    st.markdown("---")

    # ======================================================
    # Interview Evaluation
    # ======================================================

    st.subheader("📋 AI Interview Feedback")

    evaluation = state.get(

        "evaluation",

        ""

    )

    if evaluation:

        st.markdown(

            evaluation

        )

    else:

        st.info(

            "Answer evaluation will appear here."

        )

    st.markdown("---")

    # ======================================================
    # Interview Score
    # ======================================================

    st.subheader("🏆 Interview Score")

    interview_score = float(

        state.get(

            "interview_score",

            0

        )

    )

    col1, col2 = st.columns(

        [1, 3]

    )

    with col1:

        st.metric(

            "Score",

            f"{interview_score:.0f}/100"

        )

    with col2:

        if interview_score >= 85:

            st.success(

                "Excellent Interview Performance 🌟"

            )

        elif interview_score >= 70:

            st.info(

                "Good Performance 👍"

            )

        elif interview_score >= 50:

            st.warning(

                "Average Performance ⚠"

            )

        else:

            st.error(

                "Needs Improvement ❌"

            )

    st.progress(

        min(

            interview_score / 100,

            1.0

        )

    )

# ==========================================================
# 📄 TAB 5 : Reports
# ==========================================================

with tab5:

    st.header("📄 Reports & Downloads")

    # ======================================================
    # Download Complete Report
    # ======================================================

    report_path = state.get(

        "report_path",

        ""

    )

    if report_path and os.path.exists(report_path):

        with open(

            report_path,

            "rb"

        ) as pdf:

            st.download_button(

                label="📥 Download Complete InterviewAce Report",

                data=pdf,

                file_name="InterviewAce_Report.pdf",

                mime="application/pdf",

                use_container_width=True

            )

    else:

        st.info(

            "Report not available."

        )

    st.markdown("---")

    # ======================================================
    # Download Optimized Resume
    # ======================================================

    optimized_resume = state.get(

        "optimized_resume",

        ""

    )

    if optimized_resume:

        optimized_resume_pdf = generate_resume_pdf(

            optimized_resume

        )

        with open(

            optimized_resume_pdf,

            "rb"

        ) as pdf:

            st.download_button(

                label="📄 Download Optimized Resume",

                data=pdf,

                file_name="Optimized_Resume.pdf",

                mime="application/pdf",

                use_container_width=True

            )

    st.markdown("---")

    # ======================================================
    # Workflow Summary
    # ======================================================

    st.subheader("⚙ Workflow Summary")

    workflow_steps = [

        "✅ Resume Uploaded",

        "✅ Resume Parsed",

        "✅ Resume Chunked",

        "✅ Embeddings Generated",

        "✅ FAISS Index Created",

        "✅ RAG Context Retrieved",

        "✅ Resume Analysis Completed",

        "✅ Resume Optimization Completed",

        "✅ Skill Gap Analysis Completed",

        "✅ Career Coach Completed",

        "✅ Interview Questions Generated",

        "✅ Interview Evaluation Completed",

        "✅ PDF Report Generated"

    ]

    for step in workflow_steps:

        st.write(step)

    st.markdown("---")

    # ======================================================
    # Errors
    # ======================================================

    errors = state.get(

        "errors",

        []

    )

    if errors:

        st.subheader("⚠ Workflow Errors")

        for err in errors:

            st.error(err)

    else:

        st.success(

            "Workflow completed successfully with no errors."

        )

    st.markdown("---")

    # ======================================================
    # Project Information
    # ======================================================

    st.subheader("ℹ About InterviewAce AI")

    st.markdown(

        """
**InterviewAce AI** is an AI-powered interview preparation platform that combines:

- 🤖 LangGraph Multi-Agent Workflow
- 🧠 LangChain + Gemini
- 📚 Retrieval-Augmented Generation (RAG)
- 🔍 FAISS Vector Database
- 📄 ATS Resume Optimization
- 📈 Skill Gap Analysis
- 👨‍💼 AI Career Coaching
- 🎯 Interview Question Generation
- 🎙 Voice & Text Answer Evaluation
- 📑 Automated PDF Report Generation

Designed to help candidates improve resumes, prepare for interviews, and receive AI-driven feedback.
"""
    )

    st.markdown("---")

    st.success("🎉 InterviewAce AI Analysis Completed Successfully!")