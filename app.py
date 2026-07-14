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
--------
Resume Upload
      ↓
Resume Analysis
      ↓
ATS Resume
      ↓
Skill Gap Analysis
      ↓
Career Coach
      ↓
Interview Preparation
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

# -------- New States --------

if "jd_analysis" not in st.session_state:
    st.session_state.jd_analysis = ""

if "jd_questions" not in st.session_state:
    st.session_state.jd_questions = ""

# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.title("🎯 InterviewAce AI")

    st.markdown(
        """
### 🚀 AI Interview Preparation Platform

#### Features

✅ Resume Analysis

✅ ATS Resume Optimization

✅ Skill Gap Analysis

✅ Career Coach

✅ Interview Preparation

✅ Job Description Analysis

✅ JD Specific Questions

✅ Voice Mock Interview

✅ AI Answer Evaluation

✅ PDF Report Generation
"""
    )

    st.markdown("---")

    st.info(
        """
Upload your Resume

Paste the Job Description

Click **Analyze Resume**

InterviewAce AI will generate:

• Resume Analysis

• ATS Resume

• Skill Gap

• Career Advice

• Technical Questions

• Project Questions

• Behavioural Questions

• HR Questions

• Job Description Analysis

• Job Description Specific Questions

• AI Evaluation
"""
    )

# ==========================================================
# Main Title
# ==========================================================

st.title("🎯 InterviewAce AI")

