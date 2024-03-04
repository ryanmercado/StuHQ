import sqlite3
import pytest
from flask import Flask

# Define a mock Flask app for testing
def create_test_app():
    app = Flask(__name__)
    return app

# Use this function to create a mock Flask app
app = create_test_app()

@pytest.fixture(scope='module')
def app_client():
    with app.app_context():
        yield app.test_client()

@pytest.fixture
def clear_db_fixture():
    clearDB()
    yield

@pytest.fixture
def user_exists_fixture():
    add_user()
    yield

@pytest.fixture
def experience_entry_fixture():
    add_experience_entry()

@pytest.fixture
def extracurr_entry_fixture():
    add_extracurr_entry()

@pytest.fixture
def generalInfo_entry_fixture():
    add_generalInfo_entry()

@pytest.fixture
def technicalSkill_entry_fixture():
    add_technicalSkill_entry()

@pytest.fixture
def project_entry_fixture():
    add_project_entry()

@pytest.fixture
def award_entry_fixture():
    add_award_entry()

@pytest.fixture
def course_entry_fixture():
    add_course_entry()

@pytest.fixture
def objective_entry_fixture():
    add_objective_entry()

@pytest.fixture
def volunteer_entry_fixture():
    add_volunteer_entry()

def clear_db():
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usr_info')
    cursor.execute('DELETE FROM grocery_list')
    cursor.execute('DELETE FROM recipes')
    cursor.execute('DELETE FROM curr_stock')
    conn.commit()
    cursor.close()
    conn.close()

def add_user():
    clear_db()
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usr_info (usr_id, username, pswd_hash, usr_email, created_epoch) VALUES (?, ?, ?, ?, ?)', (0, 'gray', 'hash', 'g@email.com', 1))
    conn.commit()
    cursor.close()
    conn.close()

def add_experience_entry():
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('INSERT into experience (usr_id, job_id, company, role, start_date, end_date, location, desc_arr) VALUES (?, ?, ?, ?, ?, ?, ?, ?);', 
                    (1, 1, "TI", "SWE", "01/01/2021", "01/30/2022", "Dallas, TX", "Coded some stuff"))
    conn.commit()
    cursor.close()
    conn.close()

def add_extracurr_entry():
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('INSERT into extracurr (usr_id, act_id, title, desc_arr) VALUES (?, ?, ?, ?);', 
                    (1, 1, "Basketball", "Averaged 30 ppg"))
    conn.commit()
    cursor.close()
    conn.close()

def add_generalInfo_entry():
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('INSERT into general_info (usr_id, lastname, firstname, phone, email, linkedin, edu, grad_date, major, GPA) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', 
                    (1, "Abramson", "Owen", 2142508672, "owenabramson@yahoo.com", "owenabramson", "University of Texas", "05/10/2024", "ECE", 3.90))
    conn.commit()
    cursor.close()
    conn.close()

def add_technicalSkill_entry():
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('INSERT into technical_skills (usr_id, skill_id, name) VALUES (?, ?, ?);', 
                    (1, 1, "Java"))
    conn.commit()
    cursor.close()
    conn.close()

def add_project_entry():
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('INSERT into projects (usr_id, proj_id, title, who_for, date, desc_arr) VALUES (?, ?, ?, ?, ?, ?);', 
                    (1, 1, "Video Game", "University of Texas", "03/22/2021", "Programmed a game"))
    conn.commit()
    cursor.close()
    conn.close()

def add_award_entry():
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('INSERT into awards (usr_id, awd_id, title, desc) VALUES (?, ?, ?, ?);', 
                    (1, 1, "Best Student", "I was the best student"))
    conn.commit()
    cursor.close()
    conn.close()

def add_course_entry():
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('INSERT into course_work (usr_id, course_id, name) VALUES (?, ?, ?);', 
                    (1, 1, "Computer Vision"))
    conn.commit()
    cursor.close()
    conn.close()

def add_objective_entry():
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('INSERT into objective (usr_id, obj_str, obj_id) VALUES (?, ?, ?);', 
                    (1, "I want to be the best engineer ever", 1))
    conn.commit()
    cursor.close()
    conn.close()

def add_volunteer_entry():
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('INSERT into volunteer_work (usr_id, vol_id, company, role, start_date, end_date) VALUES (?, ?, ?, ?, ?, ?);', 
                    (1, 1, "YMSL", "Secretary", "02/21/2021", "05/30/2022"))
    conn.commit()
    cursor.close()
    conn.close()


