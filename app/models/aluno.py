from app.utils.connectDB import PostgreSQL

class Aluno:
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
            AND table_name IN ('curso', 'pessoa', 'aluno', 'telefone_aluno', 'email_aluno', 'participa', 'turma', 'disciplina');
        '''
        
        result = self.__postgre.consult(sql)
        
        if result is None or result[0][0] != 8: return False
        else: return True
        
    #insert data from a json
    def insert(self, json):
        try: 
            #Insert Pessoa and get pessoa's id
            sql = f'''
                    INSERT INTO pessoa 
                    (codigo)
                    VALUES 
                    ('{json["curso"]}')
                    RETURNING id;
                '''
            pessoa_id = self.__postgre.execute(sql)[0][0]
            
            #Insert Aluno
            sql = f'''
                    INSERT INTO aluno
                    (n_matricula, nome, data_matricula, id) 
                    VALUES
                    ('{json["n_matricula"]}','{json["nome"]}','{json["data_matricula"]}','{pessoa_id}')
                    RETURNING n_matricula;
                '''
            
            n_matricula = self.__postgre.execute(sql)[0][0]

            #Insert each telefone and email
            for telefone in json["telefones"]:
                sql = f'''
                        INSERT INTO telefone_aluno
                        (numero, n_matricula)
                        VALUES ('{telefone}', '{n_matricula}');
                    '''
                self.__postgre.execute(sql)
            
            for email in json["emails"]:
                sql = f'''
                        INSERT INTO email_aluno
                        (email, n_matricula)
                        VALUES ('{email}', '{n_matricula}');
                    '''
                self.__postgre.execute(sql)
        except:
            return None

        self.__postgre.database.commit()
        return n_matricula

    #Read all data
    def get_all(self):
        sql = """
            SELECT 
                a.n_matricula, 
                c.nome AS nome_curso, 
                a.nome, 
                a.data_matricula 
            FROM aluno a
            JOIN pessoa p ON a.id = p.id
            JOIN curso c ON p.codigo = c.codigo;
        """
        alunos = self.__postgre.consult(sql)

        if not alunos:
            return None

        alunos_json = {"alunos": []}

        for aluno in alunos:
            n_matricula = aluno[0]

            # Média Nnotas 
            sql = f"""
                SELECT AVG(p.nota_total) AS media_notas
                FROM participa p
                WHERE p.n_matricula = '{n_matricula}'
                GROUP BY p.n_matricula;
            """
            media_notas = self.__postgre.consult(sql)
            media_notas = media_notas[0][0] if media_notas else 0

            # Tempo de curso
            sql = f"""
                SELECT EXTRACT(YEAR FROM AGE(CURRENT_DATE, data_matricula)) AS tempo_curso_anos
                FROM aluno
                WHERE n_matricula = '{n_matricula}';
            """
            tempo_curso = int(self.__postgre.consult(sql)[0][0])

            # Disciplinas aprovadas
            sql = f"""
                SELECT d.codigo 
                FROM participa p
                JOIN turma t ON p.id = t.id
                JOIN disciplina d ON t.codigo = d.codigo
                WHERE p.n_matricula = '{n_matricula}'
                AND p.nota_total >= 6.0
                AND p.presenca >= 8.0;
            """
            disciplinas_aprovadas = [row[0] for row in self.__postgre.consult(sql)]

            # Telefones do aluno
            sql = f"""
                SELECT numero 
                FROM telefone_aluno
                WHERE n_matricula = '{n_matricula}';
            """
            telefones = [row[0] for row in self.__postgre.consult(sql)]

            # Emails do aluno
            sql = f"""
                SELECT email 
                FROM email_aluno
                WHERE n_matricula = '{n_matricula}';
            """
            emails = [row[0] for row in self.__postgre.consult(sql)]

            alunos_json["alunos"].append({
                "n_matricula": aluno[0],
                "nome_curso": aluno[1],
                "nome": aluno[2],
                "data_matricula": aluno[3].strftime("%Y-%m-%d"),
                "media_notas": media_notas,
                "tempo_curso_anos": tempo_curso,
                "disciplinas_aprovadas": disciplinas_aprovadas,
                "telefones": telefones,
                "emails": emails
            })

        return alunos_json

    #Update data
    def update(self, n_matricula, json):

        update_fields = []

        try:
            #Update each field in json
            if "nome" in json:
                update_fields.append(f"nome = '{json["nome"]}'")

            if "data_matricula" in json:
                update_fields.append(f"data_matricula = '{json["data_matricula"]}'")
            
            if update_fields:
                sql = f'''
                    UPDATE aluno
                    SET {', '.join(update_fields)}
                    WHERE n_matricula = '{n_matricula}';
                '''
                self.__postgre.execute(sql)
            
            #Delete each telefone and email and inssert the new ones
            if "telefones" in json:
                
                sql = f'''
                    DELETE FROM telefone_aluno
                    WHERE n_matricula = '{n_matricula}';
                '''

                self.__postgre.execute(sql)

                for telefone in json["telefones"]:
                    sql = f'''
                            INSERT INTO telefone_aluno
                            (numero, n_matricula)
                            VALUES ('{telefone}', '{n_matricula}');
                        '''
                    self.__postgre.execute(sql)

            if "emails" in json:
                
                sql = f'''
                    DELETE FROM email_aluno
                    WHERE n_matricula = '{n_matricula}';
                '''

                self.__postgre.execute(sql)

                for email in json["emails"]:
                    sql = f'''
                            INSERT INTO email_aluno
                            (email, n_matricula)
                            VALUES ('{email}', '{n_matricula}');
                        '''
                    self.__postgre.execute(sql)
        
        except:
            return False
        
        self.__postgre.database.commit()
        return True
        
    #delet data
    def delete(self, n_matricula):

        try:
            #Get pessoa's id
            sql = f'''
                    SELECT id 
                    FROM aluno 
                    WHERE n_matricula = '{n_matricula}';
                '''
            pessoa_id = self.__postgre.execute(sql)[0][0]
            
            #Delete Pessoa
            sql = f'''
                DELETE FROM pessoa
                WHERE id = {pessoa_id};
            '''
            self.__postgre.execute(sql)
        except Exception as e:
            return False
        
        self.__postgre.database.commit()
        return True

    #close db
    def close(self):
        self.__postgre.close()
    