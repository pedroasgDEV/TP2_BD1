from app.utils.connectDB import PostgreSQL

class UsrSub:
    def __init__(self):
        #connect the database 
        self.__postgre = PostgreSQL()
        
        if not self.__table_check(): raise Exception("ERRO: Table not exists")

    
    #check if the table exists
    def __table_check(self):
        
        sql = '''  
            SELECT * 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name = 'user_subjects';
        '''
        
        result = self.__postgre.consult(sql)
        
        if result is None or len(result) < 1: return False
        else: return True
        
    #insert data from a json
    def insert(self, user_id, subject_code):
        sql = f'''
            INSERT INTO user_subjects 
            (user_id, subject_code)
            VALUES 
            ('{user_id}', '{subject_code}');
        '''
        
        return self.__postgre.execute(sql)
        
    #Verify if the connection exists
    def verify(self, user_id, subject_code):
        sql = f'''
            SELECT * FROM user_subjects
            WHERE user_id = '{user_id}'
            AND subject_code = '{subject_code}';
        '''
        
        result = self.__postgre.consult(sql)
        
        if result is None or len(result) < 1: return False
        else: return True
        
    #select all Admins
    def select_all_users(self, subject_code):
        sql = f'''
            SELECT *
            FROM users usr
            JOIN user_subjects usrsub ON usr.regis_id = usrsub.user_id
            WHERE usrsub.subject_code = '{subject_code}';
        '''
        
        results = self.__postgre.consult(sql)
        usrs = []
        
        if results is None or len(results) < 1: return False
        else:
            for result in results:
                usr = {
                    "regis_id": result[0],
                    "name": result[1],
                    "email": result[2],
                    "passwrd": result[3],
                    "course": result[4]
                }
                
                usrs.append(usr)
                
            return usrs
        
    #select all Subjects
    def select_all_subjects(self, user_id):
        sql = f'''
            SELECT *
            FROM subjects sub
            JOIN user_subjects usrsub ON sub.subject_code = usrsub.subject_code
            WHERE usrsub.user_id = '{user_id}';
        '''
        
        results = self.__postgre.consult(sql)
        subs = []
        
        if results is None or len(results) < 1: return False
        else:
            for result in results:
                sub = {
                    "subject_code": result[0],
                    "name": result[1],
                    "professor": result[2],
                    "derp": result[3]
                }
                
                subs.append(sub)
                
            return subs
    
    #delet data
    def delete(self, user_id, subject_code):
        sql = f'''
            DELETE FROM user_subjects
            WHERE user_id = '{user_id}'
            AND subject_code = '{subject_code}';
        '''
        
        if self.__postgre.execute(sql) is False: return False
        else: return True
    
    #close db
    def close(self):
        self.__postgre.close()