# START OF EXPERIENCE TESTS
def test_add_experience(user_exists_fixture, experience_entry_fixture): #add experience (user exists, 1 experience entry exists in DB already)
    resume = Resume()
    resume.addExperience(1, "Dell", "SWE", "03/22/2022", "07/24/2024", "Austin, TX", "Was a software engineer")
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM experience WHERE usr_id = ?', (1, ))
    res = cursor.fetchall()
    assert(res[0][1] != res[1][1])  # check that job_ids are unique
    assert(res[0][2] == "TI")       # check names of companies in entries
    assert(res[1][2] == "Dell")

def test_add_experience2(user_exists_fixture): #add experience (user exists, 0 experience entries exists in DB already)
    resume = Resume()
    resume.addExperience(1, "Dell", "SWE", "03/22/2022", "07/24/2024", "Austin, TX", "Was a software engineer")
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM experience WHERE usr_id = ?', (1, ))
    res = cursor.fetchone()
    assert(res[2] == "Dell")                # check name of company in entries

# START OF EXTRACURR TESTS
def test_add_extracurr(user_exists_fixture, extracurr_entry_fixture): #add extracurr (user exists, 1 extracurr entry exists in DB already)
    resume = Resume()
    resume.addExtracurr(1, "Video Games", "Played Fortnite")
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM extracurr WHERE usr_id = ?', (1, ))
    res = cursor.fetchall()
    assert(res[0][1] != res[1][1])          # check that act_ids are unique
    assert(res[0][2] == "Basketball")       # check names of activities in entries
    assert(res[1][2] == "Video Games")

def test_add_extracurr2(user_exists_fixture): #add experience (user exists, 0 extracurr entries exists in DB already)
    resume = Resume()
    resume.addExtracurr(1, "Video Games", "Played Fortnite")
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM extracurr WHERE usr_id = ?', (1, ))
    res = cursor.fetchall()
    assert(res[0][2] == "Video Games")      # check name of activity in entry

# START OF GENERAL INFO TESTS
def test_add_generalInfo(user_exists_fixture, generalInfo_entry_fixture): #add generalInfo (user exists, 1 general_info entry exists in DB already)
    resume = Resume()
    try:
        resume.addGeneralInfo(1, "Drinkard", "Grayson", 2142535672, "gdrinkard@yahoo.com", "gdrinkard", "University of Texas", "05/10/2024", "ECE", 3.90)
        error = 0
    except sqlite3.IntegrityError as e:
        error = 1
    finally:
        # Close the database connection
        assert(error == 1)                    # test that there is an error when making entry with same PK

def test_add_generalInfo2(user_exists_fixture): #add generalInfo (user exists, 0 general_info entries exists in DB already)
    resume = Resume()
    resume.addGeneralInfo(1, "Drinkard", "Grayson", 2142535672, "gdrinkard@yahoo.com", "gdrinkard", "University of Texas", "05/10/2024", "ECE", 3.90)
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM general_info WHERE usr_id = ?', (1, ))
    res = cursor.fetchone()
    assert(res[1] == "Drinkard")             # check name of person in entry

# START OF TECHNICAL SKILL TESTS
def test_add_technicalSkill(user_exists_fixture, technicalSkill_entry_fixture): #add technical skill (user exists, 1 technical skill entry exists in DB already)
    resume = Resume()
    resume.addTechnicalSkill(1, "Python")
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM technical_skills WHERE usr_id = ?', (1, ))
    res = cursor.fetchall()
    assert(res[0][1] != res[1][1])          # check that skill_ids are unique
    assert(res[0][2] == "Java")             # check names of skills in entries
    assert(res[1][2] == "Python")

def test_add_technicalSkill2(user_exists_fixture): # add technical skill (user exists, 0 technical skill entries exist in DB already)
    resume = Resume()
    resume.addTechnicalSkill(1, "Python")
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM technical_skills WHERE usr_id = ?', (1, ))
    res = cursor.fetchone()
    assert(res[2] == "Python")             # check name of skill in entry

# START OF PROJECT TESTS
def test_add_project(user_exists_fixture, project_entry_fixture): #add project (user exists, 1 project entry exists in DB already)
    resume = Resume()
    resume.addProject(1, "StuHQ", "University of Texas", "04/19/2023", "Student Hub App")
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM projects WHERE usr_id = ?', (1, ))
    res = cursor.fetchall()
    assert(res[0][1] != res[1][1])          # check that proj_ids are unique
    assert(res[0][2] == "Video Game")       # check names of projects in entries
    assert(res[1][2] == "StuHQ")

