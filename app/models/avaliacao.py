from app.utils.connectDB import PostgreSQL
import datetime

class Avaliacao:
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
            AND table_name IN ('turma', 'aluno', 'possui', 'participa', 'avaliacao');
        '''
        
        result = self.__postgre.consult(sql)
        
        if result is None or result[0][0] != 5: return False
        else: return True
        
    #insert data from a json
    def insert(self, json):

        #Check if Alunos are in the Turma
        for aluno in json["nota_alunos"]:
            sql = f'''
                    SELECT COUNT(*)
                    FROM participa
                    WHERE id = {json["id_turma"]}
                    AND n_matricula = '{aluno["n_matricula"]}';
                '''
            if self.__postgre.execute(sql)[0][0] != 1: return None

        try:
            #Insert avaliacao
            sql = f'''
                    INSERT INTO avaliacao 
                    (id, data_aplicacao, nota_maxima)
                    VALUES 
                    ({json["id_turma"]}, '{json["data_aplicacao"]}', {json["nota_maxima"]})
                    RETURNING id, data_aplicacao;
                '''
            result = self.__postgre.execute(sql)
            result = (result[0][0], result[0][1].strftime("%Y-%-m-%-d"))

            #Insert nota for each Aluno and update nota_total
            for aluno in json["nota_alunos"]:
                sql = f'''
                        INSERT INTO possui
                        (n_matricula, id, data_aplicacao, nota)
                        VALUES ('{aluno["n_matricula"]}', {json["id_turma"]}, '{json["data_aplicacao"]}', {aluno["nota"]});
                    '''
                self.__postgre.execute(sql)

                sql = f'''
                        UPDATE participa
                        SET nota_total = nota_total + {aluno["nota"]}
                        WHERE n_matricula = '{aluno["n_matricula"]}' 
                        AND id = {json["id_turma"]};
                    '''
                self.__postgre.execute(sql)

        except Exception as e:
            return None
        
        self.__postgre.database.commit()
        return result

    #Get All Data
    def get_all(self):
        sql = '''
            SELECT 
                a.id AS id_turma,
                a.data_aplicacao,
                a.nota_maxima,
                AVG(p.nota) AS media,
                COUNT(CASE WHEN p.nota >= a.nota_maxima * 0.6 THEN 1 END) AS qnt_acima_60pct,
                MAX(p.nota) AS maior_nota,
                MIN(p.nota) AS menor_nota
            FROM avaliacao a
            LEFT JOIN possui p ON a.id = p.id AND a.data_aplicacao = p.data_aplicacao
            GROUP BY a.id, a.data_aplicacao, a.nota_maxima;
        '''
        result = self.__postgre.consult(sql)

        if result is None:
            return None

        avaliacoes = {"avaliacoes":[]}
        for row in result:
            avaliacoes["avaliacoes"].append({
                "id_turma": row[0],
                "data_aplicacao": row[1].strftime("%Y-%m-%d"),
                "nota_maxima": float(row[2]),
                "media": round(float(row[3]), 2) if row[3] is not None else None,
                "qnt_acima_60pct": row[4],
                "maior_nota": float(row[5]) if row[5] is not None else None,
                "menor_nota": float(row[6]) if row[6] is not None else None
            })

        return avaliacoes

    #delet data
    def delete(self, turma_id, data_aplicacao):

        try:
            #Get the nota and n_matricula
            sql = f'''
                SELECT n_matricula, nota
                FROM possui
                WHERE id = {turma_id} 
                AND data_aplicacao = '{data_aplicacao}';
            '''
            alunos = self.__postgre.execute(sql)

            #Update nota_total for each aluno
            for aluno in alunos:
                sql = f'''
                        UPDATE participa
                        SET nota_total = nota_total - {aluno[1]}
                        WHERE n_matricula = '{aluno[0]}' 
                        AND id = {turma_id};
                    '''
                self.__postgre.execute(sql)

            #Delete avaliacap
            sql = f'''
                    DELETE FROM avaliacao
                    WHERE data_aplicacao = '{data_aplicacao}'
                    AND id = {turma_id};
                '''

            self.__postgre.execute(sql)
        except:
            return False
        
        self.__postgre.database.commit()
        return True

    #close db
    def close(self):
        self.__postgre.close()
    