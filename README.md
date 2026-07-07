# 🚀 InterviewAce AI
### A Multi-Agent LLM & RAG-Based Intelligent Interview Preparation and Resume Analysis System

InterviewAce AI is an end-to-end **Generative AI** application that helps job seekers improve their resumes and prepare for interviews using **Large Language Models (LLMs)**, **Retrieval-Augmented Generation (RAG)**, and a **Multi-Agent AI** architecture.

The system performs semantic resume analysis, ATS optimization, skill-gap assessment, personalized interview question generation, AI-powered answer evaluation, career coaching, and automated PDF report generation through an interactive Streamlit web application.

---

# 🌟 Features

- 📄 Resume Upload (PDF)
- 🎯 Job Description Matching
- 🤖 Multi-Agent AI Workflow
- 🧠 LLM-Powered Resume Analysis
- 📊 ATS Resume Optimization
- 🔍 Semantic Resume Search using FAISS
- 📈 Skill Gap Analysis
- 💼 Career Coaching
- ❓ Personalized Interview Question Generation
- 📝 AI-Powered Interview Answer Evaluation
- 📑 Automated PDF Report Generation
- 🎤 Voice Recording Support (Optional)
- 🌐 Interactive Streamlit Web Interface

---

# 🏗️ System Architecture

```
                    User
                      │
                      ▼
             Streamlit Web Interface
                      │
        ┌─────────────┴─────────────┐
        ▼                           ▼
 Resume Upload              Job Description
        │                           │
        └─────────────┬─────────────┘
                      ▼
             PDF Text Extraction
                (pdfplumber)
                      │
                      ▼
               Text Chunking
                      │
                      ▼
      Sentence Transformer Embeddings
                      │
                      ▼
          FAISS Vector Database
                      │
                      ▼
        Retrieval-Augmented Generation
                      │
                      ▼
            Gemini 2.5 Flash LLM
                      │
                      ▼
          LangGraph Multi-Agent Workflow
                      │
──────────────────────────────────────────────
Resume Analysis Agent

Resume Optimizer Agent

Skill Gap Agent

Career Coach Agent

Interview Question Agent

Interview Evaluation Agent

Report Generation Agent
──────────────────────────────────────────────
                      │
                      ▼
            Streamlit Results + PDF Reports
```

---

# ⚙️ Workflow

```
Resume Upload
      │
      ▼
PDF Loader
      │
      ▼
Chunking
      │
      ▼
Sentence Embeddings
      │
      ▼
FAISS Vector Index
      │
      ▼
Retriever
      │
      ▼
Gemini 2.5 Flash
      │
      ▼
LangGraph Workflow
      │
      ▼
Multi-Agent AI
      │
      ▼
PDF Report Generation
```

---

# 🤖 Multi-Agent Workflow

The application is built using **LangGraph**, where each agent performs a specialized task.

```
Resume Analysis Agent
          │
          ▼
Supervisor Agent
          │
          ▼
Resume Optimizer Agent
          │
          ▼
Skill Gap Agent
          │
          ▼
Career Coach Agent
          │
          ▼
Interview Question Agent
          │
          ▼
Interview Evaluation Agent
          │
          ▼
Report Generation Agent
```

---

# 🛠️ Technology Stack

## Programming Language

- Python

## Generative AI

- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- Multi-Agent AI

## LLM

- Gemini 2.5 Flash

## AI Frameworks

- LangChain
- LangGraph

## Semantic Search

- Sentence Transformers
- FAISS

## Machine Learning

- TensorFlow
- PyTorch
- Scikit-learn

## Web Framework

- Streamlit

## PDF Processing

- pdfplumber
- ReportLab

## Data Processing

- NumPy
- Pandas

---

# 📂 Project Structure

```
InterviewAce-AI/
│
├── app.py
├── workflow.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│
├── langgraph_agents/
│   ├── state.py
│   ├── supervisor.py
│   ├── resume_analysis_agent.py
│   ├── resume_optimizer_agent.py
│   ├── skill_gap_agent.py
│   ├── career_coach_agent.py
│   ├── interview_question_agent.py
│   ├── interview_evaluation_agent.py
│   └── report_generation_agent.py
│
├── utils/
│   ├── pdf_loader.py
│   ├── embedder.py
│   ├── faiss_store.py
│   ├── rag.py
│   ├── pdf_report.py
│   └── langchain/
│
└── reports/
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/InterviewAce-AI.git
```

```
cd InterviewAce-AI
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Gemini API

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Run Application

```bash
streamlit run app.py
```

---

# 📸 Screenshots

## Home Page

Add screenshot here

```
assets/home.png
```

---

## Resume Analysis

```
assets/resume_analysis.png
```

---

## ATS Resume

```
assets/ats_resume.png
```

---

## Skill Gap Analysis

```
assets/skill_gap.png
```

---

## Career Coach

```
assets/career_coach.png
```

---

## Interview Questions

```
assets/questions.png
```

---

## Interview Evaluation

```
assets/evaluation.png
```

---

## PDF Report

```
assets/report.png
```

---

# 🎯 Features Explained

### Resume Analysis

- Resume Matching
- ATS Score
- Strengths
- Weaknesses
- Missing Skills

---

### ATS Optimization

- Improved Formatting
- ATS Friendly Content
- Better Keywords
- Professional Structure

---

### Skill Gap Analysis

- Missing Skills
- Learning Roadmap
- Priority Technologies

---

### Career Coach

- Certifications
- Projects
- Career Advice
- Learning Path

---

### Interview Questions

- Technical Questions
- HR Questions
- Behavioural Questions
- Project Questions

---

### Interview Evaluation

- AI Score
- Feedback
- Strengths
- Weaknesses
- Suggested Improvements

---

### Report Generation

- InterviewAce_Report.pdf
- Optimized_Resume.pdf

---

# 💡 Future Improvements

- User Authentication
- Cloud Deployment
- Persistent Vector Database
- Resume History
- Speech-to-Text Integration
- Coding Interview Module
- LinkedIn Profile Analysis
- Job Portal Integration
- Multilingual Support
- Mobile Application

---

# 📚 Key Concepts Used

- Generative AI
- Large Language Models
- Retrieval-Augmented Generation
- LangChain
- LangGraph
- Multi-Agent AI
- Prompt Engineering
- Semantic Search
- Sentence Embeddings
- Vector Database
- FAISS
- Streamlit

---

# 🚀 Future Scope

The following enhancements are planned for future versions of InterviewAce AI:

- 📱 Mobile Application (Flutter)
- ☁ Cloud Deployment (AWS / Azure / GCP)
- 🔐 User Authentication & Dashboard
- 💻 Coding Interview Assessment
- 🎙 Speech-to-Text Interview Evaluation
- 🌍 Multilingual Interview Support
- 💼 LinkedIn Profile Analysis
- 🔗 Job Portal Integration
- 📊 Interview Performance Analytics
- 🧠 Personalized AI Career Roadmaps
- 📂 Resume Version History
- 🤝 Recruiter Feedback Dashboard


# 👨‍💻 Author

**Dharani Partha Sarathy**

M.Tech Artificial Intelligence & Data Science

Python | Generative AI | LLMs | RAG | LangChain | LangGraph | Machine Learning | Deep Learning

---

# ⭐ If you found this project useful, please consider giving it a Star!
