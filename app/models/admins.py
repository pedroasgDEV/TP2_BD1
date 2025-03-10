from app.utils.connectDB import PostgreSQL

class Admins:
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
            AND table_name = 'admins';
        '''
        
        result = self.__postgre.consult(sql)
        
        if result is None or len(result) < 1: return False
        else: return True
        
    #insert data from a json
    def insert(self, doc):
        sql = f'''
            INSERT INTO admins 
            (name, email, passwrd, derp)
            VALUES 
            ('{doc["name"]}', '{doc["email"]}', '{doc["passwrd"]}', '{doc["derp"]}');
        '''
        
        if self.__postgre.execute(sql) is False: return False
            
        sql = f'''
            SELECT id FROM admins WHERE email = '{doc['email']}';
        '''
        
        result = self.__postgre.consult(sql)
        return int(result[0][0])
    
    #select by id
    def select(self, id):
        sql = f'''
            SELECT * FROM admins
            WHERE id = {id};
        '''
        
        result = self.__postgre.consult(sql)
        
        if result is None or len(result) < 1: return False
        else:
            adm = {
                "id": int(result[0][0]),
                "name": result[0][1],
                "email": result[0][2],
                "passwrd": result[0][3],
                "derp": result[0][4]
            }
            
            return adm
        
    #select all
    def select_all(self):
        sql = f'''
            SELECT * FROM admins;
        '''
        
        results = self.__postgre.consult(sql)
        adms = []
        
        if results is None or len(results) < 1: return False
        else:
            for result in results:
                adm = {
                    "id": int(result[0]),
                    "name": result[1],
                    "email": result[2],
                    "passwrd": result[3],
                    "derp": result[4]
                }
                
                adms.append(adm)
                
            return adms
    
    #update data
    def update(self, id, doc):
        upd = ""
        for index in doc:
            upd += f"{index} = '{doc[index]}', "
            
        upd = upd[:-2]
        
        sql = f'''
            UPDATE admins
            SET {upd}
            WHERE id = {id};
        '''
        
        if self.__postgre.execute(sql) is False: return False
        else: return True
    
    #delet data
    def delete(self, id):
        sql = f'''
            DELETE FROM admins
            WHERE id = {id};
        '''
        
        if self.__postgre.execute(sql) is False: return False
        else: return True
    
    def login(self, doc):
        sql = f'''
            SELECT * FROM admins
            WHERE email = '{doc['email']}'
            AND passwrd = '{doc['passwrd']}';
        '''
        
        result = self.__postgre.consult(sql)
            
        if result is None or len(result) < 1: return False
        else: 
            adm = {
                "id": result[0][0],
                "name": result[0][1],
                "email": result[0][2],
                "passwrd": result[0][3],
                "derp": result[0][4]
            }
            
            return adm
    
    #close db
    def close(self):
        self.__postgre.close()