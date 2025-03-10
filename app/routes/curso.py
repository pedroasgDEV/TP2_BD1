from utils.connectDB import PostgreSQL

class Curso:
    def __init__(self):
        #connect the database 
        self.__postgre = PostgreSQL()
        
        if not self.curso_table_check(): raise Exception("ERRO: Table not exists")

    
    #check if the table curso exists
    def curso_table_check(self):
        
        sql = '''  
            SELECT * 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            AND table_name = 'Curso';
        '''
        
        result = self.__postgre.consult(sql)
        
        if result is None or len(result) < 1: return False
        else: return True
        
    #insert data from a json
    def insert(self, curso_json):
        sql = f'''
            INSERT INTO Curso 
            (admin_id, subject_code)
            VALUES 
            ({curso_json}, '{subject_code}');
        '''
        
        return self.__postgre.execute(sql)
        
    #Verify if the connection exists
    def verify(self, admin_id, subject_code):
        sql = f'''
            SELECT * FROM admin_subjects
            WHERE admin_id = {admin_id}
            AND subject_code = '{subject_code}';
        '''
        
        result = self.__postgre.consult(sql)
        
        if result is None or len(result) < 1: return False
        else: return True
        
    #select all Admins
    def select_all_admins(self, subject_code):
        sql = f'''
            SELECT *
            FROM admins adm
            JOIN admin_subjects admsub ON adm.id = admsub.admin_id
            WHERE admsub.subject_code = '{subject_code}';
        '''
        
        results = self.__postgre.consult(sql)
        adms = []
        
        if results is None or len(results) < 1: return False
        else:
            for result in results:
                adm = {
                    "id": result[0],
                    "name": result[1],
                    "email": result[2],
                    "passwrd": result[3],
                    "derp": result[4]
                }
                
                adms.append(adm)
                
            return adms
        
    #select all Subjects
    def select_all_subjects(self, admin_id):
        sql = f'''
            SELECT *
            FROM subjects sub
            JOIN admin_subjects admsub ON sub.subject_code = admsub.subject_code
            WHERE admsub.admin_id = {admin_id};
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
    def delete(self, admin_id, subject_code):
        sql = f'''
            DELETE FROM admin_subjects
            WHERE admin_id = {admin_id}
            AND subject_code = '{subject_code}';
        '''
        
        if self.__postgre.execute(sql) is False: return False
        else: return True
    
    #close db
    def close(self):
        self.__postgre.close()