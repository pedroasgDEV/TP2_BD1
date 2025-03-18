from app.utils.connectDB import PostgreSQL

class Professor:
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
            AND table_name IN ('curso', 'pessoa', 'professor', 'telefone_professor',
             'email_professor', 'professor_substituto', 'professor_titular', 'se_interessa',
             'participa', 'aluno', 'turma');
        '''
        
        result = self.__postgre.consult(sql)
        
        if result is None or result[0][0] != 11: return False
        else: return True
        
    #insert data from a json
    def insert(self, json):
        try: 
            #Insert Pessoa and get pessoa's id
            sql = f'''
                    INSERT INTO pessoa 
                    (codigo)
                    VALUES 
                    ({json["curso"]})
                    RETURNING id;
                '''
            pessoa_id = self.__postgre.execute(sql)[0][0]
            
            #Insert Professor
            sql = f'''
                    INSERT INTO professor
                    (cpf, nome, data_inicio_contrato, id) 
                    VALUES
                    ('{json["cpf"]}', '{json["nome"]}', '{json["data_inicio_contrato"]}', {pessoa_id})
                    RETURNING cpf;
                '''
            
            professor_cpf = self.__postgre.execute(sql)[0][0]

            #Insert each telefone and email
            for telefone in json["telefones"]:
                sql = f'''
                        INSERT INTO telefone_professor
                        (numero, cpf)
                        VALUES ('{telefone}', '{professor_cpf}');
                    '''
                self.__postgre.execute(sql)
            
            for email in json["emails"]:
                sql = f'''
                        INSERT INTO email_professor
                        (email, cpf)
                        VALUES ('{email}', '{professor_cpf}');
                    '''
                self.__postgre.execute(sql)

            #Insert especializa
            especializa = json["especializa"]

            if especializa["tipo"] == "substituto":
                sql = f'''
                        INSERT INTO professor_substituto
                        (cpf, data_fim_contrato)
                        VALUES
                        ('{professor_cpf}', '{especializa["data_fim_contrato"]}');
                    '''
                self.__postgre.execute(sql)
            
            elif especializa["tipo"] == "titular":
                sql = f'''
                        INSERT INTO professor_titular
                        (cpf)
                        VALUES
                        ('{professor_cpf}');
                    '''
                self.__postgre.execute(sql)

                for area in especializa["areas"]:
                    sql = f'''
                            INSERT INTO se_interessa
                            (id, cpf) 
                            VALUES
                            ({area}, '{professor_cpf}');
                        '''
                    self.__postgre.execute(sql)

        except Exception as e:
            return None

        self.__postgre.database.commit()
        return professor_cpf

    #Get all data
    def get_all(self):
        sql = """
            SELECT
                pr.cpf,
                c.nome AS nome_curso,
                pr.nome AS nome_professor,
                pr.data_inicio_contrato,
                ARRAY_AGG(DISTINCT tp.numero) AS telefones,
                ARRAY_AGG(DISTINCT ep.email) AS emails,
                CASE 
                    WHEN ps.cpf IS NOT NULL THEN 'titular'
                    ELSE 'substituto'
                END AS especializa,
                EXTRACT(YEAR FROM AGE(pr.data_inicio_contrato)) AS contrato_anos,
                (SELECT AVG(par.nota_total)
                FROM participa par
                JOIN aluno al ON al.n_matricula = par.n_matricula
                WHERE par.id IN (SELECT id FROM turma WHERE cpf = pr.cpf)) AS media_notas_alunos,
                (SELECT COUNT(DISTINCT al.id)
                FROM aluno al
                JOIN participa par ON par.n_matricula = al.n_matricula
                JOIN turma t ON t.id = par.id
                WHERE t.cpf = pr.cpf) AS qnt_alunos
            FROM
                professor pr
            JOIN pessoa pe ON pe.id = pr.id
            JOIN curso c ON c.codigo = pe.codigo
            LEFT JOIN telefone_professor tp ON tp.cpf = pr.cpf
            LEFT JOIN email_professor ep ON ep.cpf = pr.cpf
            LEFT JOIN professor_titular ps ON ps.cpf = pr.cpf
            GROUP BY
                pr.cpf, c.nome, pr.nome, pr.data_inicio_contrato, ps.cpf;

            """
        result = self.__postgre.consult(sql)

        professores = {"professores": []}

        for row in result:
            professor = {
                "CPF": row[0],
                "nome_curso": row[1],
                "nome": row[2],
                "data_inicio_contrato": row[3].strftime("%Y-%m-%d"),
                "telefones": row[4],
                "emails": row[5],
                "especializa": row[6],
                "contrato_anos": int(row[7]),
                "media_notas_alunos": round(row[8], 2) if row[8] is not None else None,
                "qnt_alunos": row[9]
            }
            professores["professores"].append(professor)

        return professores 

    #Update data
    def update(self, professor_cpf, json):

        update_fields = []

        try:
            #Update each field in json
            if "nome" in json:
                update_fields.append(f"nome = '{json["nome"]}'")

            if "data_inicio_contrato" in json:
                update_fields.append(f"data_inicio_contrato = '{json["data_inicio_contrato"]}'")
            
            if update_fields:
                sql = f'''
                    UPDATE professor
                    SET {', '.join(update_fields)}
                    WHERE cpf = '{professor_cpf}';
                '''
                self.__postgre.execute(sql)
            
            #Delete each telefone and email and inssert the new ones
            if "telefones" in json:
                
                sql = f'''
                    DELETE FROM telefone_professor
                    WHERE cpf = '{professor_cpf}';
                '''

                self.__postgre.execute(sql)

                for telefone in json["telefones"]:
                    sql = f'''
                            INSERT INTO telefone_professor
                            (numero, cpf)
                            VALUES ('{telefone}', '{professor_cpf}');
                        '''
                    self.__postgre.execute(sql)

            if "emails" in json:
                 
                sql = f'''
                    DELETE FROM email_professor
                    WHERE cpf = '{professor_cpf}';
                '''

                self.__postgre.execute(sql)

                for email in json["emails"]:
                    sql = f'''
                            INSERT INTO email_professor
                            (email, cpf)
                            VALUES ('{email}', '{professor_cpf}');
                        '''
                    self.__postgre.execute(sql)

            #Update especialidade
            if "especializa" in json:

                especializa = json["especializa"]

                #Delete old especialidade
                sql = f'''
                        DELETE FROM professor_substituto 
                        WHERE cpf = '{professor_cpf}';

                        DELETE FROM professor_titular 
                        WHERE cpf = '{professor_cpf}';
                    '''
                self.__postgre.execute(sql)

                #Insert new especialidade
                if especializa["tipo"] == "substituto":
                    sql = f'''
                            INSERT INTO professor_substituto
                            (cpf, data_fim_contrato)
                            VALUES
                            ('{professor_cpf}', '{especializa["data_fim_contrato"]}');
                        '''
                    self.__postgre.execute(sql)
                
                elif especializa["tipo"] == "titular":
                    sql = f'''
                            INSERT INTO professor_titular
                            (cpf)
                            VALUES
                            ('{professor_cpf}');
                        '''
                    self.__postgre.execute(sql)

                    for area in especializa["areas"]:
                        sql = f'''
                                INSERT INTO se_interessa
                                (id, cpf) 
                                VALUES
                                ({area}, '{professor_cpf}');
                            '''
                        self.__postgre.execute(sql)
        
        except:
            return False
        
        self.__postgre.database.commit()
        return True
        
    #delet data
    def delete(self, professor_cpf):

        try:
            #Get pessoa's id
            sql = f'''
                    SELECT id 
                    FROM professor 
                    WHERE cpf = '{professor_cpf}';
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
    