from app.utils.connectDB import PostgreSQL

class Turma:
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
            AND table_name IN ('disciplina', 'turma', 'aluno', 'participa',
             'horarios', 'professor');
        '''
        
        result = self.__postgre.consult(sql)
        
        if result is None or result[0][0] != 6: return False
        else: return True
        
    #insert data from a json
    def insert(self, json):
        try: 
            #Insert Turma and get Turma's id
            sql = f'''
                    INSERT INTO turma 
                    (data_inicio, codigo, cpf)
                    VALUES 
                    ('{json["data_inicio"]}', '{json["codigo"]}', '{json["cpf"]}')
                    RETURNING id;
                '''
            turma_id = self.__postgre.execute(sql)[0][0]

            #Insert each horario
            for horario in json["horarios"]:
                sql = f'''
                        INSERT INTO horarios
                        (sala, dia, horario, id)
                        VALUES 
                        ('{horario["sala"]}', {horario["dia"]}, {horario["horario"]}, {turma_id});
                    '''
                self.__postgre.execute(sql)
            
            #Insert each aluno
            for aluno in json["alunos"]:
                sql = f'''
                        INSERT INTO participa
                        (n_matricula, id, presenca, nota_total)
                        VALUES ('{aluno["n_matricula"]}', {turma_id}, {aluno["presenca"]}, {aluno["nota_total"]});
                    '''
                self.__postgre.execute(sql)

        except Exception as e:
            print(e)
            return None

        self.__postgre.database.commit()
        return turma_id

    #Get all data
    def get_all(self):
        sql = """
                SELECT
                    t.id AS ID,
                    t.codigo AS codigo_disciplina,
                    t.data_inicio,
                    jsonb_build_object(
                        'CPF', pr.cpf,
                        'nome', pr.nome
                    ) AS professor,
                    COALESCE(AVG(p.nota_total), 0) AS media_notas,
                    COUNT(DISTINCT p.n_matricula) AS qnt_alunos
                FROM turma t
                LEFT JOIN professor pr ON pr.cpf = t.cpf
                LEFT JOIN participa p ON p.id = t.id
                GROUP BY t.id, t.codigo, t.data_inicio, pr.cpf, pr.nome;
            """

        result = self.__postgre.consult(sql)
        turmas = {"turmas":[]}

        for row in result:
            turma = {
                "ID": row[0],
                "codigo_disciplina": row[1],
                "data_inicio": row[2].strftime("%Y-%m-%d"),
                "professor": row[3], 
                "media_notas": round(row[4], 2) if row[3] is not None else None,
                "qnt_alunos": int(row[5])  
            }
            turmas["turmas"].append(turma)

        return turmas
        
    #Update data
    def update(self, turma_id, json):

        update_fields = []

        try:
            #Update each field in json
            if "data_inicio" in json:
                update_fields.append(f"data_inicio = '{json["data_inicio"]}'")

            if "codigo" in json:
                update_fields.append(f"codigo = '{json["codigo"]}'")
            
            if "cpf" in json:
                update_fields.append(f"cpf = '{json["cpf"]}'")
            
            if update_fields:
                sql = f'''
                    UPDATE turma
                    SET {', '.join(update_fields)}
                    WHERE id = '{turma_id}';
                '''
                self.__postgre.execute(sql)
            
            #Update each horario
            if "horarios" in json:
                sql = f'''
                        DELETE FROM horarios
                        WHERE id = '{turma_id}';
                    '''
                self.__postgre.execute(sql)

                for horario in json["horarios"]:
                    sql = f'''
                            INSERT INTO horarios
                            (sala, dia, horario, id)
                            VALUES 
                            ('{horario["sala"]}', {horario["dia"]}, {horario["horario"]}, {turma_id});
                        '''
                    self.__postgre.execute(sql)
            
            #Update each aluno
            if "alunos" in json:
                sql = f'''
                        DELETE FROM participa
                        WHERE id = '{turma_id}';
                    '''
                self.__postgre.execute(sql)

                for aluno in json["alunos"]:
                    sql = f'''
                            INSERT INTO participa
                            (n_matricula, id, presenca, nota_total)
                            VALUES ('{aluno["n_matricula"]}', {turma_id}, {aluno["presenca"]}, {aluno["nota_total"]});
                        '''
                    self.__postgre.execute(sql)
        
        except:
            return False
        
        self.__postgre.database.commit()
        return True
        
    #delet data
    def delete(self, turma_id):

        try:
            #Delete Turma
            sql = f'''
                DELETE FROM turma
                WHERE id = {turma_id};
            '''
            self.__postgre.execute(sql)
        except Exception as e:
            return False
        
        self.__postgre.database.commit()
        return True

    #close db
    def close(self):
        self.__postgre.close()
    