st.caption(
    "Multi-Agent LLM & RAG-Based Intelligent Interview Preparation Platform"
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
    height=260,
    placeholder="""
Paste the complete Job Description here...

Example:

Python
Machine Learning
LangChain
Docker
FastAPI
AWS
SQL
Communication Skills
Problem Solving
"""
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
# Run Complete Workflow
# ==========================================================

if analyze_clicked:

    # ------------------------------------------------------
    # Validate Inputs
    # ------------------------------------------------------

    if uploaded_resume is None:

        st.warning("⚠ Please upload your Resume.")

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
    # Run LangGraph Workflow
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
# Retrieve Final State
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

    st.header("📊 AI Resume Analysis")

    # ------------------------------------------------------
    # Resume Preview
    # ------------------------------------------------------

    with st.expander(
        "📄 View Extracted Resume",
        expanded=False
    ):

        st.text(
            state.get(
                "resume_text",
                "Resume text not available."
            )
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

    col1, col2 = st.columns([1, 3])

    with col1:

        st.metric(
            "ATS Match Score",
            f"{match_score:.1f}%"
        )

    with col2:

        if match_score >= 90:

            st.success(
                "🌟 Outstanding Match! Your resume is highly aligned with the Job Description."
            )

        elif match_score >= 75:

            st.info(
                "👍 Good Match! Minor improvements can further strengthen your resume."
            )

        elif match_score >= 60:

            st.warning(
                "⚠ Moderate Match. Consider improving your resume before applying."
            )

        else:

            st.error(
                "❌ Low Match. Significant improvements are recommended."
            )

    st.progress(
        min(match_score / 100, 1.0)
    )

    st.markdown("---")

    # ------------------------------------------------------
    # AI Resume Analysis
    # ------------------------------------------------------

    st.subheader("🤖 AI Resume Analysis")

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
            "Resume Analysis is not available."
        )

    st.markdown("---")

    # ------------------------------------------------------
    # Resume Readiness
    # ------------------------------------------------------

    st.subheader("📌 Resume Readiness")

    if match_score >= 90:

        st.success(
            """
Your resume is highly optimized for this role.

✔ Strong ATS compatibility

✔ Excellent skill alignment

✔ Ready for submission
"""
        )

    elif match_score >= 75:

        st.info(
            """
Your resume is competitive.

Recommended improvements:

• Add more JD keywords

• Quantify achievements

• Improve project descriptions
"""
        )

    elif match_score >= 60:

        st.warning(
            """
Your resume needs improvement.

Focus on:

• Missing technical skills

• Better ATS keywords

• Stronger project descriptions
"""
        )

    else:

        st.error(
            """
Your resume requires significant improvements.

Recommended:

• Update technical skills

• Improve ATS optimization

• Add relevant projects

• Tailor the resume to the Job Description
"""
        )

    st.markdown("---")

    # ------------------------------------------------------
    # Resume Statistics
    # ------------------------------------------------------

    st.subheader("📈 Resume Overview")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Resume Status",
            "Analyzed"
        )

    with col2:

        st.metric(
            "Job Match",
            f"{match_score:.0f}%"
        )

    with col3:

        if match_score >= 75:

            st.metric(
                "Recommendation",
                "Apply ✅"
            )

        else:

            st.metric(
                "Recommendation",
                "Improve ⚠"
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
    # ATS Optimized Resume
    # ------------------------------------------------------

    if optimized_resume:

        with st.expander(
            "📄 View ATS Optimized Resume",
            expanded=True
        ):

            st.markdown(
                optimized_resume
            )

    else:

        st.warning(
            "ATS Optimized Resume not available."
        )

    st.markdown("---")

    # ------------------------------------------------------
    # Download ATS Resume
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

                label="📥 Download ATS Optimized Resume",

                data=pdf,

                file_name="ATS_Optimized_Resume.pdf",

                mime="application/pdf",

                use_container_width=True

            )

    st.markdown("---")

    # ------------------------------------------------------
    # ATS Resume Checklist
    # ------------------------------------------------------

    st.subheader("✅ ATS Resume Checklist")

    checklist = [

        "✔ Professional Summary aligned with the Job Description",

        "✔ Relevant technical keywords included",

        "✔ Skills section optimized",

        "✔ Projects highlight measurable impact",

        "✔ Resume follows ATS-friendly formatting",

        "✔ No tables, graphics or complex layouts",

        "✔ Experience written using action verbs",

        "✔ Important technologies emphasized",

        "✔ Resume customized for this specific role"

    ]

    for item in checklist:

        st.write(item)

    st.markdown("---")

    # ------------------------------------------------------
    # ATS Resume Tips
    # ------------------------------------------------------

    st.subheader("💡 AI Suggestions")

    st.info(

        """
### Improve your ATS Score by:

• Matching keywords from the Job Description

• Quantifying achievements with numbers

• Using action verbs

• Highlighting relevant projects

• Mentioning tools and frameworks required for the role

• Keeping formatting simple and ATS-friendly

• Tailoring every application instead of using one generic resume
        """

    )

    st.markdown("---")

    # ------------------------------------------------------
    # ATS Readiness Meter
    # ------------------------------------------------------

    st.subheader("📈 ATS Resume Readiness")

    match_score = float(
        state.get(
            "match_score",
            0
        )
    )

    st.progress(
        min(match_score / 100, 1.0)
    )

    if match_score >= 90:

        st.success(
            "🌟 Excellent! Your resume is highly optimized for Applicant Tracking Systems."
        )

    elif match_score >= 75:

        st.info(
            "👍 Good ATS compatibility. Minor improvements can increase your chances."
        )

    elif match_score >= 60:

        st.warning(
            "⚠ Moderate ATS compatibility. Resume optimization is recommended."
        )

    else:

        st.error(
            "❌ Low ATS compatibility. Consider updating your resume before applying."
        )

    st.markdown("---")

    # ------------------------------------------------------
    # ATS Resume Summary
    # ------------------------------------------------------

    st.subheader("📌 ATS Summary")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Resume",
            "Optimized"
        )

    with col2:

        st.metric(
            "ATS Score",
            f"{match_score:.0f}%"
        )

    with col3:

        if match_score >= 75:

            st.metric(
                "Status",
                "Ready ✅"
            )

        else:

            st.metric(
                "Status",
                "Improve ⚠"
            )

# ==========================================================
# 📈 TAB 3 : Skills & Career
# ==========================================================

