from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

from exampleResumeData import fetch_and_return

document = SimpleDocTemplate("resume.pdf", pagesize=letter)
styles = getSampleStyleSheet()

experiences, extracurriculars, general_infos, projects, technical_skills = fetch_and_return()




def generateResume():
    # Fetch resume data
    experiences, extracurriculars, general_infos, projects, technical_skills = fetch_and_return()

    # Create a new PDF document
    c = canvas.Canvas("resume.pdf", pagesize=letter)

    # Write general information to the PDF
    c.drawString(100, 700, f"Name: {general_infos[0].firstname} {general_infos[0].lastname}")
    c.drawString(100, 680, f"Email: {general_infos[0].email}")
    c.drawString(100, 660, f"Phone: {general_infos[0].phone}")
    c.drawString(100, 640, f"LinkedIn: {general_infos[0].linkedin}")
    c.drawString(100, 620, f"Education: {general_infos[0].edu}")
    c.drawString(100, 600, f"Graduation Date: {general_infos[0].grad_date}")
    c.drawString(100, 580, f"Major: {general_infos[0].major}")
    c.drawString(100, 560, f"GPA: {general_infos[0].GPA}")

    # Save the PDF
    c.save()

if __name__ == "__main__":
    generateResume()