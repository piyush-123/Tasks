# Sample 10 inheritences

import logging

class logrec:

    def __init__(self,filename,level,format):
        self.filename = filename
        self.level = level
        self.format = format
        logging.basicConfig(filename=self.filename,
                            level=self.level,
                            format=self.format)

    def log(self,message,method):
        '''
                    logging the message based on the method
                    passed in this function
                    in the file
        '''
        if method == 'INFO':
            logging.info(message)
        else:
            logging.error(message)

class ineuron:

    def __init__(self):
        self.student_count = 1000
        self.logger_list = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')
    def student_welcome(self):
        '''
        this method is used to register the students on ineuron
        courses
        '''

        try:
                self.logger_list.log("Welcome Student", "INFO")
                message = "Hi Students ,welcome to ineuron"
                return message

        except Exception as e:
            self.logger_list.log("Exception happened while registration", "ERROR")

    def student_total(self):
        '''
        this method is used to return the id of student
        '''

        try:
                self.logger_list.log("fetching total count of Student", "INFO")

                return self.student_count

        except Exception as e:
            self.logger_list.log("Exception happened in fetching student count", "ERROR")

class oneNeuron(ineuron):

    def __init__(self,neuron_cost,neuron_type):
        self.neuron_cost = neuron_cost
        self.neuron_type = neuron_type
        self.student_count = 1000
        self.logger_list = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')
        self.logger_oneNeuron = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')
    def neuron_register(self):
        '''
        this method is used to create the type of neurons on one neuron
        '''

        try:
                self.logger_oneNeuron.log("Creating new neuron type on one neuron portal", "INFO")
                message = "New type of  neuron is created "
                self.logger_oneNeuron.log("Neuron is created ", "INFO")
                return message


        except Exception as e:
            self.logger_oneNeuron.log("Creating Neuron failed.Please have a look", "ERROR")

    def neuron_costing(self,neuron_type):
        '''
        this method is used to return the cost of neuron type
        '''

        try:
                self.logger_oneNeuron.log("Cost determination started for a neuron", "INFO")
                cost = self.neuron_cost
                self.logger_oneNeuron.log("Cost of neuron is returned now ", "INFO")
                return cost

        except Exception as e:
            self.logger_oneNeuron.log("Exception happened while calculating cost", "ERROR")


# Creating objects of different classes

o = oneNeuron(9900,"new_type")
print(o.student_welcome())
print("Total student counts are ",o.student_total())
print(o.neuron_register())
print("Cost of tech neuron is ",o.neuron_costing("tech"))

class techNeuron:

    def __init__(self):
        self.logger_techNeuron = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')
    def course_list(self,instructor_name):
        '''
        this method is used to return the list of courses for a particular
        instructor
        '''

        try:
                self.logger_techNeuron.log("Creating list of courses for an instructor", "INFO")
                opt_list = ["Full Stack JavaScript ","C","React"]
                self.logger_techNeuron.log("Course list is created and returned ", "INFO")
                return opt_list

        except Exception as e:
            self.logger_techNeuron.log("Creating course list encountered problem", "ERROR")

    def course_cost(self,course_name):
        '''
        this method is used to return the cost of a course
        '''

        try:
                self.logger_techNeuron.log("Cost determination started for a course", "INFO")
                cost = 17700
                self.logger_techNeuron.log("Cost of course is returned now ", "INFO")
                return cost

        except Exception as e:
            self.logger_techNeuron.log("Exception happened while calculating cost of the course", "ERROR")

class instructor(techNeuron):

    def __init__(self,instructor_name,instructor_age,instructor_skills):
        self.instructor_name= instructor_name
        self.instructor_age = instructor_age
        self.instructor_skills = instructor_skills
        self.logger_techNeuron = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')
        self.logger_instructor = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')
    def instructor_registration(self):
        '''
        this method is used to register the instructor in ineuron
        '''

        try:
                self.logger_instructor.log("Starting registration of  an instructor", "INFO")
                result = "Hi, You are registered as an instructor "
                self.logger_instructor.log("Instructor registration process is done ", "INFO")
                return result

        except Exception as e:
            self.logger_instructor.log("Instructor Registration encountered problem", "ERROR")

    def instructor_skills_update(self,skills):
        '''
        this method is used to update the skills of an instructor
        '''

        try:
                self.logger_instructor.log("Instructor skills is being updated", "INFO")
                self.instructor_skills = skills
                self.logger_instructor.log("Instructor skills are updated ", "INFO")
                return "Hi , Your skills are updated"

        except Exception as e:
            self.logger_instructor.log("Updating Instructor Skill process failed","ERROR")


ins = instructor("krishna",31,"C,C++,Core Java")
print("course list Instructor rahul teaches are ",ins.course_list("rahul"))
print("Cost of the Datascience Course in tech Neuron is ",ins.course_cost("data science"))
print(ins.instructor_registration())
print(ins.instructor_skills_update("data_science"))

