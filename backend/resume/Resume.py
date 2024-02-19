import sqlite3
import json

class Experience:
    def __init__(self, user_id, job_id):
        self.user_id = user_id
        self.job_id = job_id
        self.company = ''
        self.role = ''
        self.start_date = ''
        self.end_date = ''
        self.location = ''
        self.desc_arr = ''

    def setData(self, user_id, job_id, company, role, start_date, end_date, location, desc_arr):
        self.user_id = user_id
        self.job_id = job_id
        self.company = company
        self.role = role
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.desc_arr = desc_arr

    def getDataFromDatabase(self):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM experience WHERE job_id = ?', (self.job_id,))
        result = cursor.fetchone()

        self.company = result[2]
        self.role = result[3]
        self.start_date = result[4]
        self.end_date = result[5]
        self.location = result[6]
        self.desc_arr = result[7]

        conn.close()

    def getData(self):
        return self.user_id, self.job_id, self.company, self.role, self.start_date, self.end_date, self.location, self.desc_arr
    
class Extracurr:
    def __init__(self, user_id, act_id):
        self.user_id = user_id
        self.act_id = act_id
        self.title = ''
        self.desc = ''

    def setData(self, user_id, act_id, title, desc):
        self.user_id = user_id
        self.act_id = act_id
        self.title = title
        self.desc = desc

    def getDataFromDatabase(self):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM extracurr WHERE act_id = ?', (self.act_id,))
        result = cursor.fetchone()

        self.title = result[2]
        self.desc = result[3]

        conn.close()

    def getData(self):
        return self.user_id, self.act_id, self.title, self.desc

class General_Info:
    def __init__(self, user_id):
        self.user_id = user_id
        self.lastname = ''
        self.firstname = ''
        self.phone = -1
        self.email = ''
        self.linkedin = ''
        self.edu = ''
        self.grad_date = ''
        self.major = ''
        self.GPA = 0.0

    def setData(self, user_id, lastname, firstname, phone, email, linkedin, edu, grad_date, major, GPA):
        self.user_id = user_id
        self.lastname = lastname
        self.firstname = firstname
        self.phone = phone
        self.email = email
        self.linkedin = linkedin
        self.edu = edu
        self.grad_date = grad_date
        self.major = major
        self.GPA = GPA

    def getDataFromDatabase(self):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM general_info WHERE usr_id = ?', (self.user_id,))
        result = cursor.fetchone()
        self.lastname = result[1]
        self.firstname = result[2]
        self.phone = result[3]
        self.email = result[4]
        self.linkedin = result[5]
        self.edu = result[6]
        self.grad_date = result[7]
        self.major = result[8]
        self.GPA = result[9]

        conn.close()

    def getData(self):
        return self.user_id, self.lastname, self.firstname, self.phone, self.email, self.linkedin, self.edu, self.grad_date, self.major, self.GPA

class Technical_Skill:
    def __init__(self, user_id, skill_id):
        self.user_id = user_id
        self.skill_id = skill_id
        self.name = ''

    def setData(self, user_id, skill_id, name):
        self.user_id = user_id
        self.skill_id = skill_id
        self.name = name

    def getDataFromDatabase(self):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM technical_skills WHERE skill_id = ?', (self.skill_id,))
        result = cursor.fetchone()
        self.name = result[2]

        conn.close()

    def getData(self):
        return self.user_id, self.skill_id, self.name

class Project:
    def __init__(self, user_id, proj_id):
        self.user_id = user_id
        self.proj_id = proj_id
        self.title = ''
        self.who_for = ''
        self.date = ''
        self.desc_arr = ''

    def setData(self, user_id, proj_id, title, who_for, date, desc_arr):
        self.user_id = user_id
        self.proj_id = proj_id
        self.title = title
        self.who_for = who_for
        self.date = date
        self.desc_arr = desc_arr

    def getDataFromDatabase(self):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM projects WHERE proj_id = ?', (self.proj_id,))
        result = cursor.fetchone()
        self.title = result[2]
        self.who_for = result[3]
        self.date = result[4]
        self.desc_arr = result[5]

        conn.close()

    def getData(self):
        return self.user_id, self.proj_id, self.title, self.who_for, self.date, self.desc_arr

