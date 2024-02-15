from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

document = SimpleDocTemplate("resume.pdf", pagesize=letter)
styles = getSampleStyleSheet()



def generateResume(data):
    document.append(Paragraph(data, styles["Normal"]))