class courses:
    def __init__(self,main_course_name,sub_course_name):
        self.main_course_name = main_course_name
        self.sub_course_name = sub_course_name
        self.logger_courses = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')
    def new_course_creation(self):
        '''
                this method is used to create a new sub course in main
                course in ineuron portal
        '''

        try:
            self.logger_courses.log("Starting creation of a new sub course", "INFO")
            result = "New sub course is created and registered"
            self.logger_courses.log("Sub Course registration process is completed ", "INFO")
            return result

        except Exception as e:
            self.logger_courses.log("Course Registration failed", "ERROR")

    def sub_course_count(self,main_course_name):
        '''
                this method is used to return the count of  sub courses in main
                course in ineuron portal
        '''

        try:
            self.logger_courses.log("Starting counting of  sub courses", "INFO")
            count = 11
            self.logger_courses.log("Sub Course count process is completed ", "INFO")
            return count

        except Exception as e:
            self.logger_courses.log("Sub Course Count process is failed", "ERROR")
    def sub_course_deletion(self,sub_course_name):
        '''
                this method is used to delete a new sub course in main
                course in ineuron portal
        '''

        try:
            self.logger_courses.log("Starting deletion of a new sub course", "INFO")
            count = 10
            self.logger_courses.log("Sub Course deletion process is completed ", "INFO")
            return count

        except Exception as e:
            self.logger_courses.log("Sub Course Deletion process failed", "ERROR")

class student(courses):
    def __init__(self,student_name,student_mob,student_email,student_password,main_course_name,sub_course_name):
        super().__init__(main_course_name,sub_course_name)
        self.student_name = student_name
        self.student_mob = student_mob
        self.student_email = student_email
        self.student_password = student_password
        self.logger_courses = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')
        self.logger_student = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')

    def student_registration(self):
        '''
                 this method is used to register a new student in
                 ineuron portal
         '''

        try:
            self.logger_student.log("Registering the Student", "INFO")
            bool = False
            if not bool:
                result = "student is registered"
            else:
                result = "student is already present"
            self.logger_student.log("Student Registration process is completed ", "INFO")
            return result

        except Exception as e:
            self.logger_courses.log("Student Registration failed", "ERROR")

    def student_mobile_update(self,mob,student_name):
        '''
                 this method is used to update the mobile number of student in
                 ineuron portal
         '''

        try:
            self.logger_student.log("Updating the Mobile number of Student", "INFO")

            if student_name:
                self.mob = mob
                result = "Mobile number is updated"
            else:
                result = "student is not  present"
            self.logger_student.log("Mobile Number updation process is completed ", "INFO")
            return result

        except Exception as e:
            self.logger_courses.log("Mobile Update process failed", "ERROR")


s = student("ram",9876556789,"ram@gmail.com","121212","Data Science","Python Programming")
print(s.new_course_creation())
print("Now the total subcourses under data science are ",s.sub_course_count("data science"))
print("After deleting, total subcourses under data science are ",s.sub_course_deletion("Data Analytics"))
print(s.student_registration())
print("Hi Ram your ",s.student_mobile_update(9876543345,"ram"))

class blog:
    def __init__(self):
        self.logger_blog = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')

    def blog_creation(self,blog_type,blog_title,blog_content):
            '''
                     this method is used to store the blog in
                     database
             '''

            try:
                self.logger_blog.log("Creating the blog", "INFO")
                blog_id = 10
                self.logger_blog.log("Blog is stored successfully ", "INFO")
                return blog_id

            except Exception as e:
                self.logger_blog.log("Blog Registration failed", "ERROR")

    def blog_types(self):
            '''
                     this method is used to return the different types of blog in
                     database
             '''

            try:
                self.logger_blog.log("Fetching the blog types", "INFO")
                opt = ['BigData','Blockchain','DataSciene']
                self.logger_blog.log("Blog types list is prepared ", "INFO")
                return opt

            except Exception as e:
                self.logger_blog.log("Error while fetching the blog types", "ERROR")

class affiliate(instructor):
    def __init__(self,instructor_name,instructor_age,instructor_skills):
        super().__init__(instructor_name,instructor_age,instructor_skills)
        self.logger_affiliate = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')
        self.logger_instructor = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')
    def bank_update(self,account_number,accountholdername,ifsccode,pancard):
        '''
                 this method is used to update the bank details to become
                  the affiliate member in ineuron
         '''

        try:
            self.logger_affiliate.log("Updating the bank details", "INFO")
            update = [account_number,accountholdername,ifsccode,pancard]
            message = "Account updated"
            self.logger_affiliate.log("Account updated successfully ", "INFO")
            return message

        except Exception as e:
            self.logger_affiliate.log("Please try Again later!! Account did not get updated", "ERROR")

    def create_affiliate_eligible(self,name):
        '''
                 this method is used to check if affiliate can be created in ineuron
         '''

        try:
            self.logger_affiliate.log("Starting the affiliation process", "INFO")
            if False:
                message = "Yes"

            else:
                message = "No"
            self.logger_affiliate.log("Affiliation verified ", "INFO")
            return message

        except Exception as e:
            self.logger_affiliate.log("Error Encountered during affiliation check", "ERROR")