class Award:
    def __init__(self, user_id, award_id):
        self.user_id = user_id
        self.award_id = award_id
        self.title = ''
        self.desc = ''

    def setData(self, user_id, award_id, title, desc):
        self.user_id = user_id
        self.award_id = award_id
        self.title = title
        self.desc = desc

    def getDataFromDatabase(self):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM awards WHERE awd_id = ?', (self.award_id,))
        result = cursor.fetchone()

        self.title = result[2]
        self.desc = result[3]

        conn.close()

    def getData(self):
        return self.user_id, self.award_id, self.title, self.desc

class Course:
    def __init__(self, user_id, course_id):
        self.user_id = user_id
        self.course_id = course_id
        self.name = ''

    def setData(self, user_id, course_id, name):
        self.user_id = user_id
        self.course_id = course_id
        self.name = name

    def getDataFromDatabase(self):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM awards WHERE course_id = ?', (self.course_id,))
        result = cursor.fetchone()
        self.name = result[2]

        conn.close()

    def getData(self):
        return self.user_id, self.course_id, self.name

class Objective:
    def __init__(self, user_id):
        self.user_id = user_id
        self.obj_str = ''
        self.obj_id = -1

    def setData(self, user_id, obj_str,obj_id):
        self.user_id = user_id
        self.obj_str = obj_str
        self.obj_id = obj_id

    def getDataFromDatabase(self):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM awards WHERE usr_id = ?', (self.usr_id,))
        result = cursor.fetchone()

        self.obj_str = result[1]
        self.obj_id = result[2]

        conn.close()

    def getData(self):
        return self.user_id, self.obj_str, self.obj_id

class Volunteer_Work:
    def __init__(self, user_id, vol_id):
        self.user_id = user_id
        self.vol_id = vol_id
        self.company = ''
        self.role = ''
        self.start_date = ''
        self.end_date = ''

    def setData(self, user_id, vol_id, company, role, start_date, end_date):
        self.user_id = user_id
        self.vol_id = vol_id
        self.company = company
        self.role = role
        self.start_date = start_date
        self.end_date = end_date

    def getDataFromDatabase(self):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM awards WHERE usr_id = ?', (self.usr_id,))
        result = cursor.fetchone()

        self.company = result[2]
        self.role = result[3]
        self.start_date = result[4]
        self.end_date = result[5]

        conn.close()

    def getData(self):
        return self.user_id, self.vol_id, self.company, self.role, self.start_date, self.end_date

