from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from Resume import Resume
import json

#from Resume import Resume


pdfmetrics.registerFont(TTFont('Cambria', './fonts/Cambria.ttf'))
pdfmetrics.registerFont(TTFont('Cambria-Bold', './fonts/Cambria-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Cambria-Italic', './fonts/Cambria-Italic.ttf'))
styles = getSampleStyleSheet()

# NOTE: THIS CODE EXPECTS BULLET POINTS TO BE STORED IN THE DATABSE AS JSON ARRAYS

# IF FONT SIZE IS CHANGED, ALL HORIZONTAL LINES WILL BE RUINED
regFontSize = 10.5
titleFontSize = 14
tinyFontSize = 9.5

def generateResume(usr_id):
    # Create a PDF document
    document = SimpleDocTemplate("resume.pdf", pagesize=letter, leftMargin=0.5*inch, rightMargin=0.5*inch, topMargin=0.5*inch, bottomMargin=0.5*inch)
    doc = []


    # Fetch user data
    resume = Resume()
    resume.getUserInfo(usr_id)


    experiences = resume.experience
    extracurriculars = resume.extracurr
    general_infos = resume.general_info
    projects = resume.projects
    technical_skills = resume.technical_skills
    
    # Gen INFO

    style = nameTitleStyle()

    title = Paragraph(f"{general_infos[0].firstname} {general_infos[0].lastname}", style)
    
    doc.append(title)


    # Phone Number might not exist(optional field)
    phoneNum = general_infos[0].phone
    style = tinyStyle()
    if phoneNumber is None:
        smallTxt = Paragraph(f"{general_infos[0].email} • {general_infos[0].linkedin}", style)
        doc.append(smallTxt)
    else:
        smallTxt = Paragraph(f"{general_infos[0].email} • {phoneNumber(phoneNum)} • {general_infos[0].linkedin}", style)
        doc.append(smallTxt)


    eduTitle = Paragraph(f"<u>EDUCATION{whiteSpace(203)}</u>", underlineBoldStyle())
    doc.append(eduTitle)

    # EDUCATION TABLE
    col_widths = [2.5*inch, 3.875*inch, 1.125*inch]
    t1 = Paragraph(general_infos[0].edu, regularBoldStyle())
    t2 = Paragraph(general_infos[0].major, regularStyle())
    t3 = Paragraph(general_infos[0].grad_date, regularRightStyle())
    t4 = Paragraph(f"Overall GPA: {general_infos[0].GPA}", regularBoldStyle())
    tEmpty = Paragraph("", regularStyle())
    data = [
        [t1,t2,t3],
        [tEmpty, t4, tEmpty]
    ]
    table = Table(data, colWidths=col_widths)
    table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.white), ('BOX', (0, 0), (-1, -1), 0.25, colors.white)]))
    doc.append(table)

    spacer = Spacer(1, 0.125*inch)
    doc.append(spacer)
    
    # SKILLS


  
    skillsStr = ""
    finalSkill = technical_skills.pop()  
    for skill in technical_skills:
        skillsStr = skillsStr + skill.name + ", "
    skillsStr = skillsStr + finalSkill.name

    skills = (Paragraph(f"<font face = 'Cambria-Bold'>Relavent Skills:</font> {skillsStr}", justifyRegularStyle()))
    doc.append(skills)

    # EXPERIENCE
    expTitle = Paragraph(f"<br></br><u>EXPERIENCE{whiteSpace(201)}</u>", underlineBoldStyle())
    
    doc.append(expTitle)
    for i in range(len(experiences)):
        col_widths = [5*inch, 2.5*inch]
        #t1 = Paragraph(experiences[0].company, regularBoldStyle())
        t1 = Paragraph(text=f"<font face = 'Cambria-Bold' size={regFontSize}>{experiences[i].company}</font> - <font face=Cambria-Italic size={regFontSize}> {experiences[i].role}; {experiences[i].location}</font>")
        #t2 = Paragraph(f"{experiences[0].role}; {experiences[0].location}", regularStyle())
        t2 = Paragraph(f"{experiences[i].start_date} - {experiences[i].end_date}", regularRightStyle())
        data = [
            [t1,t2]
        ]
        table = Table(data, colWidths=col_widths)
        table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.white), ('BOX', (0, 0), (-1, -1), 0.25, colors.white)]))
        doc.append(table)
        desc_array = json.loads(experiences[i].desc_arr)
        for desc in desc_array:
            ptext=f'<bullet>&bull;</bullet>{desc}'
            doc.append(Paragraph(ptext, regularStyle()))
        
        spacer = Spacer(1, 0.125*inch)
        doc.append(spacer)
        
        

        if i > 3:
            break
    #exp
    #code
    #here

    # PROJECTS
    projTitle = Paragraph(f"<br></br><u>PROJECTS{whiteSpace(207)}</u>", underlineBoldStyle())
    doc.append(projTitle)

    for i in range(len(projects)):
        col_widths = [5*inch, 2.5*inch]
        #t1 = Paragraph(experiences[0].company, regularBoldStyle())
        t1 = Paragraph(text=f"<font face = 'Cambria-Bold' size={regFontSize}>{projects[i].title}</font> - <font face=Cambria-Italic size={regFontSize}> {projects[i].who_for}</font>")
        #t2 = Paragraph(f"{projects[0].role}; {projects[0].location}", regularStyle())
        t2 = Paragraph(f"{projects[i].date}", regularRightStyle())
        data = [
            [t1,t2]
        ]
        table = Table(data, colWidths=col_widths)
        table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.white), ('BOX', (0, 0), (-1, -1), 0.25, colors.white)]))
        doc.append(table)
        desc_array = json.loads(projects[i].desc_arr)
        for desc in desc_array:
            ptext = f'<bullet>&bull;</bullet>{desc}'
            doc.append(Paragraph(ptext, regularStyle()))
            
        spacer = Spacer(1, 0.125*inch)
        doc.append(spacer)
        
        

        if i > 3:
            break


    # EXTRACURRICULARS
    extraTitle = Paragraph(f"<br></br><u>EXTRACURRICULARS{whiteSpace(184)}</u>", underlineBoldStyle())
    #code here 

    doc.append(extraTitle)

    #temp dates for activiteies
    dates = ['May 1931', 'October 1944', 'January 1956']

    for i in range(len(extracurriculars)):
        col_widths = [5*inch, 2.5*inch]
        t1 = Paragraph(text=f"<font face = 'Cambria-Bold' size={regFontSize}>{extracurriculars[i].title}</font>")
        #t1 = Paragraph(text=f"<font face = 'Cambria-Bold' size={regFontSize}>{extracurriculars[i].title}</font> - <font face=Cambria-Italic size={regFontSize}>{extracurriculars[i].desc_arr}</font>")
        #t2 = Paragraph(f"{extracurriculars[i].date}", regularRightStyle())
        t2 = Paragraph(f"{dates[i]}", regularRightStyle())

        data = [
            [t1,t2]
        ]

        table = Table(data, colWidths=col_widths)
        table.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.white), ('BOX', (0, 0), (-1, -1), 0.25, colors.white)]))
        doc.append(table)
        spacer = Spacer(1, 0.125*inch)
        doc.append(spacer)
        
        

        if i > 3:
            break


    # Save the PDF
    document.build(doc)


    