afl = affiliate("krishna",31,"C,C++,Core Java")
print(ins.instructor_registration())
print("Is krishna eligible for affiliation ",afl.create_affiliate_eligible("krishna"))
print("Affiliation is ready for krishna as ",afl.bank_update(121214212,"krishna","icici000999","ggcdefghi"))

class jobs:
    def __init__(self):
        self.logger_jobs = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')


    def jobs_search(self,job_type):
        '''
        this method is used to search the jobs of a particular job type
        '''

        try:
            self.logger_jobs.log("Starting the searching of jobs for given job type", "INFO")
            if job_type == 'Contract':
                opt =  ['Data Scientist at flipkart',
                        'data analyst at cognizant']
            elif job_type == 'Full time':
                opt = 'Full TIme'
            else:
                opt = 'Part time'

            self.logger_jobs.log("List generated for given job type ", "INFO")
            return opt

        except Exception as e:
            self.logger_jobs.log("Please try Again later!! Not Able to get the job list", "ERROR")

class contact:
    def __init__(self):
        self.logger_contact = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')

    def create_query(self,name,email_address,mob,message,type):
        '''
         this method is used to create the query for ineuron
         '''

        try:
            self.logger_contact.log("Storing the query", "INFO")
            query = [name,email_address,mob,message,type]
            opt = 'Query Created'
            self.logger_contact.log("Query created ", "INFO")
            return opt

        except Exception as e:
            self.logger_contact.log("Error while creating query. Please check", "ERROR")

class library:

    def __init__(self):
        self.logger_lib = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')

    def lib_courses(self):
        '''
          this method is used to return the courses present in library
          '''

        try:
            self.logger_lib.log("Fetching the courses from library", "INFO")

            opt = ['Blockchain Community Class',
                       'Javascript Marathon']

            self.logger_lib.log("List generated for courses ", "INFO")
            return opt

        except Exception as e:
            self.logger_lib.log("Please try Again later!! Not Able to get the course list", "ERROR")

class lib_neuron(library,ineuron):
    def __init__(self):
        self.student_count = 1000
        self.logger_list = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')
        self.logger_lib = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')

class blog_jobs(blog,jobs):
    def __init__self(self):
        self.logger_jobs = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')
        self.logger_blog = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')

    def test12(self):
        self.blog_creation('data analytics','data analytics','quite easy')

class language:
    def __init__(self):
        self.logger_lang = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')
    def language_types(self):
        '''
               this method is used to return the languages of courses
               '''

        try:
            self.logger_lang.log("Returning the course kanguages", "INFO")
            opt = ['English','Hindi']
            self.logger_lang.log("List created for languages ", "INFO")
            return opt

        except Exception as e:
            self.logger_lang.log("Error while getting languages. Please check", "ERROR")

    def add_language(self,lang):
        '''
                    this method is used to add the new  languages of courses
                    '''

        try:
            self.logger_lang.log("Creating the course languages", "INFO")
            opt = ['German']
            self.logger_lang.log("New Language created for course ", "INFO")
            return "Language Created"

        except Exception as e:
            self.logger_lang.log("Error while creating new languages. Please check", "ERROR")

class lang_neuron(language,techNeuron):
    def __init__(self):
        self.logger_lang = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')
        self.logger_techNeuron = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')
    def new_method(self):
        '''
                           this method is used to verify the tech neuron courses language
                           '''

        try:
            self.logger_lang.log("Verifying the techneuron languages", "INFO")
            opt = self.language_types()
            op1 = self.course_list("krishna")
            self.logger_lang.log("Languages verified ", "INFO")
            return "Language are Verified"

        except Exception as e:
            self.logger_lang.log("Error while verifying languages. Please check", "ERROR")

ln = lang_neuron()
print(ln.new_method())
bj = blog_jobs()
bj.test12()

ln = lib_neuron()
print(ln.student_welcome())

blg = blog()
print("blog is created with id as ", blg.blog_creation('data science','welcome to data science','its easy to learn'))
print("Different blog types are ", blg.blog_types())



jbs = jobs()

print("Contract jobs are : ", jbs.jobs_search("Contract"))

cnt = contact()
print(cnt.create_query("ram","ram@gmail.com",9876543345,"hi when i can join batch","Course Enquiry"))
