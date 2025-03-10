from app.utils.connectDB import PostgreSQL

class Subjects:
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
            AND table_name = 'subjects';
        '''
        
        result = self.__postgre.consult(sql)
        
        if result is None or len(result) != 1: return False
        else: return True
        
    #insert data from a json
    def insert(self, doc):
        sql = f'''
            INSERT INTO subjects 
            (subject_code, name, professor, derp)
            VALUES 
            ('{doc["subject_code"]}', '{doc["name"]}', '{doc["professor"]}', '{doc["derp"]}');
        '''
        
        return self.__postgre.execute(sql)
        
    #select by subject_code
    def select(self, subject_code):
        sql = f'''
            SELECT * FROM subjects
            WHERE subject_code = '{subject_code}';
        '''
        
        result = self.__postgre.consult(sql)
        
        if result is None or len(result) < 1: return False
        else: 
            sbj = {
                "subject_code": result[0][0],
                "name": result[0][1],
                "professor": result[0][2],
                "derp": result[0][3]
            }
            
            return sbj
        
    #select all
    def select_all(self):
        sql = f'''
            SELECT * FROM subjects;
        '''
        
        results = self.__postgre.consult(sql)
        subs = []
        
        if results is None or len(results) < 1: return False
        else:
            for result in results:
                sub = {
                    "subject_code": result[0][0],
                    "name": result[0][1],
                    "professor": result[0][2],
                    "derp": result[0][3]
                }
                
                subs.append(sub)
                
            return subs
    
    #update data
    def update(self, subject_code, doc):
        
        upd = ""
        for index in doc:
            upd += f"{index} = '{doc[index]}', "
            
        upd = upd[:-2]
        
        sql = f'''
            UPDATE subjects
            SET {upd}
            WHERE subject_code = '{subject_code}';
        '''
        
        return self.__postgre.execute(sql)
    
    #delet data
    def delete(self, subject_code):
        sql = f'''
            DELETE FROM subjects
            WHERE subject_code = '{subject_code}';
        '''
        
        return self.__postgre.execute(sql)
    
    #close db
    def close(self):
        self.__postgre.close()