def whiteSpace(num):
    str = ""
    for i in range(num):
        str = str + "&nbsp;"
    return str


def phoneNumber(number):
    # Convert the number to a string
    number_str = str(number)

    # Ensure the number has exactly 10 digits
    if len(number_str) != 10:
        raise ValueError("Phone number must have exactly 10 digits.")

    # Format the string as (123) 456-7890
    formatted_number = f"({number_str[0:3]}) {number_str[3:6]}-{number_str[6:]}"

    return formatted_number



def nameTitleStyle():
    style = ParagraphStyle(name='Title', parent=styles['Normal'], fontName='Cambria-Bold', fontSize=titleFontSize, alignment=TA_CENTER, leading=titleFontSize)
    return style
def tinyStyle():
    style = ParagraphStyle(name='Tiny', parent=styles['Normal'], fontName='Cambria', fontSize=tinyFontSize, alignment=TA_CENTER, leading=titleFontSize)
    return style
def justifyRegularStyle():
    style = ParagraphStyle(name='JustifyRegular', parent=styles['Normal'], fontName='Cambria', fontSize=regFontSize, alignment=TA_JUSTIFY, leading=regFontSize)
    return style
def regularStyle():
    style = ParagraphStyle(name='Regular', parent=styles['Normal'], fontName='Cambria', fontSize=regFontSize, alignment=TA_LEFT, leading=regFontSize)
    return style
def regularBoldStyle():
    style = ParagraphStyle(name='RegularBold', parent=styles['Normal'], fontName='Cambria-Bold', fontSize=regFontSize, alignment=TA_LEFT, leading=regFontSize)
    return style
def underlineBoldStyle():
    style = ParagraphStyle(name='UnderlinedBold', parent=styles['Normal'], fontName='Cambria-Bold', fontSize=regFontSize, alignment=TA_LEFT, leading=regFontSize)
    return style
def regularRightStyle():
    style = ParagraphStyle(name='RegularRight', parent=styles['Normal'], fontName='Cambria', fontSize=regFontSize, alignment=TA_RIGHT, leading=regFontSize)
    return style

#def ItalicRegular():

if __name__ == "__main__":
    generateResume(1)