with tab3:

    st.header("📈 Skills & Career")

    # ======================================================
    # Skill Gap Analysis
    # ======================================================

    st.subheader("📊 AI Skill Gap Analysis")

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
    # Missing Skills & Recommended Skills
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

                st.error(f"• {skill}")

        else:

            st.success(
                "No major missing skills detected."
            )

    # ------------------------------------------------------
    # Recommended Skills
    # ------------------------------------------------------

    with col2:

        st.markdown("### ✅ Recommended Skills")

        if recommended_skills:

            for skill in recommended_skills:

                st.success(f"• {skill}")

        else:

            st.info(
                "No additional recommendations available."
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
    # AI Career Coach
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
    # Certifications Recommendation
    # ======================================================

    st.subheader("🎓 Suggested Certifications")

    certifications = [

        "Google Professional Machine Learning Engineer",

        "Microsoft Azure AI Engineer Associate",

        "AWS Certified Machine Learning",

        "DeepLearning.AI Generative AI Specialization",

        "TensorFlow Developer Certificate",

        "LangChain for LLM Application Development"

    ]

    for cert in certifications:

        st.write(f"• {cert}")

    st.markdown("---")

    # ======================================================
    # Recommended Future Projects
    # ======================================================

    st.subheader("🚀 Suggested AI Projects")

    projects = [

        "Multi-Agent AI Systems",

        "LLM Applications using LangGraph",

        "Retrieval-Augmented Generation (RAG)",

        "AI Chatbot with Memory",

        "Medical AI using Computer Vision",

        "AI Document Assistant",

        "Speech-to-Text AI Applications",

        "Autonomous AI Agents"

    ]

    for project in projects:

        st.write(f"• {project}")

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

    st.progress(
        min(match_score / 100, 1.0)
    )

    if match_score >= 90:

        st.success(
            "🌟 Excellent! You are highly prepared for this role."
        )

    elif match_score >= 75:

        st.info(
            "👍 Good preparation. Minor improvements can strengthen your profile."
        )

    elif match_score >= 60:

        st.warning(
            "⚠ Improve your technical skills and resume before applying."
        )

    else:

        st.error(
            "❌ Significant upskilling is recommended before applying."
        )

    st.markdown("---")

    # ======================================================
    # Career Dashboard
    # ======================================================

    st.subheader("📌 Career Summary")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Career Readiness",
            f"{match_score:.0f}%"
        )

    with col2:

        if missing_skills:

            st.metric(
                "Missing Skills",
                str(len(missing_skills))
            )

        else:

            st.metric(
                "Missing Skills",
                "0"
            )

    with col3:

        if match_score >= 75:

            st.metric(
                "Recommendation",
                "Apply ✅"
            )

        else:

            st.metric(
                "Recommendation",
                "Upskill 📚"
            )

# ==========================================================
# 🎯 TAB 4 : Interview Preparation (Part 5A)
# ==========================================================

