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

class profile:

        __id = 10
        __name = "raman"

        def __init__(self):
            self.logger_profile = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')

        def profile_id(self):
            '''
            This method is used to return the profile id
            '''
            try:
                self.logger_profile.log("returning the profile id", "INFO")
                return profile.__id
            except:
                self.logger_profile.log("Error while returning the id", "ERROR")
        def profile_name(self):
            '''
            This method is used to return the profile name
            '''
            try:
                self.logger_profile.log("returning the profile name", "INFO")
                return profile.__name
            except:
                self.logger_profile.log("Error while returning the name", "ERROR")

p = profile()
print("profile id is " , p._profile__id)
print("profile name is ",p._profile__name)
print(p.profile_id())
print(p.profile_name())

class categories:
         _types= ['Data Analytics','Data Science','Development']
         count = 3

         def __init__(self):
             self.logger_cat = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')

         def __categories_count(self):
             '''
             This method is used to return the categories count
             '''
             try:
                 self.logger_cat.log("returning the categories count", "INFO")
                 return self.count
             except:
                 self.logger_cat.log("Error while returning the categories count", "ERROR")
         def categories_types(self):
             '''
             This method is used to return the categories types
             '''
             try:
                 self.logger_cat.log("returning the categories types", "INFO")
                 return self._types
             except:
                 self.logger_cat.log("Error while returning the categories types", "ERROR")

c= categories()
print("category count is ",c.count)
print("category types are ",c._types)


class Subtopics:

    def __init__(self):
        self.names = ['Deep Learning','Full Stack Data Science','Machine Learning']
        self.filter = True
        self.logger_subt = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')
    def subtopics_list(self):
        '''
                     This method is used to return the subtopics list
        '''
        try:
            self.logger_subt.log("returning the subtopics list", "INFO")
            return self.names
        except:
            self.logger_subt.log("Error while returning the subtopics list", "ERROR")

    def _subtopics_count(self):
        '''
                      This method is used to return the subtopics count
         '''
        try:
            self.logger_subt.log("returning the subtopics count", "INFO")
            if self.filter:
                return 3
            else:
                return 10
        except Exception as e:
            self.logger_subt.log("Error while returning the subtopics count", "ERROR")

st = Subtopics()
print("Subtopics names are :",st.names)
st.names = "Data Maniplulation"
print("subtopics list is ",st.subtopics_list())



class Instructors:

    def __init__(self):
        self.instructors_name= ['Ankur Khanna','Sunny','Anurag']
        self.__score = 0
        self.logger_inst = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')


    def instructor_scores(self):
        '''
        this method is used to return the instructor score
        '''
        try:
            self.logger_inst.log("returning the instructor scores", "INFO")
            if  'Ankur' in self.instructors_name:
                Instructors.__score = 90
            else:
                Instructors.__score = 100
            return Instructors.__score
        except Exception as e:
            self.logger_inst.log("Error while returning the instruction score", "ERROR")


    def _List_instructors(self):
        '''
          this method is used to return the instructor list
          '''
        try:
            self.logger_inst.log("returning the instructor list", "INFO")
            return self.instructors_name
        except Exception as e:
            self.logger_inst.log("Error while returning the instruction list", "ERROR")
ins = Instructors()

print("Default Instructor score is " , ins._Instructors__score)
print("Updated Instructor score is " , ins.instructor_scores())
print("Instructors are ", ins._List_instructors())

class course_card:



    def __init__(self):
        self.name = 'Sanjeevan'
        self._coursename = 'BlockChain Community Class'
        self.logger_cc = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')

    def define_course(self):
        '''
              this method is used to return the course name
        '''
        try:
            self.logger_cc.log("returning the course name", "INFO")
            return self._coursename

        except Exception as e:
            self.logger_cc.log("Error while returning the course name", "ERROR")

    def course_update(self,coursename_new):
        '''
            this method is used to update the course name
        '''
        try:
            self.logger_cc.log("updating the course name", "INFO")
            self._coursename = coursename_new

        except Exception as e:
            self.logger_cc.log("Error while updating the course name", "ERROR")

cc = course_card()
print("instructor name is ", cc.name)
print("course name is ", cc._coursename)
cc.course_update("machine learning")
print("updated course name is ", cc._coursename)


class enrolled_courses:
    _enrolled_course_count = 0

    def __init__(self,profile_id):
        self.profile_id = profile_id
        self.logger_ec = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')

    def enr_courses(self):
        '''
                this method is used to return the enrolled courses
          '''
        try:
            self.logger_ec.log("returning the enrolled courses", "INFO")
            enrolled_course = ['Full Stack Data Science']
            return enrolled_course

        except Exception as e:
            self.logger_ec.log("Error while returning the enrolled course name", "ERROR")

    def enr_courses_count(self):
        '''
                this method is used to return the enrolled courses count
          '''
        try:
            self.logger_ec.log("returning the count of enrolled courses", "INFO")
            self._enrolled_course_count = self._enrolled_course_count + 1
            return self._enrolled_course_count

        except Exception as e:
            self.logger_ec.log("Error while returning the enrolled course count", "ERROR")

ec = enrolled_courses(10)
print("enrolled courses are :",ec.enr_courses())
print("enrolled course count is ",ec.enr_courses_count())
ec._enrolled_course_count = 9
print("updated enrolled course count is ",ec.enr_courses_count())


class instructor:
    __instructor_count = 0

    def __init__(self,instructor_name,instructor_skills):
        self.instructor_name= instructor_name
        self._instructor_skills = instructor_skills
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

    def instructor_count_update(self):
        '''
        this method is used to update the count of an instructor
        '''

        try:
                self.logger_instructor.log("Instructor count is being updated", "INFO")
                instructor.__instructor_count = instructor.__instructor_count  + 1
                self.logger_instructor.log("Instructor count is updated ", "INFO")

        except Exception as e:
            self.logger_instructor.log("Updating Instructor count process failed","ERROR")

ins = instructor("sham","machine learning")
print(ins.instructor_registration())
print("initial count  is ",ins._instructor__instructor_count)
ins.instructor_count_update()
print("updated count is ",ins._instructor__instructor_count)

ins1 = instructor("sham","machine learning")
ins1.instructor_count_update()
print("updated count is ",ins1._instructor__instructor_count)

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

crs = courses("test1","ds")
print(crs.new_course_creation())


class student:

    __student_id = 99
    def __init__(self,student_name,student_mob,student_email,student_password):
        self.student_name = student_name
        self.student_mob = student_mob
        self.student_email = student_email
        self.student_password = student_password
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

class blog:
    def __init__(self):
        self.blog_count = 10
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

blg = blog()
print(blg.blog_count)





