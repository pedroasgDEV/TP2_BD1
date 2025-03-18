from app.utils.connectDB import PostgreSQL

class Curso:
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
            AND table_name IN ('curso', 'telefone_curso', 'email_curso', 'coordenador', 'aluno',
                                'pessoa', 'professor', 'disciplina', 'area_do');
        '''
        
        result = self.__postgre.consult(sql)
        
        if result is None or result[0][0] != 9: return False
        else: return True
        
    #insert data from a json
    def insert(self, json):
        
        try:
            #Insert curso
            sql = f'''
                    INSERT INTO curso 
                    (nome)
                    VALUES 
                    ('{json["nome"]}')
                    RETURNING codigo;
                '''
            curso_codigo = self.__postgre.execute(sql)[0][0]

            #Insert Coordenador
            sql = f'''
                    INSERT INTO coordenador 
                    (cpf, codigo, data_inicio, data_fim)
                    VALUES
                    ('{json["coordenador"]["cpf"]}', {curso_codigo}, 
                    '{json["coordenador"]["data_inicio"]}', '{json["coordenador"]["data_fim"]}');
                '''
            self.__postgre.execute(sql)

            #Insert each telefone and email
            for telefone in json["telefones"]:
                sql = f'''
                        INSERT INTO telefone_curso
                        (numero, codigo)
                        VALUES ('{telefone}', {curso_codigo});
                    '''
                self.__postgre.execute(sql)
            
            for email in json["emails"]:
                sql = f'''
                        INSERT INTO email_curso
                        (email, codigo)
                        VALUES ('{email}', {curso_codigo});
                    '''
                self.__postgre.execute(sql)

        except: 
            return None
        
        self.__postgre.database.commit()
        return curso_codigo

    #Get all data
    def get_all(self):
        sql = '''
            SELECT 
                c.codigo,
                c.nome,
                ARRAY(SELECT t.numero FROM telefone_curso t WHERE t.codigo = c.codigo) AS telefones,
                ARRAY(SELECT e.email FROM email_curso e WHERE e.codigo = c.codigo) AS emails,
                (SELECT COUNT(*) FROM aluno a 
                JOIN pessoa p ON a.id = p.id 
                WHERE p.codigo = c.codigo) AS qnt_aluno,
                (SELECT COUNT(*) FROM professor pr 
                JOIN pessoa p ON pr.id = p.id 
                WHERE p.codigo = c.codigo) AS qnt_professores,
                (SELECT COUNT(*) FROM disciplina d WHERE d.codigo_curso = c.codigo) AS qnt_disciplinas,
                (SELECT COUNT(*) FROM area_do ad WHERE ad.codigo = c.codigo) AS qnt_areas,
                p.cpf AS cpf_prof_titular,
                p.nome AS coordenador_nome,
                co.data_inicio AS coordenador_data_inicio,
                co.data_fim AS coordenador_data_fim
            FROM 
                curso c
            LEFT JOIN 
                coordenador co ON c.codigo = co.codigo
            LEFT JOIN 
                professor p ON co.cpf = p.cpf;
        '''
        
        result = self.__postgre.consult(sql)
        
        cursos = {"cursos": []}
        
        for row in result:
            curso = {
                "codigo": row[0],
                "nome": row[1],
                "telefones": row[2],
                "emails": row[3],
                "qnt_aluno": row[4],
                "qnt_professores": row[5],
                "qnt_disciplinas": row[6],
                "qnt_areas": row[7],
                "coordenador": {
                    "cpf_prof_titular": row[8],
                    "nome": row[9],
                    "data_inicio": row[10].strftime('%Y-%m-%d') if row[10] else None,
                    "data_fim": row[11].strftime('%Y-%m-%d') if row[11] else None
                }
            }
            cursos["cursos"].append(curso)
        
        return cursos

    #Update data
    def update(self, curso_codigo, json):
        try:
            #Update nome if is in json
            if "nome" in json:
                sql = f'''
                    UPDATE curso
                    SET nome = '{json["nome"]}'
                    WHERE codigo = {curso_codigo};
                '''

                self.__postgre.execute(sql)
               
            
            #Delete each telefone and email and inssert the new ones
            if "telefones" in json:
                
                sql = f'''
                    DELETE FROM telefone_curso
                    WHERE codigo = {curso_codigo};
                '''

                self.__postgre.execute(sql)

                for telefone in json["telefones"]:
                    sql = f'''
                            INSERT INTO telefone_curso
                            (numero, codigo)
                            VALUES ('{telefone}', {curso_codigo});
                        '''
                    self.__postgre.execute(sql)

            if "emails" in json:
                
                sql = f'''
                    DELETE FROM email_curso
                    WHERE codigo = {curso_codigo};
                '''

                self.__postgre.execute(sql)

                for email in json["emails"]:
                    sql = f'''
                            INSERT INTO email_curso
                            (email, codigo)
                            VALUES ('{email}', {curso_codigo});
                        '''
                    self.__postgre.execute(sql)

            #Delete and update the coordenador if is in json
            if "coordenador" in json:

                coordenador = json["coordenador"]

                #If change Coordenador 
                if all(key in coordenador for key in ("cpf", "data_inicio", "data_fim")):
                    sql = f'''
                            DELETE FROM coordenador
                            WHERE codigo = {curso_codigo};
                        '''
                    self.__postgre.execute(sql)

                    #Insert the new Coordenador
                    sql = f'''
                            INSERT INTO coordenador 
                            (cpf, codigo, data_inicio, data_fim)
                            VALUES
                            ('{coordenador["cpf"]}', {curso_codigo}, 
                            '{coordenador["data_inicio"]}', '{coordenador["data_fim"]}');
                        '''
                    self.__postgre.execute(sql)


                #If change data_inicio or data_fim
                else: 
                    if "data_inicio" in coordenador:
                        sql = f'''
                            UPDATE coordenador
                            SET data_inicio = '{coordenador["data_inicio"]}'
                            WHERE codigo = {curso_codigo};
                        '''

                        self.__postgre.execute(sql)

                    if "data_fim" in coordenador:
                        sql = f'''
                            UPDATE coordenador
                            SET data_fim = '{coordenador["data_fim"]}'
                            WHERE codigo = {curso_codigo};
                        '''

                        self.__postgre.execute(sql)
        
        except Exception as e:
            print(e)
            return False
        
        self.__postgre.database.commit()
        return True

    #delet data
    def delete(self, curso_codigo):
        
        try:
            #Delete Curso
            sql = f'''
                    DELETE FROM curso
                    WHERE codigo = {curso_codigo};
                '''
            self.__postgre.execute(sql)
        except Exception as e:
            return False
        
        self.__postgre.database.commit()
        return True

    #close db
    def close(self):
        self.__postgre.close()
    