with tab4:

    st.header("🎯 AI Interview Preparation")

    questions = state.get(
        "interview_questions",
        ""
    )

    if not questions:

        st.warning(
            "Interview questions not generated."
        )

    else:

        # ======================================================
        # Job Description Analysis (NEW)
        # ======================================================

        st.subheader("📌 Job Description Analysis")

        st.info(
            """
The following technologies, responsibilities and skills
have been identified from the uploaded Job Description.
These are used to generate personalized interview questions.
"""
        )

        jd_analysis = ""

        if "# Technical Questions" in questions:

            jd_analysis = questions.split(
                "# Technical Questions"
            )[0]

        else:

            jd_analysis = questions

        st.markdown(jd_analysis)

        st.markdown("---")

        # ======================================================
        # Technical Questions
        # ======================================================

        technical_questions = ""

        if "# Project Questions" in questions:

            technical_questions = questions.split(
                "# Technical Questions"
            )[1].split(
                "# Project Questions"
            )[0]

        st.subheader("💻 Technical Questions")

        st.markdown(
            technical_questions
        )

        st.markdown("---")

        # ======================================================
        # Project Questions
        # ======================================================

        project_questions = ""

        if "# Behavioural Questions" in questions:

            project_questions = questions.split(
                "# Project Questions"
            )[1].split(
                "# Behavioural Questions"
            )[0]

        st.subheader("📂 Project Questions")

        st.markdown(
            project_questions
        )

        st.markdown("---")

        # ======================================================
        # Behavioural Questions
        # ======================================================

        behavioural_questions = ""

        if "# HR Questions" in questions:

            behavioural_questions = questions.split(
                "# Behavioural Questions"
            )[1].split(
                "# HR Questions"
            )[0]

        st.subheader("🧠 Behavioural Questions")

        st.markdown(
            behavioural_questions
        )

        st.markdown("---")

        # ======================================================
        # HR Questions
        # ======================================================

        hr_questions = ""

        if "# Job Description Specific Questions" in questions:

            hr_questions = questions.split(
                "# HR Questions"
            )[1].split(
                "# Job Description Specific Questions"
            )[0]

        else:

            hr_questions = questions.split(
                "# HR Questions"
            )[1]

        st.subheader("👨‍💼 HR Questions")

        st.markdown(
            hr_questions
        )

        st.markdown("---")

        # ======================================================
        # Job Description Specific Questions (NEW)
        # ======================================================

        if "# Job Description Specific Questions" in questions:

            jd_questions = questions.split(
                "# Job Description Specific Questions"
            )[1]

            st.subheader(
                "🎯 Job Description Specific Questions"
            )

            st.success(
                """
These questions are generated directly from the uploaded
Job Description and evaluate whether your skills match
the employer's expectations.
"""
            )

            st.markdown(
                jd_questions
            )

            st.markdown("---")
            # ======================================================
    # Candidate Answer
    # ======================================================

    st.header("✍️ Your Answer")

    candidate_answer = st.text_area(

        "Type your interview answer below",

        value=st.session_state.candidate_answer,

        height=220,

        placeholder="""
Type your answer here...

Tips:

• Explain your approach clearly.

• Mention technologies used.

• Discuss challenges.

• Explain your solution.

• Conclude with results.
"""
    )

    st.session_state.candidate_answer = candidate_answer

    st.markdown("---")

    # ======================================================
    # Voice Recorder
    # ======================================================

    st.subheader("🎤 Voice Mock Interview")

    audio = mic_recorder(

        start_prompt="🎤 Start Recording",

        stop_prompt="⏹ Stop Recording",

        key="voice_recorder"

    )

    if audio:

        st.success("✅ Voice Recorded Successfully")

        st.audio(audio["bytes"])

        st.info(
            """
Speech-to-text integration can be added using:

• OpenAI Whisper

• Google Speech-to-Text

• Azure Speech Services
"""
        )

    st.markdown("---")

    # ======================================================
    # Select Question
    # ======================================================

    st.subheader("📝 Interview Evaluation")

    interview_question = st.text_area(

        "Paste the interview question you answered",

        height=120,

        placeholder="Paste one interview question here..."

    )

    st.markdown("---")

    # ======================================================
    # Evaluate Button
    # ======================================================

    if st.button(

        "🚀 Evaluate My Answer",

        use_container_width=True

    ):

        if not interview_question.strip():

            st.warning(

                "Please enter the interview question."

            )

        elif not candidate_answer.strip():

            st.warning(

                "Please type your answer first."

            )

        else:

            with st.spinner(

                "🤖 AI Interviewer is evaluating your answer..."

            ):

                from utils.langchain.chain import (
                    run_evaluation_chain
                )

                evaluation = run_evaluation_chain(

                    question=interview_question,

                    answer=candidate_answer

                )

                st.session_state.interview_feedback = evaluation

    # ======================================================
    # Display Evaluation
    # ======================================================

    if "interview_feedback" in st.session_state:

        st.markdown("---")

        st.subheader("🤖 AI Interview Feedback")

        st.markdown(

            st.session_state.interview_feedback

        )

        st.markdown("---")

        st.subheader("📊 Interview Performance")

        st.info(
            """
Evaluation includes

✔ Technical Accuracy

✔ Completeness

✔ Communication

✔ Confidence

✔ Suggestions

✔ Final Score
"""
        )

        st.success(

            "Keep practising to improve your interview performance!"

        )

    st.markdown("---")

    # ======================================================
    # Interview Tips
    # ======================================================

    st.subheader("💡 Interview Tips")

    st.info(
        """
### During Technical Interviews

✔ Think aloud while solving problems.

✔ Explain your approach.

✔ Mention trade-offs.

✔ Use real project examples.

✔ Highlight measurable achievements.

✔ Don't rush your answer.

✔ Ask clarifying questions when required.

✔ End with a concise summary.
"""
    )

