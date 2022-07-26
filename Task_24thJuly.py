import logging
import mysql.connector as connection
import pandas as pd
import pymongo
import json

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

class sql_admin:
    def __init__(self):
        self.logger_list = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')

    def create_connection(self):
        '''
            this method is used to connect to MYSQL
            server.
        '''
        try:
            self.logger_list.log("Establishing the SQL Connection ", "INFO")
            sql_connection = connection.connect(host="localhost", user="root", passwd="root",database="student")
            self.logger_list.log("SQL Connection has been established ", "INFO")

            return sql_connection
        except Exception as e:
            self.logger_list.log("There is some SQL connection error,Please check ", "INFO")


    def create_table(self,sql_connection):
        '''
            this method is used to create the SQL tables
        '''
        try:
            self.logger_list.log("Creating the tables if not present ", "INFO")
            query = "create table if not exists student.attribute(Dress_ID int(20),Style varchar(20),Price varchar(20),Rating decimal(3,2),Size varchar(10),Season varchar(20),Neckline varchar(30),Sleevelength varchar(30),waiseline varchar(30),Material varchar(30),FabricType varchar(30),Decoration varchar(30),PatternTypes varchar(30),Recommendation int(1))"
            cursor = sql_connection.cursor()
            cursor.execute(query)
            query = "create table if not exists student.dress(Dress_id int(20),col1_Aug29 int(20),col2_Aug31 int(20),col3_Sep2 int(20),col4_Sep4 int(20),col5_Sep6 int(20),col6_Sep8 int(20),col7_Sep10 int(20),col8_Sep12 int(20),col9_Sep14 int(20),col10_Sep16 int(20),col11_Sep18 int(20),col12_Sep20 int(20),col13_Sep22 int(20),col14_Sep24 int(20),col15_Sep26 int(20),col16_Sep28 int(20),col17_Sep30 int(20),col18_Oct2 int(20),col19_Oct4 int(20),col20_Oct6 int(20),col21_Oct8 int(20),col22_Oct10 int(20),col23_Oct12 int(20))"
            cursor1 = sql_connection.cursor()
            cursor1.execute(query)
            self.logger_list.log(" Tables have been created ", "INFO")
        except:
            self.logger_list.log("SQL Error while creating the table,Please check ", "INFO")
            cursor.close()
            cursor1.close()

class tables_population:
    def __init__(self):
        self.logger_list = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')

    def insert_table(self,sql_connection):
        '''
            this method is used to bulk insert the records in tables
        '''
        try:
            self.logger_list.log("Bulk Inserting the records in tables ", "INFO")
            query = "LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Attribute DataSet.csv'  into Table student.attribute FIELDS TERMINATED BY ',' IGNORE 1 LINES"
            cursor2 = sql_connection.cursor()
            cursor2.execute(query)
            query = "LOAD DATA LOCAL INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Dress Sales.csv'  into Table student.dress FIELDS TERMINATED BY ',' IGNORE 1 LINES"
            cursor3 = sql_connection.cursor()
            cursor3.execute(query)

            self.logger_list.log("Bulk Insertion has been completed", "INFO")


        except Exception as e:
            self.logger_list.log("Error in bulk Insertion Process,Please check ", "INFO")

class dataframe_oper:

    def __init__(self):
        self.logger_list = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')

    def read_dataframe(self,sql_connection):
        '''
            this method is used to read the records from tables as pandas dataframe
        '''
        try:
            self.logger_list.log("Reading the records from tables in dataframes ", "INFO")
            query = "Select * from attribute"
            cursor = sql_connection.cursor()
            cursor.execute(query)
            opt = cursor.fetchall()
            df_attribute = pd.DataFrame(opt)
            query = "Select * from dress"
            cursor5 = sql_connection.cursor()
            cursor5.execute(query)
            opt = cursor.fetchall()
            df_dress = pd.DataFrame(opt)


            self.logger_list.log("Reading Data in dataframe has been completed", "INFO")
            return df_attribute



        except Exception as e:
            print(e)
            self.logger_list.log("Error in reading dataframe Process,Please check ", "INFO")

    def convert_to_json(self,df):
        '''
            this method is used to convert the format in json
        '''
        try:
            self.logger_list.log("Converting the dataframe in json format ", "INFO")
            output_json = df.to_json()


            self.logger_list.log("JSON conversion has been completed", "INFO")
            return output_json


        except Exception as e:
            self.logger_list.log("Error in JSON conversion Process,Please check ", "INFO")

class mongo_oper:

    def __init__(self):
        self.logger_list = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')

    def mongo_connection(self):
        '''
            this method is used to connect to mongo db
        '''
        try:
            self.logger_list.log("Connecting the Mongo db client ", "INFO")
            client = pymongo.MongoClient("mongodb+srv://piyush1304:System909@cluster0.gocvn.mongodb.net/?retryWrites=true&w=majority")

            self.logger_list.log("Mongo DB connected successfully", "INFO")

            return client


        except Exception as e:
            self.logger_list.log("Error in connecting mongodb,Please check ", "INFO")

    def mongo_data_load(self,client,opt_json):
        '''
            this method is used to store the data in mongodb database
        '''
        try:
            self.logger_list.log("Storing the data in mongodb ", "INFO")
            database1 = client['task_attribute']
            collection1 = database1['data_attribute']
            collection1.insert_many(json.loads(opt_json).values())
            self.logger_list.log("Mongo DB data storage has been completed", "INFO")


        except Exception as e:
            print(e)
            self.logger_list.log("Error in storing data in mongodb database,Please check ", "INFO")

