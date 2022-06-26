import pymysql

class Connection:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.passwd = '2202'
        self.database = 'passmanagerDb1'
        self.mydb = ''
        self.created = False
      
    def connection(self):
        try:
            if self.created == False:
                self.mydb = pymysql.connect(host=self.host,user=self.user,passwd=self.passwd)
                cursor = self.mydb.cursor()
                cursor.execute("CREATE DATABASE IF NOT EXISTS passmanagerDb1")
                cursor.execute("use passmanagerDb1")
                cursor.execute("create table IF NOT EXISTS login(name VARCHAR(255),password VARCHAR(255))")
                self.created = True
            else:
                self.mydb = pymysql.connect(host=self.host,user=self.user,passwd=self.passwd,database=self.database)
        except:
            print("No Connection")
    def fetch_all(self):
        data = []
        cursor = self.mydb.cursor()
        query = "select * from login"
        try:
            cursor.execute(query)
            data = cursor.fetchall()
        except:
            print("Could not execute query")
        
        
        return data
    def fetch_data(self,query):
        data = []
        cursor = self.mydb.cursor()

        try:
            cursor.execute(query)
            data = cursor.fetchall()
        except:
            print("Could not execute query")
        
        
        return data
    def insert_data(self,query,val):
        cursor = self.mydb.cursor()
        try:
            cursor.execute(query,val)
            self.mydb.commit()
        except:
            print("could not execute query")




