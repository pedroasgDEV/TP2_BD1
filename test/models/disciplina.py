from test.utils.connectDB import PostgreSQL

class Disciplina:
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
            AND table_name IN ('disciplina', 'curso', 'professor', 'participa', 'turma');
        '''
        
        result = self.__postgre.consult(sql)
        
        if result is None or result[0][0] != 5: return False
        else: return True
        
    #insert data from a json
    def insert(self, json):

        try: 
            #Insert Disciplina
            sql = f'''
                    INSERT INTO disciplina 
                    (codigo, nome, codigo_curso)
                    VALUES 
                    ('{json["codigo"]}', '{json["nome"]}', {json["codigo_curso"]})
                    RETURNING codigo;
                '''
            disciplina_codigo = self.__postgre.execute(sql)[0][0]
            
        except:
            return None

        self.__postgre.database.commit()
        return disciplina_codigo

    #Get all data
    def get_all(self):
        sql = '''
            SELECT 
                d.codigo,
                c.nome AS nome_curso,
                d.nome,
                -- Calcular a média das notas com base nas turmas associadas à disciplina
                COALESCE((
                    SELECT AVG(p.nota_total)
                    FROM participa p
                    JOIN turma t ON t.id = p.id
                    WHERE t.codigo = d.codigo
                ), 0) AS media_notas,
                (
                    SELECT json_agg(
                        json_build_object(
                            'CPF', p.cpf,
                            'nome', p.nome
                        )
                    )
                    FROM professor p
                    JOIN turma t ON t.cpf = p.cpf
                    WHERE t.codigo = d.codigo
                ) AS professores
            FROM 
                disciplina d
            JOIN 
                curso c ON c.codigo = d.codigo_curso;   
        '''
        
        result = self.__postgre.consult(sql)
        
        disciplinas = {"disciplinas": []}
        
        for row in result:
            disciplina = {
                "disciplina": {
                    "codigo": row[0],
                    "nome_curso": row[1],
                    "nome": row[2],
                    "media_notas": round(row[3], 2) if row[3] is not None else None,
                    "professores": row[4] if row[4] else []
                }
            }
            disciplinas["disciplinas"].append(disciplina)
        
        return disciplinas

    #Update data
    def update(self, disciplina_codigo, json):

        update_fields = []

        try:
            #Update each field in json
            if "nome" in json:
                update_fields.append(f"nome = '{json["nome"]}'")

            if "codigo_curso" in json:
                update_fields.append(f"codigo_curso = {json["codigo_curso"]}")
            
            if update_fields:
                sql = f'''
                    UPDATE disciplina
                    SET {', '.join(update_fields)}
                    WHERE codigo = '{disciplina_codigo}';
                '''
                self.__postgre.execute(sql)
        
        except:
            return False
        
        self.__postgre.database.commit()
        return True

    #delet data
    def delete(self, disciplina_codigo):

        try:
            #Delete Disciplina
            sql = f'''
                DELETE FROM disciplina
                WHERE codigo = '{disciplina_codigo}';
            '''
            self.__postgre.execute(sql)
        except:
            return False
        
        self.__postgre.database.commit()
        return True

    #close db
    def close(self):
        self.__postgre.close()
    