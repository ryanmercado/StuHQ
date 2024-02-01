from pylatex import Document, Section, Subsection, Command, NewPage, NoEscape
from pylatex.utils import bold
from pylatex.basic import SmallText
from datetime import date

# Create a new LaTeX document
doc = Document()

# Define document title and author
doc.preamble.append(Command('title', 'My Resume'))
doc.preamble.append(Command('author', 'John Doe'))
doc.append(NoEscape(r'\maketitle'))

# Add a section for personal information
with doc.create(Section('Personal Information')):
    doc.append('Name: John Doe\n')
    doc.append('Address: 123 Main St, Anytown, USA\n')
    doc.append('Phone: (555) 555-5555\n')
    doc.append('Email: john.doe@example.com\n')
    doc.append('Date of Birth: ' + date.today().strftime("%B %d, %Y") + '\n')

# Add a section for work experience
with doc.create(Section('Work Experience')):
    with doc.create(Subsection('Software Engineer')):
        doc.append(bold('Company XYZ, 2020 - Present'))
        doc.append('\n')
        doc.append(' - Developed software applications\n')
        doc.append(' - Managed a team of developers\n')

    with doc.create(Subsection('Web Developer')):
        doc.append(bold('Company ABC, 2018 - 2020'))
        doc.append('\n')
        doc.append(' - Designed and developed websites\n')
        doc.append(' - Collaborated with clients to meet project requirements\n')

# Add a section for education
with doc.create(Section('Education')):
    with doc.create(Subsection('Bachelor of Science in Computer Science')):
        doc.append(bold('University of XYZ, 2014 - 2018'))
        doc.append('\n')
        doc.append(' - Relevant coursework in computer science\n')
        doc.append(' - Graduated with honors\n')

# Save the LaTeX document to a file
doc.generate_pdf('my_resume', clean_tex=False, compiler='pdflatex')

print('LaTeX document generated and saved as my_resume.pdf')

# from pylatex import Document, Section, Command, NoEscape

# # Create a Document instance
# doc = Document()

# # Add metadata to your document
# doc.preamble.append(Command('title', 'My Custom LaTeX Document'))
# doc.preamble.append(Command('author', 'Your Name'))
# doc.append(NoEscape(r'\maketitle'))

# # Create sections and add content to your LaTeX document
# with doc.create(Section('Introduction')):
#     doc.append('This is the introduction section.')

# with doc.create(Section('Section 2')):
#     doc.append('This is another section.')

# # Generate the PDF document
# pdf_file = 'my_document.pdf'
# doc.generate_pdf(pdf_file, compiler='pdflatex')

# print(f'PDF generated and saved as {pdf_file}')

