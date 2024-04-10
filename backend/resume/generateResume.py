from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors

# For Dev
# from Resume import Resume

# # For Prod
from resume.Resume import Resume
import json
import os
import sqlite3

#from Resume import Resume


pdfmetrics.registerFont(TTFont('Cambria', 'backend/resume/fonts/Cambria.ttf'))
pdfmetrics.registerFont(TTFont('Cambria-Bold', 'backend/resume/fonts/Cambria-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Cambria-Italic', 'backend/resume/fonts/Cambria-Italic.ttf'))
styles = getSampleStyleSheet()

# NOTE: THIS CODE EXPECTS BULLET POINTS TO BE STORED IN THE DATABSE AS JSON ARRAYS

# IF FONT SIZE IS CHANGED, ALL HORIZONTAL LINES WILL BE RUINED
regFontSize = 10.5
titleFontSize = 14
tinyFontSize = 9.5

#WHERE RESUME IS STORED
def connect_to_database():
    try:
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')
        return conn
    except sqlite3.Error as e:
        print("Error connecting to database:", e)
        return None

def deleteResumeFile(filepath):
    os.remove(filepath)

def generateResume(usr_id):
    # Define the filename based on usr_id
    filename = f"backend/resumes/resume-{usr_id}.pdf"
    
    # Create the "resumes" folder if it doesn't exist
    os.makedirs("backend/resumes", exist_ok=True)


    # Create a PDF document
    document = SimpleDocTemplate(filename, pagesize=letter, leftMargin=0.5*inch, rightMargin=0.5*inch, topMargin=0.5*inch, bottomMargin=0.5*inch)
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
        smallTxt = Paragraph(f"{general_infos[0].email} • {phoneNum} • {general_infos[0].linkedin}", style)
        doc.append(smallTxt)


    eduTitle = Paragraph(f"<u>EDUCATION{whiteSpace(203)}</u>", underlineBoldStyle())
    doc.append(eduTitle)

    # EDUCATION TABLE
    col_widths = [2.5*inch, 3.875*inch, 1.125*inch]
    t1 = Paragraph(general_infos[0].edu, regularBoldStyle())
    t2 = Paragraph(general_infos[0].major, regularStyle())
    t3 = Paragraph(general_infos[0].grad_date, regularRightStyle())
    t4 = Paragraph(f"Overall GPA: {fixGPA(general_infos[0].GPA)}", regularBoldStyle())
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
        
        

        if i > 4:
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
        
        

        if i > 4:
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
        date = extracurriculars[i].desc
        t2 = Paragraph(f"{date}", regularRightStyle())

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


    # SEND THROUGH 


    
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

def fixGPA(gpa):
    gpa_str = "{:.2f}".format(gpa)
    return gpa_str



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

def generateUniqueID(id_name, table):
        conn = connect_to_database()
        cursor = conn.cursor() 
        cursor.execute('SELECT ' + id_name + ' FROM ' + table)
        result = cursor.fetchall()
        ids = [results[0] for results in result]
        if not ids:
            return 1
        unique_id = max(ids) + 1
        conn.close()
        return unique_id

def fill_example_data(usr_id):
    conn = connect_to_database()  
    if conn:
        cursor = conn.cursor()
        # Example data for the provided usr_id
        
        # GEN INFO

        howie_info = (usr_id, 'DeWitt', 'Howie', 1234567890, 'howiedewitt@example.com', 'linkedin.com/howie', 'The University of Texas at Austin', 'May 2024', 'Bachelor of Science: Computer Science', 3.80)

        # Insert general info
        cursor.execute("INSERT INTO general_info VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", howie_info)

        
        # PROJ DATA
        proj_desc1 = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.']
        proj_desc2 = ['Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.']
        proj_desc3 = ['Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', 
                       'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.']
        proj_desc4 = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.']
        json1 = json.dumps(proj_desc1)
        json2 = json.dumps(proj_desc2)
        json3 = json.dumps(proj_desc3)
        json4 = json.dumps(proj_desc4)

        next_idx = generateUniqueID('proj_id', 'projects')
        projects_data = [
            (usr_id, next_idx, 'Project A', 'Company A', 'June 1783', json1),
            (usr_id, next_idx+1, 'Project B', 'Company B', 'August 1939', json2),
            (usr_id, next_idx+2, 'Project C', 'Company C', 'December 2000', json3),
            (usr_id, next_idx+3, 'Project D', 'Company D', 'January 2022', json4)
        ]

        # Insert projects
        cursor.executemany("INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?)", projects_data)

        # EXPERIENCE DATA

        desc_array1 = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.']
        desc_array2 = ['Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.', 
                       'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', 
                       'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',]
        desc_array3 = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.']
        json1 = json.dumps(desc_array1)
        json2 = json.dumps(desc_array2)
        json3 = json.dumps(desc_array3)

        next_idx = generateUniqueID('job_id', 'experience')
        experiences_data = [
            (usr_id, next_idx, 'Company X', 'Software Engineer', 'Spring 2022', 'Present', 'New York', json1),
            (usr_id, next_idx+1, 'Company Y', 'Data Analyst', 'January 2017', 'Spring 2022', 'San Francisco', json2),
            (usr_id, next_idx+2, 'Company Z', 'Marketing Intern', 'Summer 2016', 'August 2016', 'Austin', json3)
        ]

        # Insert job experiences
        cursor.executemany("INSERT INTO experience VALUES (?, ?, ?, ?, ?, ?, ?, ?)", experiences_data)

        # EXTRACURRICULARS DATA

        next_idx = generateUniqueID('act_id', 'extracurr')
        extracurriculars_data = [
            (usr_id, next_idx, 'Club A', 'June 1783'),
            (usr_id, next_idx+1, 'Club B', 'August 1939'),
            (usr_id, next_idx+2, 'Club C', 'Febuary 2011'),
            (usr_id, next_idx+3, 'Club D', 'January 2022'),
        ]

        
        # Insert extracurriculars
        cursor.executemany("INSERT INTO extracurr VALUES (?, ?, ?, ?)", extracurriculars_data)

        # TECHNICAL SKILLS DATA

        next_idx = generateUniqueID('skill_id', 'technical_skills')
        technical_skills_data = [
            (usr_id, next_idx, 'Microsoft Office 365'),
            (usr_id, next_idx+1, 'Leadership'),
            (usr_id, next_idx+2, 'Time Management'),
            (usr_id, next_idx+3, 'Customer Service'),
            (usr_id, next_idx+4, 'Problem Solving'),
            (usr_id, next_idx+5, 'Interpersonal Skills'),
            (usr_id, next_idx+6, 'Critical Thnking'),
            (usr_id, next_idx+7, 'Flexibility'),
            (usr_id, next_idx+8, 'Marketing')
        ]

        # Insert technical skills
        cursor.executemany("INSERT INTO technical_skills VALUES (?, ?, ?)", technical_skills_data)

        # Commit changes to the database
        conn.commit()
        conn.close()
    else:
        print("Connection to database failed.")

if __name__ == "__main__":
    
    fill_example_data(5)


