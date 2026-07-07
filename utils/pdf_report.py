from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet


# ===========================================================
# Utility
# ===========================================================

def safe_text(text):

    if not text:
        return "Not Available"

    return str(text).replace(
        "\n",
        "<br/>"
    )


# ===========================================================
# Complete InterviewAce Report
# ===========================================================

def generate_pdf_report(

    score,

    analysis,

    optimized_resume,

    questions,

    evaluation,

    career_advice,

    skill_gap,

    output_file="InterviewAce_Report.pdf"

):

    doc = SimpleDocTemplate(output_file)

    styles = getSampleStyleSheet()

    content = []

    # ======================================================
    # Title
    # ======================================================

    content.append(

        Paragraph(
            "InterviewAce AI Report",
            styles["Title"]
        )

    )

    content.append(

        Paragraph(
            f"Generated on : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
            styles["BodyText"]
        )

    )

    content.append(
        Spacer(1,20)
    )

    # ======================================================
    # Match Score
    # ======================================================

    content.append(

        Paragraph(
            "Overall Job Match Score",
            styles["Heading1"]
        )

    )

    content.append(

        Paragraph(
            f"<b>{score:.2f}%</b>",
            styles["Heading2"]
        )

    )

    content.append(
        Spacer(1,15)
    )

    # ======================================================
    # Resume Analysis
    # ======================================================

    content.append(
        Paragraph(
            "Resume Analysis",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            safe_text(analysis),
            styles["BodyText"]
        )
    )

    content.append(PageBreak())

    # ======================================================
    # Resume Optimizer
    # ======================================================

    content.append(
        Paragraph(
            "Optimized Resume",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            safe_text(optimized_resume),
            styles["BodyText"]
        )
    )

    content.append(PageBreak())

    # ======================================================
    # Skill Gap
    # ======================================================

    content.append(
        Paragraph(
            "Skill Gap Analysis",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            safe_text(skill_gap),
            styles["BodyText"]
        )
    )

    content.append(PageBreak())

    # ======================================================
    # Interview Questions
    # ======================================================

    content.append(
        Paragraph(
            "Generated Interview Questions",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            safe_text(questions),
            styles["BodyText"]
        )
    )

    content.append(PageBreak())

    # ======================================================
    # Interview Evaluation
    # ======================================================

    content.append(
        Paragraph(
            "Interview Evaluation",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            safe_text(evaluation),
            styles["BodyText"]
        )
    )

    content.append(PageBreak())

    # ======================================================
    # Career Coach
    # ======================================================

    content.append(
        Paragraph(
            "Career Coach Recommendations",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            safe_text(career_advice),
            styles["BodyText"]
        )
    )

    content.append(PageBreak())

    # ======================================================
    # Workflow Summary
    # ======================================================

    content.append(
        Paragraph(
            "InterviewAce AI Workflow Summary",
            styles["Heading1"]
        )
    )

    summary = """
    1. Resume Uploaded
    <br/>
    2. Resume Text Extracted
    <br/>
    3. Resume Chunked
    <br/>
    4. Sentence Embeddings Generated
    <br/>
    5. FAISS Vector Database Created
    <br/>
    6. Relevant Resume Chunks Retrieved using RAG
    <br/>
    7. Resume Analysis Agent
    <br/>
    8. Resume Optimizer Agent
    <br/>
    9. Skill Gap Agent
    <br/>
    10. Interview Question Agent
    <br/>
    11. Interview Evaluation Agent
    <br/>
    12. Career Coach Agent
    <br/>
    13. Report Generation Agent
    """

    content.append(

        Paragraph(
            summary,
            styles["BodyText"]
        )

    )

    doc.build(content)

    return output_file


# ===========================================================
# Optimized Resume PDF
# ===========================================================

def generate_resume_pdf(

    optimized_resume,

    output_file="Optimized_Resume.pdf"

):

    doc = SimpleDocTemplate(output_file)

    styles = getSampleStyleSheet()

    content = []

    content.append(

        Paragraph(
            "Optimized Resume",
            styles["Title"]
        )

    )

    content.append(
        Spacer(1,20)
    )

    content.append(

        Paragraph(
            safe_text(optimized_resume),
            styles["BodyText"]
        )

    )

    doc.build(content)

    return output_file