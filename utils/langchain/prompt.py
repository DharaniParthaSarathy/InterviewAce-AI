from langchain_core.prompts import PromptTemplate

# ==========================================================
# Resume Analysis Prompt
# ==========================================================

analysis_prompt = PromptTemplate.from_template(
"""
You are an expert AI recruiter.

Analyze the candidate's resume against the Job Description.

Use ONLY the provided Resume Context.

==============================
Resume Context
==============================

{context}

==============================
Job Description
==============================

{job_description}

Provide the following:

1. Match Score (0-100%)

2. Matched Skills

3. Missing Skills

4. Candidate Strengths

5. Candidate Weaknesses

6. Final Recommendation

Return the answer in professional markdown.
"""
)

# ==========================================================
# Resume Optimizer Prompt
# ==========================================================

optimizer_prompt = PromptTemplate.from_template(
"""
You are an ATS Resume Optimization Expert.

Rewrite the resume using ONLY the provided Resume Context.

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

• Never invent projects.

• Never invent certifications.

• Never invent companies.

• Never invent skills.

• Improve ATS keywords.

• Improve grammar.

• Improve formatting.

• Keep every fact truthful.

Return the COMPLETE optimized resume.
"""
)

# ==========================================================
# Skill Gap Prompt
# ==========================================================

skill_gap_prompt = PromptTemplate.from_template(
"""
You are an AI Career Coach.

Compare the Resume Context with the Job Description.

Use ONLY the provided context.

==============================
Resume Context
==============================

{context}

==============================
Job Description
==============================

{job_description}

Return in EXACTLY this format.

Overall Skill Gap

<summary>

Missing Skills

- Skill 1
- Skill 2
- Skill 3

Recommended Skills

- Skill A
- Skill B
- Skill C

Learning Roadmap

1.
2.
3.

Final Advice
"""
)

# ==========================================================
# Interview Question Prompt
# ==========================================================

question_prompt = PromptTemplate.from_template(
"""
You are a Senior Technical Interviewer.

Generate interview questions using ONLY the Resume Context.

==============================
Resume Context
==============================

{context}

==============================
Job Description
==============================

{job_description}

Generate

## Technical Questions
5 questions

## Project Questions
5 questions

## Behavioural Questions
5 questions

## HR Questions
5 questions

Questions should evaluate

• Technical knowledge

• Project understanding

• Problem solving

• Communication

Return ONLY the questions.
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

Evaluate the answer using

1. Technical Accuracy

2. Completeness

3. Communication

4. Confidence

5. Suggestions for Improvement

6. Final Score (0-100)

Return professional feedback.
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

Provide

1. Overall Career Assessment

2. Should the candidate apply now?

3. Skills to learn immediately

4. Recommended Certifications

5. Recommended Projects

6. 3-Month Learning Roadmap

7. Interview Preparation Tips

8. Final Career Advice

Return the answer professionally.
"""
)