def test_add_project2(user_exists_fixture): #add project (user exists, 0 project entries exist in DB already)
    resume = Resume()
    resume.addProject(1, "StuHQ", "University of Texas", "04/19/2023", "Student Hub App")
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM projects WHERE usr_id = ?', (1, ))
    res = cursor.fetchone()
    assert(res[2] == "StuHQ")               # check name of project

# START OF AWARD TESTS
def test_add_award(user_exists_fixture, award_entry_fixture): #add award (user exists, 1 award entry exists in DB already)
    resume = Resume()
    resume.addAward(1, "College Scholar", "Top 20 percent of class")
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM awards WHERE usr_id = ?', (1, ))
    res = cursor.fetchall()
    assert(res[0][1] != res[1][1])          # check that awd_ids are unique
    assert(res[0][2] == "Best Student")     # check names of awards in entries
    assert(res[1][2] == "College Scholar")

def test_add_award2(user_exists_fixture, award_entry_fixture): #add award (user exists, 0 award entries exist in DB already)
    resume = Resume()
    resume.addAward(1, "College Scholar", "Top 20 percent of class")
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM awards WHERE usr_id = ?', (1, ))
    res = cursor.fetchone()
    assert(res[2] == "College Scholar")  # check name of award in entry

# START OF COURSE TESTS
def test_add_course(user_exists_fixture, course_entry_fixture): #add course (user exists, 1 course entry exists in DB already)
    resume = Resume()
    resume.addCourse(1, "SWArch")
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM course_work WHERE usr_id = ?', (1, ))
    res = cursor.fetchall()
    assert(res[0][1] != res[1][1])          # check that course_ids are unique
    assert(res[0][2] == "Computer Vision")  # check names of courses in entries
    assert(res[1][2] == "SWArch")

def test_add_course2(user_exists_fixture): #add course (user exists, 0 course entries exist in DB already)
    resume = Resume()
    resume.addCourse(1, "SWArch")
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM course_work WHERE usr_id = ?', (1, ))
    res = cursor.fetchone()
    assert(res[2] == "SWArch")           # check name of course in entry

# START OF OBJECTIVE TESTS
def test_add_objective(user_exists_fixture, objective_entry_fixture): #add objective (user exists, 1 objective entry exists in DB already)
    resume = Resume()
    resume.addObjective(1, "I want to be a great student")
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM objective WHERE usr_id = ?', (1, ))
    res = cursor.fetchall()
    assert(res[0][2] != res[1][2])                              # check that obj_ids are unique
    assert(res[0][1] == "I want to be the best engineer ever")  # check objectives in entries
    assert(res[1][1] == "I want to be a great student")

def test_add_objective2(user_exists_fixture): #add objective (user exists, 0 objective entries exist in DB already)
    resume = Resume()
    resume.addObjective(1, "I want to be a great student")
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM objective WHERE usr_id = ?', (1, ))
    res = cursor.fetchone()
    assert(res[1] == "I want to be a great student")        # check objective in entry

# START OF VOLUNTEER WORK TESTS
def test_add_volunteerWork(user_exists_fixture, volunteer_entry_fixture_entry_fixture): #add volunteer work (user exists, 1 volunteer work entry exists in DB already)
    resume = Resume()
    resume.addVolunteerWork(1, "Food Bank", "Food Collector", "02/23/2023", "05/14/2023")
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM volunteer_work WHERE usr_id = ?', (1, ))
    res = cursor.fetchall()
    assert(res[0][1] != res[1][1])                              # check that vol_ids are unique
    assert(res[0][2] == "YMSL")                                 # check companies in entries
    assert(res[1][2] == "Food Bank")

def test_add_volunteerWork2(user_exists_fixture): #add volunteer work (user exists, 0 volunteer work entries exist in DB already)
    resume = Resume()
    resume.addVolunteerWork(1, "Food Bank", "Food Collector", "02/23/2023", "05/14/2023")
    conn = sqlite3.connect('server/usrDatabase/usrDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM volunteer_work WHERE usr_id = ?', (1, ))
    res = cursor.fetchone()
    assert(res[2] == "Food Bank")                               # check companies in entry