class Resume:
    def __init__(self):
        self.awards = []
        self.course_work = []
        self.experience = []
        self.extracurr = []
        self.general_info = []
        self.projects = []
        self.volunteer_work = []
        self.technical_skills = []
        self.objective = []

    def getUserInfo(self, id):
        # precondtion: id is an int
        # postcondition: gets user information for resume formatting

        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor() 

        cursor.execute('SELECT COUNT(*) FROM experience WHERE usr_id = ?', (id,))
        result = cursor.fetchone()
        exp_id_exists = result[0] > 0

        cursor.execute('SELECT COUNT(*) FROM extracurr WHERE usr_id = ?', (id,))
        result = cursor.fetchone()
        extracurr_id_exists = result[0] > 0

        cursor.execute('SELECT COUNT(*) FROM general_info WHERE usr_id = ?', (id,))
        result = cursor.fetchone()
        general_id_exists = result[0] > 0

        cursor.execute('SELECT COUNT(*) FROM projects WHERE usr_id = ?', (id,))
        result = cursor.fetchone()
        project_id_exists = result[0] > 0

        cursor.execute('SELECT COUNT(*) FROM technical_skills WHERE usr_id = ?', (id,))
        result = cursor.fetchone()
        tech_id_exists = result[0] > 0

        if exp_id_exists and extracurr_id_exists and general_id_exists and project_id_exists and tech_id_exists:

            # get general info from database
            general_info = General_Info(id)
            general_info.getDataFromDatabase()
            self.general_info.append(general_info)

            # get experience from database; there may be multiple experience entries so we
            # get a list of job ids associated with the same usr_id
            cursor.execute('SELECT job_id FROM experience WHERE usr_id=?', (id,))
            result = cursor.fetchall()
            job_ids = [results[0] for results in result]
            for job_id in job_ids:
                experience = Experience(id, job_id)
                experience.getDataFromDatabase()
                self.experience.append(experience)

            # get extracurriculars from database; there may be multiple extracurricular entries so we
            # get a list of activity ids associated with the same usr_id
            cursor.execute('SELECT act_id FROM extracurr WHERE usr_id=?', (id,))
            result = cursor.fetchall()
            act_ids = [results[0] for results in result]
            for act_id in act_ids:
                extracurr = Extracurr(id, act_id)
                extracurr.getDataFromDatabase()
                self.extracurr.append(extracurr)

            # get projects from database; there may be multiple project entries so we
            # get a list of project ids associated with the same usr_id
            cursor.execute('SELECT proj_id FROM projects WHERE usr_id=?', (id,))
            result = cursor.fetchall()
            project_ids = [results[0] for results in result]
            for project_id in project_ids:
                project = Project(id, project_id)
                project.getDataFromDatabase()
                self.projects.append(project)

            # get technical skills from database; there may be multiple skill entries so we
            # get a list of skill ids associated with the same usr_id
            cursor.execute('SELECT skill_id FROM technical_skills WHERE usr_id=?', (id,))
            result = cursor.fetchall()
            skill_ids = [results[0] for results in result]
            for skill_id in skill_ids:
                technical_skill = Technical_Skill(id, skill_id)
                technical_skill.getDataFromDatabase()
                self.technical_skills.append(technical_skill)

            cursor.execute('SELECT COUNT(*) FROM awards WHERE usr_id = ?', (id,))
            result = cursor.fetchone()
            awards_id_exists = result[0] > 0
            cursor.execute('SELECT COUNT(*) FROM volunteer_work WHERE usr_id = ?', (id,))
            result = cursor.fetchone()
            volunteer_work_id_exists = result[0] > 0
            cursor.execute('SELECT COUNT(*) FROM objective WHERE usr_id = ?', (id,))
            result = cursor.fetchone()
            objective_id_exists = result[0] > 0
            cursor.execute('SELECT COUNT(*) FROM course_work WHERE usr_id = ?', (id,))
            result = cursor.fetchone()
            course_work_id_exists = result[0] > 0

            if awards_id_exists and volunteer_work_id_exists and objective_id_exists and course_work_id_exists:
                # get awards from database; there may be multiple award entries so we
                # get a list of award ids associated with the same usr_id
                cursor.execute('SELECT awd_id FROM awards WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                awd_ids = [results[0] for results in result]
                for awd_id in awd_ids:
                    award = Award(id, awd_id)
                    award.getDataFromDatabase()
                    self.awards.append(award)

                # get volunteer work from database; there may be multiple volunteer entries so we
                # get a list of volunteer ids associated with the same usr_id
                cursor.execute('SELECT vol_id FROM vounteer_work WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                vol_ids = [results[0] for results in result]
                for vol_id in vol_ids:
                    volunteer_work = Volunteer_Work(id, vol_id)
                    volunteer_work.getDataFromDatabase()
                    self.volunteer_work.append(volunteer_work)

                # get course work from database; there may be multiple course entries so we
                # get a list of course ids associated with the same usr_id
                cursor.execute('SELECT course_id FROM course_work WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                course_ids = [results[0] for results in result]
                for course_id in course_ids:
                    course_work = Course_Work(id, course_id)
                    course_work.getDataFromDatabase()
                    self.course_work.append(course_work)

                # get objective statement from database
                objective = Objective(id)
                objective.getDataFromDatabase()
                self.objective.append(objective)

            elif awards_id_exists and volunteer_work_id_exists and objective_id_exists:
                # get awards from database; there may be multiple award entries so we
                # get a list of award ids associated with the same usr_id
                cursor.execute('SELECT awd_id FROM awards WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                awd_ids = [results[0] for results in result]
                for awd_id in awd_ids:
                    award = Award(id, awd_id)
                    award.getDataFromDatabase()
                    self.awards.append(award)

                # get volunteer work from database; there may be multiple volunteer entries so we
                # get a list of volunteer ids associated with the same usr_id
                cursor.execute('SELECT vol_id FROM vounteer_work WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                vol_ids = [results[0] for results in result]
                for vol_id in vol_ids:
                    volunteer_work = Volunteer_Work(id, vol_id)
                    volunteer_work.getDataFromDatabase()
                    self.volunteer_work.append(volunteer_work)

                # get objective statement from database
                objective = Objective(id)
                objective.getDataFromDatabase()
                self.objective.append(objective)

            elif awards_id_exists and volunteer_work_id_exists and course_work_id_exists:
                # get awards from database; there may be multiple award entries so we
                # get a list of award ids associated with the same usr_id
                cursor.execute('SELECT awd_id FROM awards WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                awd_ids = [results[0] for results in result]
                for awd_id in awd_ids:
                    award = Award(id, awd_id)
                    award.getDataFromDatabase()
                    self.awards.append(award)

                # get volunteer work from database; there may be multiple volunteer entries so we
                # get a list of volunteer ids associated with the same usr_id
                cursor.execute('SELECT vol_id FROM vounteer_work WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                vol_ids = [results[0] for results in result]
                for vol_id in vol_ids:
                    volunteer_work = Volunteer_Work(id, vol_id)
                    volunteer_work.getDataFromDatabase()
                    self.volunteer_work.append(volunteer_work)

                # get course work from database; there may be multiple course entries so we
                # get a list of course ids associated with the same usr_id
                cursor.execute('SELECT course_id FROM course_work WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                course_ids = [results[0] for results in result]
                for course_id in course_ids:
                    course_work = Course_Work(id, course_id)
                    course_work.getDataFromDatabase()
                    self.course_work.append(course_work)

            elif awards_id_exists and  objective_id_exists and course_work_id_exists:
                # get awards from database; there may be multiple award entries so we
                # get a list of award ids associated with the same usr_id
                cursor.execute('SELECT awd_id FROM awards WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                awd_ids = [results[0] for results in result]
                for awd_id in awd_ids:
                    award = Award(id, awd_id)
                    award.getDataFromDatabase()
                    self.awards.append(award)

                # get course work from database; there may be multiple course entries so we
                # get a list of course ids associated with the same usr_id
                cursor.execute('SELECT course_id FROM course_work WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                course_ids = [results[0] for results in result]
                for course_id in course_ids:
                    course_work = Course_Work(id, course_id)
                    course_work.getDataFromDatabase()
                    self.course_work.append(course_work)

                # get objective statement from database
                objective = Objective(id)
                objective.getDataFromDatabase()
                self.objective.append(objective)


            elif awards_id_exists and volunteer_work_id_exists:
                # get awards from database; there may be multiple award entries so we
                # get a list of award ids associated with the same usr_id
                cursor.execute('SELECT awd_id FROM awards WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                awd_ids = [results[0] for results in result]
                for awd_id in awd_ids:
                    award = Award(id, awd_id)
                    award.getDataFromDatabase()
                    self.awards.append(award)

                # get volunteer work from database; there may be multiple volunteer entries so we
                # get a list of volunteer ids associated with the same usr_id
                cursor.execute('SELECT vol_id FROM vounteer_work WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                vol_ids = [results[0] for results in result]
                for vol_id in vol_ids:
                    volunteer_work = Volunteer_Work(id, vol_id)
                    volunteer_work.getDataFromDatabase()
                    self.volunteer_work.append(volunteer_work)

            elif awards_id_exists and course_work_id_exists:
                # get awards from database; there may be multiple award entries so we
                # get a list of award ids associated with the same usr_id
                cursor.execute('SELECT awd_id FROM awards WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                awd_ids = [results[0] for results in result]
                for awd_id in awd_ids:
                    award = Award(id, awd_id)
                    award.getDataFromDatabase()
                    self.awards.append(award)

                # get course work from database; there may be multiple course entries so we
                # get a list of course ids associated with the same usr_id
                cursor.execute('SELECT course_id FROM course_work WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                course_ids = [results[0] for results in result]
                for course_id in course_ids:
                    course_work = Course_Work(id, course_id)
                    course_work.getDataFromDatabase()
                    self.course_work.append(course_work)

            elif awards_id_exists and objective_id_exists:
                # get awards from database; there may be multiple award entries so we
                # get a list of award ids associated with the same usr_id
                cursor.execute('SELECT awd_id FROM awards WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                awd_ids = [results[0] for results in result]
                for awd_id in awd_ids:
                    award = Award(id, awd_id)
                    award.getDataFromDatabase()
                    self.awards.append(award)

                # get objective statement from database
                objective = Objective(id)
                objective.getDataFromDatabase()
                self.objective.append(objective)

            elif awards_id_exists:
                # get awards from database; there may be multiple award entries so we
                # get a list of award ids associated with the same usr_id
                cursor.execute('SELECT awd_id FROM awards WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                awd_ids = [results[0] for results in result]
                for awd_id in awd_ids:
                    award = Award(id, awd_id)
                    award.getDataFromDatabase()
                    self.awards.append(award)

            elif volunteer_work_id_exists and objective_id_exists and course_work_id_exists:
                # get volunteer work from database; there may be multiple volunteer entries so we
                # get a list of volunteer ids associated with the same usr_id
                cursor.execute('SELECT vol_id FROM volunteer_work WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                vol_ids = [results[0] for results in result]
                for vol_id in vol_ids:
                    volunteer_work = Volunteer_Work(id, vol_id)
                    volunteer_work.getDataFromDatabase()
                    self.volunteer_work.append(volunteer_work)

                # get course work from database; there may be multiple course entries so we
                # get a list of course ids associated with the same usr_id
                cursor.execute('SELECT course_id FROM course_work WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                course_ids = [results[0] for results in result]
                for course_id in course_ids:
                    course_work = Course_Work(id, course_id)
                    course_work.getDataFromDatabase()
                    self.course_work.append(course_work)

                # get objective statement from database
                objective = Objective(id)
                objective.getDataFromDatabase()
                self.objective.append(objective)

            elif volunteer_work_id_exists and course_work_id_exists:
                # get volunteer work from database; there may be multiple volunteer entries so we
                # get a list of volunteer ids associated with the same usr_id
                cursor.execute('SELECT vol_id FROM vounteer_work WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                vol_ids = [results[0] for results in result]
                for vol_id in vol_ids:
                    volunteer_work = Volunteer_Work(id, vol_id)
                    volunteer_work.getDataFromDatabase()
                    self.volunteer_work.append(volunteer_work)

                # get course work from database; there may be multiple course entries so we
                # get a list of course ids associated with the same usr_id
                cursor.execute('SELECT course_id FROM course_work WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                course_ids = [results[0] for results in result]
                for course_id in course_ids:
                    course_work = Course_Work(id, course_id)
                    course_work.getDataFromDatabase()
                    self.course_work.append(course_work)

            elif volunteer_work_id_exists and objective_id_exists:
                # get volunteer work from database; there may be multiple volunteer entries so we
                # get a list of volunteer ids associated with the same usr_id
                cursor.execute('SELECT vol_id FROM vounteer_work WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                vol_ids = [results[0] for results in result]
                for vol_id in vol_ids:
                    volunteer_work = Volunteer_Work(id, vol_id)
                    volunteer_work.getDataFromDatabase()
                    self.volunteer_work.append(volunteer_work)

                # get objective statement from database
                objective = Objective(id)
                objective.getDataFromDatabase()
                self.objective.append(objective)

            elif volunteer_work_id_exists:
                # get volunteer work from database; there may be multiple volunteer entries so we
                # get a list of volunteer ids associated with the same usr_id
                cursor.execute('SELECT vol_id FROM vounteer_work WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                vol_ids = [results[0] for results in result]
                for vol_id in vol_ids:
                    volunteer_work = Volunteer_Work(id, vol_id)
                    volunteer_work.getDataFromDatabase()
                    self.volunteer_work.append(volunteer_work)

            elif objective_id_exists and course_work_id_exists:
                # get course work from database; there may be multiple course entries so we
                # get a list of course ids associated with the same usr_id
                cursor.execute('SELECT course_id FROM course_work WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                course_ids = [results[0] for results in result]
                for course_id in course_ids:
                    course_work = Course_Work(id, course_id)
                    course_work.getDataFromDatabase()
                    self.course_work.append(course_work)

                # get objective statement from database
                objective = Objective(id)
                objective.getDataFromDatabase()
                self.objective.append(objective)

            elif objective_id_exists:
                # get objective statement from database
                objective = Objective(id)
                objective.getDataFromDatabase()
                self.objective.append(objective)

            elif course_work_id_exists:
                # get course work from database; there may be multiple course entries so we
                # get a list of course ids associated with the same usr_id
                cursor.execute('SELECT course_id FROM course_work WHERE usr_id=?', (id,))
                result = cursor.fetchall()
                course_ids = [results[0] for results in result]
                for course_id in course_ids:
                    course_work = Course_Work(id, course_id)
                    course_work.getDataFromDatabase()
                    self.course_work.append(course_work)
        conn.close()


    def addExperience(self, experience):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor() 

        cursor.execute('INSERT into experience (usr_id, job_id, company, role, start_date, end_date, location, desc_arr) VALUES (?, ?, ?, ?, ?, ?, ?, ?);', 
                        (experience.user_id, experience.job_id, experience.company, experience.role, experience.start_date, experience.end_date, 
                        experience.location, experience.desc_arr))
        conn.commit()
        conn.close()

    def addExtracurr(self, extracurr):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor() 

        cursor.execute('INSERT into extracurr (usr_id, act_id, title, desc_arr) VALUES (?, ?, ?, ?);', 
                        (extracurr.user_id, extracurr.act_id, extracurr.title, extracurr.desc))
        conn.commit()
        conn.close()

    def addGeneralInfo(self, general):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor() 

        cursor.execute('INSERT into general_info (usr_id, lastname, firstname, phone, email, linkedin, edu, grad_date, major, GPA) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', 
                        (general.user_id, general.lastname, general.firstname, general.phone, general.email, general.linkedin, general.edu, general.grad_date, general.major, general.GPA))
        conn.commit()
        conn.close()

    def addTechnicalSkill(self, technicalSkill):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor() 

        cursor.execute('INSERT into technical_skills (usr_id, skill_id, name) VALUES (?, ?, ?);', 
                        (technicalSkill.user_id, technicalSkill.skill_id, technicalSkill.name))
        conn.commit()
        conn.close()

    def addProject(self, project):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor() 

        cursor.execute('INSERT into projects (usr_id, proj_id, title, who_for, date, desc_arr) VALUES (?, ?, ?, ?, ?, ?);', 
                        (project.user_id, project.proj_id, project.title, project.who_for, project.date, project.desc_arr))
        conn.commit()
        conn.close()

    def addAward(self, award):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor() 

        cursor.execute('INSERT into awards (usr_id, awd_id, title, desc) VALUES (?, ?, ?, ?);', 
                        (award.user_id, award.award_id, award.title, award.desc))
        conn.commit()
        conn.close()

    def addCourse(self, course):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor() 

        cursor.execute('INSERT into course_work (usr_id, course_id, name) VALUES (?, ?, ?);', 
                        (course.user_id, course.course_id, course.name))
        conn.commit()
        conn.close()

    def addObjective(self, objective):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor() 

        cursor.execute('INSERT into objective (usr_id, obj_str, obj_id) VALUES (?, ?, ?);', 
                        (objective.user_id, objective.obj_str, objective.obj_id))
        conn.commit()
        conn.close()

    def addVolunteerWork(self, volunteer):
        conn = sqlite3.connect('server/usrDatabase/usrDB.db')  
        cursor = conn.cursor() 

        cursor.execute('INSERT into volunteer_work (usr_id, vol_id, company, role, start_date, end_date) VALUES (?, ?, ?, ?, ?, ?);', 
                        (volunteer.user_id, volunteer.vol_id, volunteer.company, volunteer.role, volunteer.start_date, volunteer.end_date))
        conn.commit()
        conn.close()