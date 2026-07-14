from langchain_core.prompts import PromptTemplate

# ==========================================================
# Resume Analysis Prompt
# ==========================================================

analysis_prompt = PromptTemplate.from_template(
"""
You are an expert AI Recruiter and Resume Screening Specialist.

Analyze the candidate's resume against the provided Job Description.

Use ONLY the Resume Context provided below.

==============================
Resume Context
==============================

{context}

==============================
Job Description
==============================

{job_description}

Provide the following sections:

## Match Score
(Give a percentage from 0-100%)

## Overall Summary

## Matched Skills

## Missing Skills

## Candidate Strengths

## Candidate Weaknesses

## ATS Improvement Suggestions

## Final Recommendation

Return the answer in professional Markdown format.
"""
)

# ==========================================================
# Resume Optimizer Prompt
# ==========================================================

optimizer_prompt = PromptTemplate.from_template(
"""
You are an ATS Resume Optimization Expert.

Rewrite the resume using ONLY the Resume Context.

==============================
Resume Context
==============================

{context}

==============================
Job Description
==============================

{job_description}

Rules

• Never invent experience.
• Never invent companies.
• Never invent projects.
• Never invent certifications.
• Never invent technical skills.
• Never exaggerate achievements.
• Improve ATS keyword matching.
• Improve formatting.
• Improve grammar.
• Improve readability.
• Preserve factual accuracy.

Return the COMPLETE ATS-optimized resume in Markdown.
"""
)

# ==========================================================
# Skill Gap Prompt
# ==========================================================

skill_gap_prompt = PromptTemplate.from_template(
"""
You are an AI Career Coach.

Compare the Resume Context with the Job Description.

Use ONLY the provided information.

==============================
Resume Context
==============================

{context}

==============================
Job Description
==============================

{job_description}

Return the following sections.

## Overall Skill Gap

## Matching Skills

## Missing Skills

## Recommended Skills

## Learning Roadmap

## Priority Technologies

## Final Advice

Return professional Markdown.
"""
)

# ==========================================================
# Interview Question Prompt
# ==========================================================

question_prompt = PromptTemplate.from_template(
"""
You are a Senior Technical Interviewer with experience in hiring software engineers, AI engineers, and data scientists.

Your task is to generate interview questions based on BOTH:

1. Resume Context
2. Job Description

Use ONLY the information provided below.

==================================================
Resume Context
==================================================

{context}

==================================================
Job Description
==================================================

{job_description}

--------------------------------------------------
Step 1 : Analyze the Job Description
--------------------------------------------------

Identify:

• Required Skills
• Required Programming Languages
• Frameworks
• Libraries
• Databases
• Cloud Platforms
• AI / ML Technologies
• Responsibilities
• Preferred Qualifications
• Soft Skills

--------------------------------------------------
Step 2 : Generate Interview Questions
--------------------------------------------------

Generate the following sections.

# Technical Questions
Generate 5 technical interview questions based on BOTH the Resume and Job Description.

# Project Questions
Generate 5 project-specific questions based on the candidate's resume projects.

# Behavioural Questions
Generate 5 behavioural questions.

# HR Questions
Generate 5 HR interview questions.

# Job Description Specific Questions
Carefully analyze the Job Description and generate 5 interview questions specifically targeting:

• Technologies
• Tools
• Frameworks
• Libraries
• Responsibilities
• Domain Knowledge

These questions should evaluate whether the candidate satisfies the Job Description.

--------------------------------------------------
Rules
--------------------------------------------------

Questions should evaluate:

• Technical Knowledge
• Practical Implementation
• Problem Solving
• Communication Skills
• Project Understanding
• Domain Knowledge

Return the response in the EXACT format below.

# Job Description Analysis

## Required Skills

-

-

-

## Technologies

-

-

-

## Responsibilities

-

-

-

# Technical Questions

1.

2.

3.

4.

5.

# Project Questions

1.

2.

3.

4.

5.

# Behavioural Questions

1.

2.

3.

4.

5.

# HR Questions

1.

2.

3.

4.

5.

# Job Description Specific Questions

1.

2.

3.

4.

5.

Return ONLY the interview preparation content.
"""
)

# ==========================================================
# Interview Evaluation Prompt
# ==========================================================

evaluation_prompt = PromptTemplate.from_template(
"""
You are an experienced Technical Interviewer.

Interview Question

{question}

Candidate Answer

{answer}

Evaluate the answer using the following criteria.

## Technical Accuracy

## Completeness

## Communication

## Confidence

## Strengths

## Weaknesses

## Suggestions for Improvement

## Final Score (0-100)

Return professional feedback in Markdown.
"""
)

# ==========================================================
# Career Coach Prompt
# ==========================================================

career_coach_prompt = PromptTemplate.from_template(
"""
You are an experienced AI Career Mentor.

Based ONLY on the Resume Context and Job Description, provide career guidance.

==============================
Resume Context
==============================

{context}

==============================
Job Description
==============================

{job_description}

Provide the following.

## Overall Career Assessment

## Should the Candidate Apply?

## Skills to Learn Immediately

## Recommended Certifications

## Recommended Projects

## 3-Month Learning Roadmap

## Interview Preparation Tips

## Final Career Advice

Return professional Markdown.
"""
)