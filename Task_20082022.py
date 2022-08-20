from flask import  Flask , request, jsonify
import mysql.connector as connection
import pymongo

app = Flask(__name__)

@app.route('/sql/insert',methods=['GET' , 'POST'])
def insert_sql():
    '''
    This function is used to insert record in SQL table
    '''
    if(request.method=='POST'):
        db = connection.connect(host="localhost",
                                user="root",
                                passwd="root",
                                db="student")
        cursor = db.cursor()

        Dress_ID   = request.json['Dress_ID']
        Style      = request.json['Style']
        Price      = request.json['Price']
        Rating     = request.json['Rating']
        Size       = request.json['Size']
        Season     = request.json['Season']
        Neckline    = request.json['Neckline']

        Sleevelength = request.json['Sleevelength']

        waiseline   = request.json['waiseline']

        Material    = str(request.json['Material'])

        FabricType  = request.json['FabricType']

        Decoration  = request.json['Decoration']

        PatternTypes = request.json['PatternTypes']

        Recommendation = request.json['Recommendation']


        query = "insert into attribute(Dress_ID,Style,Price,Rating,Size,Season,Neckline,Sleevelength,waiseline,Material,FabricType,Decoration,PatternTypes,Recommendation) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (Dress_ID,Style,Price,Rating,Size,Season,Neckline,Sleevelength,waiseline,Material,FabricType,Decoration,PatternTypes,Recommendation)

        try:
            cursor.execute(query,val)
            db.commit()
            return "Record is inserted successfully"
        except Exception as e:
            print(e)
            return "error occured"



@app.route('/sql/update',methods=['GET' , 'POST'])
def update_sql():
    '''
    This function is used to update record in SQL table
    '''
    if(request.method=='POST'):
        db = connection.connect(host="localhost",
                                user="root",
                                passwd="root",
                                db="student")
        cursor = db.cursor()

        Dress_ID   = request.json['Dress_ID']
        Rating     = request.json['Rating']
        Size       = request.json['Size']

        print(Dress_ID)
        print(Rating)
        print(Size)
        query = "update attribute set Rating = %s, Size=%s where Dress_ID = %s"
        val = (Rating,Size,Dress_ID)
        try:
            cursor.execute(query,val)
            db.commit()
            return "Record is Updated successfully"
        except Exception as e:
            return "Error Occured while updating the record"

@app.route('/sql/delete',methods=['GET' , 'POST'])
def delete_sql():
    '''
    This function is used to delete record in SQL table
    '''
    if(request.method=='POST'):
        db = connection.connect(host="localhost",
                                user="root",
                                passwd="root",
                                db="student")
        cursor = db.cursor()

        Dress_ID   = request.json['Dress_ID']

        query = "delete from attribute where Dress_ID = %s"
        val = (Dress_ID)
        try:
            cursor.execute(query,val)
            db.commit()
            return "Record is Deleted successfully"
        except Exception as e:
            return "Error Occured while Deletion"

@app.route('/sql/select',methods=['GET' , 'POST'])
def select_sql():
    '''
    This function is used to select record from SQL table
    '''
    if(request.method=='POST'):
        db = connection.connect(host="localhost",
                                user="root",
                                passwd="root",
                                db="student")
        cursor = db.cursor()

        Dress_ID   = request.json['Dress_ID']


        query = "select *  from attribute where Dress_ID = %s"
        val = (Dress_ID)
        try:
            cursor.execute(query,val)

            result = cursor.fetchall()

            return jsonify(str(result))
        except Exception as e:
            return "Error Occured while selecting record"

@app.route('/mongo/insert',methods=['GET' , 'POST'])
def insert_mongo():
    '''
    This function is used to insert record in MongoDb
    '''
    if(request.method=='POST'):
        client = pymongo.MongoClient(
            "mongodb+srv://piyush1304:System909@cluster0.gocvn.mongodb.net/?retryWrites=true&w=majority")
        db = client['test1234']
        coll = db['apiattribute']

        Dress_ID   = request.json['Dress_ID']
        Style      = request.json['Style']
        Price      = request.json['Price']
        Rating     = request.json['Rating']
        Size       = request.json['Size']
        Season     = request.json['Season']
        Neckline    = request.json['Neckline']

        Sleevelength = request.json['Sleevelength']

        waiseline   = request.json['waiseline']

        Material    = request.json['Material']

        FabricType  = request.json['FabricType']

        Decoration  = request.json['Decoration']

        PatternTypes = request.json['PatternTypes']

        Recommendation = request.json['Recommendation']

        my_dict = {
            "Dress_ID ":Dress_ID ,
            "Style" : Style,
            "Price":Price,
            "Rating":Rating,
            "Size":Size,
            "Season" :Season,
            "Neckline":Neckline,
            "Sleevelength":Sleevelength,
            "waiseline":waiseline,
            "Material":Material,
            "FabricType":FabricType,
            "Decoration":Decoration,
            "PatternTypes":PatternTypes,
            "Recommendation":Recommendation
        }
        try:
            coll.insert_one(my_dict)
            return "record inserted successfully in mongodb"
        except:
            return "Error Occured while inserting in Mongodb"

@app.route('/mongo/update',methods=['GET' , 'POST'])
def update_mongo():
    '''
    This function is used to update record in Mongodb
    '''
    if(request.method=='POST'):
        client = pymongo.MongoClient(
            "mongodb+srv://piyush1304:System909@cluster0.gocvn.mongodb.net/?retryWrites=true&w=majority")
        db = client['test1234']
        coll = db['apiattribute']

        Rating     = request.json['Rating']
        Size = request.json['Size']
        try:
            coll.update_one({'Rating':Rating},{'$set':{'Size':Size}})
            return "record updated successfully in mongodb"
        except:
            return "error occured"

@app.route('/mongo/delete',methods=['GET' , 'POST'])
def delete_mongo():
    '''
    This function is used to delete record in MongoDb
    '''
    if(request.method=='POST'):
        client = pymongo.MongoClient(
            "mongodb+srv://piyush1304:System909@cluster0.gocvn.mongodb.net/?retryWrites=true&w=majority")
        db = client['test1234']
        coll = db['apiattribute']

        Style   = request.json['Style']

        try:
            coll.delete_one({"Style":Style})
            return "record deleted  successfully in mongodb"
        except Exception as e:
            return "Error occured while deletion from Mongodb"

@app.route('/mongo/select',methods=['GET' , 'POST'])
def select_mongo():
    '''
    This function is used to select record from MongoDb
    '''
    if(request.method=='POST'):
        client = pymongo.MongoClient(
            "mongodb+srv://piyush1304:System909@cluster0.gocvn.mongodb.net/?retryWrites=true&w=majority")
        db = client['test1234']
        coll = db['apiattribute']

        Style   = request.json['Style']

        try:
            result = coll.find({"Style":Style})
            mydict = {}
            j = 0
            for i in result:
                mydict[j] = str(i)
                j = j + 1
            return mydict
        except Exception as e:
            return "Error occured while selecting records from MongoDb"

if __name__ =="__main__":
    app.run()