class sql_oper:

    def __init__(self):
        self.logger_list = logrec('log_file.txt', 'INFO', '%(levelname)s %(asctime)s %(name)s %(message)s')

    def sql_query_one(self,sql_connection):
        '''
            this method is used to fire the left join operation between attribute and dress tables
        '''
        try:
            self.logger_list.log("Executing the Left join query on Attribute and dress table ", "INFO")
            query = "Select A.Dress_Id,A.style,A.price,A.RAting,A.Size,A.Season,A.Neckline from attribute A LEFT JOIN dress D on A.Dress_ID = D.Dress_ID"
            cursor = sql_connection.cursor()
            cursor.execute(query)
            opt = cursor.fetchall()
            self.logger_list.log("Results are returned from left join on attribute and dress table ", "INFO")
            return opt

        except Exception as e:
            self.logger_list.log("Error in executing the left join query,Please check ", "INFO")

    def sql_query_two(self,sql_connection):
        '''
            this method is used to determine the unique dresses based on dress id
        '''
        try:
            self.logger_list.log("Determining the unique dresses based on dress id ", "INFO")
            query = "Select Distinct Dress_ID from attribute "
            cursor = sql_connection.cursor()
            cursor.execute(query)
            opt = cursor.fetchall()
            self.logger_list.log("Unique dresses are returned ", "INFO")
            return opt

        except Exception as e:
            self.logger_list.log("Error in determining the unique dresses,Please check ", "INFO")

    def sql_query_three(self,sql_connection):
        '''
            this method is used to determine count of dresses with recommendation as 0
        '''
        try:
            self.logger_list.log("Determining the dresses for zero recommendation ", "INFO")
            query = "Select count(distinct Dress_ID) from attribute where Recommendation = 0 "
            cursor = sql_connection.cursor()
            cursor.execute(query)
            opt = cursor.fetchall()
            self.logger_list.log("Zero recommended dresses are returned ", "INFO")
            return opt

        except Exception as e:
            self.logger_list.log("Error in determining the dresses for zero recommendation,Please check ", "INFO")


    def sql_query_four(self,sql_connection):
        '''
            this method is used to determine total dress sell for individual dress id
        '''
        try:
            self.logger_list.log("Determining the total dress sell for individual dress id  ", "INFO")
            query = "select Dress_id,(col1_Aug29+col2_Aug31+col3_Sep2+col4_Sep4+col5_Sep6+col6_Sep8+col7_Sep10+col8_Sep12+col9_Sep14+col10_Sep16+col11_Sep18+col12_Sep20+col13_Sep22+col14_Sep24+col15_Sep26+col16_Sep28+col17_Sep30+col18_Oct2+col19_Oct4+col20_Oct6+col21_Oct8+col22_Oct10+col23_Oct12) as total from dress group by Dress_id "
            cursor = sql_connection.cursor()
            cursor.execute(query)
            opt = cursor.fetchall()
            self.logger_list.log("Total dress sales for each dress id are returned ", "INFO")
            return opt

        except Exception as e:
            self.logger_list.log("Error in determining the total dress sell for individual dress id ,Please check ", "INFO")


    def sql_query_five(self,sql_connection):
        '''
            this method is used to determine third highest most selling dress id
        '''
        try:
            self.logger_list.log("Determining the third highest most selling dress id   ", "INFO")
            query = "select Dress_Id from (select Dress_id,(col1_Aug29+col2_Aug31+col3_Sep2+col4_Sep4+col5_Sep6+col6_Sep8+col7_Sep10+col8_Sep12+col9_Sep14+col10_Sep16+col11_Sep18+col12_Sep20+col13_Sep22+col14_Sep24+col15_Sep26+col16_Sep28+col17_Sep30+col18_Oct2+col19_Oct4+col20_Oct6+col21_Oct8+col22_Oct10+col23_Oct12) as total from dress group by Dress_id order by total desc LIMIT 1 Offset 2) as t"
            cursor = sql_connection.cursor()
            cursor.execute(query)
            opt = cursor.fetchall()
            self.logger_list.log("Third highest most selling dress id is returned ", "INFO")
            return opt

        except Exception as e:
            self.logger_list.log("Error in determining the third highest most selling dress id  ,Please check ", "INFO")


sa = sql_admin()
sql_connection = sa.create_connection()
sa.create_table(sql_connection)

print("Tables have been created Successfully..")
tp = tables_population()
tp.insert_table(sql_connection)

print("Tables have been loaded Successfully..")
do = dataframe_oper()
df = do.read_dataframe(sql_connection)
opt_json = do.convert_to_json(df)
print("Dataframes have been created")

mo = mongo_oper()
client = mo.mongo_connection()
mo.mongo_data_load(client,opt_json)

so = sql_oper()
result1 = so.sql_query_one(sql_connection)
result2 = so.sql_query_two(sql_connection)
result3 = so.sql_query_three(sql_connection)
result4 = so.sql_query_four(sql_connection)
result5 = so.sql_query_five(sql_connection)







