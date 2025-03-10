import psycopg2
from app.config import postgresql_config

class PostgreSQL:
    
    #Try to connect to postgreSQL
    def __init__(self):
        try:
            self.__conn = psycopg2.connect(
                host = postgresql_config["HOST"],
                database = postgresql_config["DATABASE"],
                user = postgresql_config["USERNAME"],
                password = postgresql_config["PASSWORD"],
                port = postgresql_config["PORT"] 
            )
        
        except:
            print("\nERRO: can't connect database\n\n")
            exit(1)
            
    @property
    def database(self):
        return self.__conn
    
    @property
    def cursor(self):
        return self.__conn.cursor()
    
    #Execute a query and return if work
    def execute(self, sql):
        try:
            cursor = self.__conn.cursor()
            cursor.execute(sql)
            cursor.close()
            self.__conn.commit()
            
        except Exception as e:
            return False
        
        return True

    #Consult some query and return the results of consult
    def consult(self, sql):
        resp = None
        
        try:
            cursor = self.__conn.cursor()
            cursor.execute(sql)
            resp = cursor.fetchall()
            
        except:           
            return None
        
        return resp
    
    #Close the connection
    def close(self):
        self.__conn.close()