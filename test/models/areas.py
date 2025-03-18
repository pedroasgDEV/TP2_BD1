from test.utils.connectDB import PostgreSQL

class Areas:
    def __init__(self):
        #connect the database 
        self.__postgre = PostgreSQL()
        
        if not self.__table_check(): raise Exception("ERRO: Table not exists")

    
    #check if the table exists
    def __table_check(self):
        
        sql = '''  
            SELECT COUNT(*) 
            FROM information_schema.tables
            WHERE table_schema = 'public'
            AND table_name IN ('curso', 'area_interesse', 'area_do', 'professor_titular', 'se_interessa');
        '''
        
        result = self.__postgre.consult(sql)
        print()
        
        if result is None or result[0][0] != 5: return False
        else: return True
        
    #insert data from a json
    def insert(self, json):

        try:
            #Insert area_interesse amd get the id
            sql = f'''
                    INSERT INTO area_interesse 
                    (nome, descricao)
                    VALUES 
                    ('{json["nome"]}', '{json["descricao"]}')
                    RETURNING id;
                '''
            
            area_id = self.__postgre.execute(sql)[0][0]
        
            #Insert area_do per Curso 
            for curso in json["curso"]:
                sql = f'''
                        INSERT INTO area_do
                        (id, codigo)
                        VALUES ({area_id}, {curso});
                    '''
                self.__postgre.execute(sql)
        except:
            return False
        
        self.__postgre.database.commit()
        return area_id

    #Get All data
    def get_all(self):
        sql = '''
            SELECT ai.id, c.nome AS nome_curso, ai.nome, ai.descricao,
                   COUNT(pt.cpf) AS qnt_professores
            FROM area_interesse ai
            JOIN area_do ad ON ai.id = ad.id
            JOIN curso c ON ad.codigo = c.codigo
            LEFT JOIN se_interessa si ON ai.id = si.id
            LEFT JOIN professor_titular pt ON si.cpf = pt.cpf
            GROUP BY ai.id, c.nome, ai.nome, ai.descricao;
        '''
        
        result = self.__postgre.consult(sql)

        if result is None:
            return None

        areas = {"areas": []}
        for row in result:
            areas["areas"].append({
                "id": row[0],
                "nome_curso": row[1],
                "nome": row[2],
                "descricao": row[3],
                "qnt_professores": row[4]
            })

        return areas

    #Update data
    def update(self, area_id, json):

        update_fields = []

        try:
            #Update each field in json
            if "nome" in json:
                update_fields.append(f"nome = '{json["nome"]}'")

            if "descricao" in json:
                update_fields.append(f"descricao = '{json["descricao"]}'")
            
            if update_fields:
                sql = f'''
                    UPDATE area_interesse
                    SET {', '.join(update_fields)}
                    WHERE id = '{area_id}';
                '''
                self.__postgre.execute(sql)
            
            #Delete each area_do and inssert the new Cursos
            if "curso" in json:
                
                sql = f'''
                    DELETE FROM area_do
                    WHERE id = '{area_id}';
                '''
                self.__postgre.execute(sql)

                for curso in json["curso"]:
                    sql = f'''
                            INSERT INTO area_do
                            (id, codigo)
                            VALUES ({area_id}, {curso});
                        '''
                    self.__postgre.execute(sql)
        
        except:
            return False
        
        self.__postgre.database.commit()
        return True

    #delet data
    def delete(self, area_id):

        try:
            sql = f'''
                DELETE FROM area_interesse
                WHERE id = {area_id};
            '''
            self.__postgre.execute(sql)
        except:
            return False
        
        self.__postgre.database.commit()
        return True

    #close db
    def close(self):
        self.__postgre.close()
    