import sqlite3


def connect_to_database():
    try:
        conn = sqlite3.connect('/root/StuHQ/server/usrDatabase/usrDB.db')
        return conn
    except sqlite3.Error as e:
        print("Error connecting to database:", e)
        return None

# Define custom classes to store resume data
class Experience:
    def __init__(self, usr_id, job_id, company, role, start_date, end_date, location, desc_arr):
        self.usr_id = usr_id
        self.job_id = job_id
        self.company = company
        self.role = role
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.desc_arr = desc_arr

    def print_info(self):
        print("Experience:")
        print("usr_id:", self.usr_id)
        print("job_id:", self.job_id)
        print("company:", self.company)
        print("role:", self.role)
        print("start_date:", self.start_date)
        print("end_date:", self.end_date)
        print("location:", self.location)
        print("desc_arr:", self.desc_arr)
        print()

class Extracurricular:
    def __init__(self, usr_id, act_id, title, desc_arr):
        self.usr_id = usr_id
        self.act_id = act_id
        self.title = title
        self.desc_arr = desc_arr

    def print_info(self):
        print("Extracurricular:")
        print("usr_id:", self.usr_id)
        print("act_id:", self.act_id)
        print("title:", self.title)
        print("desc_arr:", self.desc_arr)
        print()

class GeneralInfo:
    def __init__(self, usr_id, lastname, firstname, phone, email, linkedin, edu, grad_date, major, GPA):
        self.usr_id = usr_id
        self.lastname = lastname
        self.firstname = firstname
        self.phone = phone
        self.email = email
        self.linkedin = linkedin
        self.edu = edu
        self.grad_date = grad_date
        self.major = major
        self.GPA = GPA

    def print_info(self):
        print("General Info:")
        print("usr_id:", self.usr_id)
        print("lastname:", self.lastname)
        print("firstname:", self.firstname)
        print("phone:", self.phone)
        print("email:", self.email)
        print("linkedin:", self.linkedin)
        print("edu:", self.edu)
        print("grad_date:", self.grad_date)
        print("major:", self.major)
        print("GPA:", self.GPA)
        print()

class Project:
    def __init__(self, usr_id, proj_id, title, who_for, date, desc_arr):
        self.usr_id = usr_id
        self.proj_id = proj_id
        self.title = title
        self.who_for = who_for
        self.date = date
        self.desc_arr = desc_arr

    def print_info(self):
        print("Project:")
        print("usr_id:", self.usr_id)
        print("proj_id:", self.proj_id)
        print("title:", self.title)
        print("who_for:", self.who_for)
        print("date:", self.date)
        print("desc_arr:", self.desc_arr)
        print()

class TechnicalSkill:
    def __init__(self, usr_id, skill_id, name):
        self.usr_id = usr_id
        self.skill_id = skill_id
        self.name = name

    def print_info(self):
        print("Technical Skill:")
        print("usr_id:", self.usr_id)
        print("skill_id:", self.skill_id)
        print("name:", self.name)
        print()

# Connect to the SQLite database



# Function to retrieve data from a table and return a list of objects
def fetch_data(table_name, obj_class):
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    data = cursor.fetchall()
    objects = []
    for row in data:
        objects.append(obj_class(*row))

    cursor.close()
    return objects

def clear_table(cursor, table_name):
    cursor.execute(f"DELETE FROM {table_name}")

def fill_example_data():
    conn = connect_to_database()  
    if conn:
        cursor = conn.cursor()
        # Example data for Howie DeWitt
        cursor.execute("SELECT COUNT(*) FROM usr_info WHERE usr_id = 1")
        user_count = cursor.fetchone()[0]
        if user_count == 0:
            # If user does not exist, insert into the table
            cursor.execute("INSERT INTO usr_info (usr_id, username, pswd_hash, usr_email, created_epoch) VALUES (?, ?, ?, ?, ?)",
                           (1, 'example_user', 'example_hash', 'example@example.com', 0))  # Replace with actual data
            conn.commit()
            print("User with usr_id 1 inserted successfully.")
        else:
            print("User with usr_id 1 already exists.")
        
        # GEN INFO

        howie_info = (1, 'DeWitt', 'Howie', 1234567890, 'howie@example.com', 'linkedin.com/howie', 'BSc Computer Science', '2023-05-15', 'Computer Science', 3.80)

        # Insert general info
        clear_table(cursor, 'general_info')
        cursor.execute("INSERT INTO general_info VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", howie_info)

        
        # PROJ DATA


        projects_data = [
            (1, 1, 'Project A', 'Company A', '2022-08-01', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),
            (1, 2, 'Project B', 'Company B', '2023-02-15', 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
        ]

        # Insert projects
        clear_table(cursor, 'projects')
        cursor.executemany("INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?)", projects_data)

        # EXPERIENCE DATA


        experiences_data = [
            (1, 1, 'Company X', 'Software Engineer', '2020-01-01', '2021-06-30', 'New York', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),
            (1, 2, 'Company Y', 'Data Analyst', '2021-09-01', '2022-12-31', 'San Francisco', 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
        ]

        # Insert job experiences
        clear_table(cursor, 'experience')
        cursor.executemany("INSERT INTO experience VALUES (?, ?, ?, ?, ?, ?, ?, ?)", experiences_data)

        # EXTRACURRICULARS DATA


        extracurriculars_data = [
            (1, 1, 'Club A', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'),
            (1, 2, 'Club B', 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'),
            (1, 3, 'Club C', 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.')
        ]

        
        # Insert extracurriculars
        clear_table(cursor, 'extracurr')
        cursor.executemany("INSERT INTO extracurr VALUES (?, ?, ?, ?)", extracurriculars_data)

        # TECHNICAL SKILLS DATA


        technical_skills_data = [
            (1, 1, 'Python'),
            (1, 2, 'Java'),
            (1, 3, 'SQL'),
            (1, 4, 'JavaScript'),
            (1, 5, 'HTML'),
            (1, 6, 'CSS'),
            (1, 7, 'Git'),
            (1, 8, 'Data Analysis')
        ]

        # Insert technical skills
        clear_table(cursor, 'technical_skills')
        cursor.executemany("INSERT INTO technical_skills VALUES (?, ?, ?)", technical_skills_data)

        # Commit changes to the database
        conn.commit()
        conn.close()
    else:
        print("Connection to database failed.")



# Call the function to fill example data




if __name__ == "__main__":
    fill_example_data()
    
   
    experiences = fetch_data('experience', Experience)
    for exp in experiences:
        exp.print_info()
    extracurriculars = fetch_data('extracurr', Extracurricular)
    for ext in extracurriculars:
        ext.print_info()
    general_infos = fetch_data('general_info', GeneralInfo)
    for gi in general_infos:
        gi.print_info()
    projects = fetch_data('projects', Project)
    for proj in projects:
        proj.print_info()
    technical_skills = fetch_data('technical_skills', TechnicalSkill)
    for ts in technical_skills:
        ts.print_info()

    # Close the database connection