# ==========================================================
# 📄 TAB 5 : Reports
# ==========================================================

with tab5:

    st.header("📄 AI Reports")

    # ======================================================
    # Resume Analysis Report
    # ======================================================

    st.subheader("📊 Resume Analysis Report")

    analysis = state.get("analysis", "")

    if analysis:

        st.markdown(analysis)

    else:

        st.info("Resume Analysis Report not available.")

    st.markdown("---")

    # ======================================================
    # ATS Resume Report
    # ======================================================

    st.subheader("✨ ATS Optimized Resume")

    optimized_resume = state.get(
        "optimized_resume",
        ""
    )

    if optimized_resume:

        st.markdown(optimized_resume)

    else:

        st.info("ATS Resume not available.")

    st.markdown("---")

    # ======================================================
    # Career Coach Report
    # ======================================================

    st.subheader("👨‍💼 Career Coach Report")

    career = state.get(
        "career_advice",
        ""
    )

    if career:

        st.markdown(career)

    else:

        st.info("Career Coach Report not available.")

    st.markdown("---")

    # ======================================================
    # Skill Gap Report
    # ======================================================

    st.subheader("📈 Skill Gap Report")

    skill_gap = state.get(
        "skill_gap",
        ""
    )

    if skill_gap:

        st.markdown(skill_gap)

    else:

        st.info("Skill Gap Report not available.")

    st.markdown("---")

    # ======================================================
    # Interview Questions Report
    # ======================================================

    st.subheader("🎯 Interview Preparation Report")

    questions = state.get(
        "interview_questions",
        ""
    )

    if questions:

        st.markdown(questions)

    else:

        st.info("Interview Questions not available.")

    st.markdown("---")

    # ======================================================
    # Interview Evaluation Report
    # ======================================================

    if "interview_feedback" in st.session_state:

        st.subheader("📝 Interview Evaluation Report")

        st.markdown(

            st.session_state.interview_feedback

        )

        st.markdown("---")

    # ======================================================
    # Download ATS Resume
    # ======================================================

    st.subheader("📥 Downloads")

    if optimized_resume:

        pdf_file = generate_resume_pdf(
            optimized_resume
        )

        with open(
            pdf_file,
            "rb"
        ) as file:

            st.download_button(

                label="📄 Download ATS Resume PDF",

                data=file,

                file_name="ATS_Optimized_Resume.pdf",

                mime="application/pdf",

                use_container_width=True

            )

    st.markdown("---")

    # ======================================================
    # Workflow Summary
    # ======================================================

    st.subheader("🔄 InterviewAce AI Workflow")

    st.markdown(
        """
        """
    )

    st.markdown("---")

    # ======================================================
    # Technologies Used
    # ======================================================

    st.subheader("🛠 Technologies Used")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
### AI

- Gemini 2.5 Flash
- LangChain
- LangGraph
- RAG
- Multi-Agent AI

### Machine Learning

- Sentence Transformers
- FAISS
"""
        )

    with col2:

        st.markdown(
            """
### Frameworks

- Streamlit
- Python

### Libraries

- ReportLab
- pdfplumber
- NumPy
- Pandas
"""
        )

    st.markdown("---")

    # ======================================================
    # Future Scope
    # ======================================================

    st.subheader("🚀 Future Enhancements")

    st.markdown(
        """
✔ Flutter Mobile Application

✔ FastAPI Backend

✔ User Authentication

✔ Cloud Deployment

✔ LinkedIn Profile Analysis

✔ Coding Interview Module

✔ Speech-to-Text Evaluation

✔ Multilingual Interview Support

✔ Resume Version History

✔ AI Career Dashboard
"""
    )

    st.markdown("---")

    # ======================================================
    # Footer
    # ======================================================

    st.success(
        "🎉 Thank you for using InterviewAce AI!"
    )

    st.caption(
        "Built using Streamlit • LangGraph • LangChain • Gemini • FAISS • Sentence Transformers"
    )