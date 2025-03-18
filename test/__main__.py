from test.tests.aluno import AlunoTest
from test.tests.areas import AreasTest
from test.tests.avaliacao import AvaliacaoTest
from test.tests.curso import CursoTest
from test.tests.disciplina import DisciplinaTest
from test.tests.professor import ProfessorTest
from test.tests.turma import TurmaTest
from test.tests.rotes import run_tests

aluno = AlunoTest()

json = {   
    "n_matricula": "21.1.4015",
    "nome": "Pedro Augusto",
    "data_matricula": "2021-02-01",
    "curso": 2,
    "telefones": ["5538998107189"],
    "emails": ["pedro.asg@aluno.ufop.edu.br"]
}

if aluno.insertTest(json): print(" * Insert operation works :)")
else: print(" * Insert operation not works :(")

if aluno.getAllTest(): print(" * Get All operation works :)")
else: print(" * Get All operation not works :(")

json = {   
    "nome": "Fake Augusto",
    "telefones": ["22222222123"],
    "emails": ["fake@email.com"]
}

if aluno.updateTest(json): print(" * Update operation works :)")
else: print(" * Update operation not works :(")

if aluno.deleteTest(): print(" * Delete operation works :)")
else: print(" * Delete operation not works :(")

areas = AreasTest()

json = {
    "nome": "Ciência de Dados",
    "descricao": "A Ciência de Dados é um campo interdisciplinar que combina estatística, matemática, programação e conhecimento de domínio para extrair insights a partir de grandes volumes de dados. Envolve técnicas de análise de dados, aprendizado de máquina, visualização e processamento de dados para apoiar a tomada de decisões.",
    "curso": [2, 3]
}

if areas.insertTest(json): print(" * Insert operation works :)")
else: print(" * Insert operation not works :(")

if areas.getAllTest(): print(" * Get All operation works :)")
else: print(" * Get All operation not works :(")

json = {
    "descricao": "Ignore a Descrição",
    "curso": [1]
}

if areas.updateTest(json): print(" * Update operation works :)")
else: print(" * Update operation not works :(")

if areas.deleteTest(): print(" * Delete operation works :)")
else: print(" * Delete operation not works :(")

avaliacao = AvaliacaoTest()

json = {
    "id_turma": 1,
    "data_aplicacao": "2023-06-15",
    "nota_maxima": 10.0,
    "nota_alunos": [{
        "n_matricula": "202300001",
        "nota": 1.0
    }]
}

if avaliacao.insertTest(json): print(" * Insert operation works :)")
else: print(" * Insert operation not works :(")

if avaliacao.getAllTest(): print(" * Get All operation works :)")
else: print(" * Get All operation not works :(")

if avaliacao.deleteTest(): print(" * Delete operation works :)")
else: print(" * Delete operation not works :(")

curso = CursoTest()

json = {
    "nome": "Analise e Desenvolvimento de Sistemas",
    "telefones": ["1111-1111", 
                  "2222-2222"],
    "emails": ["ccomp@universidade.com",
               "guilherme@universidade.com"],
    "coordenador": {
        "cpf": "99999999999",
        "data_inicio": "2016-04-10",
        "data_fim": "2017-04-10"
    }
}

if curso.insertTest(json): print(" * Insert operation works :)")
else: print(" * Insert operation not works :(")

if curso.getAllTest(): print(" * Get All operation works :)")
else: print(" * Get All operation not works :(")

json1 = {
    "nome": "Analise de Sistemas",
    "telefones": ["0"],
    "emails": ["fake@email.com"],
    "coordenador": {
        "data_inicio": "2017-04-10",
        "data_fim": "2018-04-10"
    }
}

json2 = {
    "coordenador": {
        "cpf": "77777777777",
        "data_inicio": "2016-04-10",
        "data_fim": "2017-04-10"
    }
}

if curso.updateTest(json1): print(" * Update type 1 operation works :)")
else: print(" * Update type 1 operation not works :(")

if curso.updateTest(json2): print(" * Update type 2 operation works :)")
else: print(" * Update type 2 operation not works :(")

if curso.deleteTest(): print(" * Delete operation works :)")
else: print(" * Delete operation not works :(")

disciplina = DisciplinaTest()

json = {
    "codigo": "BCC321",
    "nome": "Banco de Dados 2",
    "codigo_curso": 2
}

if disciplina.insertTest(json): print(" * Insert operation works :)")
else: print(" * Insert operation not works :(")

if disciplina.getAllTest(): print(" * Get All operation works :)")
else: print(" * Get All operation not works :(")

json = {
    "nome": "BD 2",
    "codigo_curso": 1
}

if disciplina.updateTest(json): print(" * Update operation works :)")
else: print(" * Update operation not works :(")

if disciplina.deleteTest(): print(" * Delete operation works :)")
else: print(" * Delete operation not works :(")

professor = ProfessorTest()

json1 = {   
    "cpf": "12121212121",
    "nome": "Dr. Pedro Augusto",
    "data_inicio_contrato": "2020-03-01",
    "curso": 2,
    "telefones": ["5538998107189"],
    "emails": ["pedro.asg@ufop.edu.br"],
    "especializa": {
        "tipo": "substituto",
        "data_fim_contrato": "2021-03-01"
    }
}

json2 = {   
    "cpf": "13131313131",
    "nome": "Dr. Augusto Pedro",
    "data_inicio_contrato": "2021-03-01",
    "curso": 1,
    "telefones": ["5538998107189"],
    "emails": ["pedro.asg@ufop.edu.br"],
    "especializa": {
        "tipo": "titular",
        "areas": [1, 2]
    }
}

if professor.insertTest(json1): print(" * Insert Substituto operation works :)")
else: print(" * Insert Substituto operation not works :(")

if professor.getAllTest(): print(" * Get All operation works :)")
else: print(" * Get All operation not works :(")

json1 = {   
    "nome": "Dr. Augusto Pedro",
    "data_inicio_contrato": "2021-03-01",
    "telefones": ["0"],
    "emails": ["fake@email.com"],
    "especializa": {
        "tipo": "titular",
        "areas": [1, 2]
    }
}

if professor.updateTest(json1): print(" * Update Substituto operation works :)")
else: print(" * Update Substituto operation not works :(")

if professor.deleteTest(): print(" * Delete Substituto operation works :)")
else: print(" * Delete Substituto operation not works :(")

if professor.insertTest(json2): print(" * Insert Titular operation works :)")
else: print(" * Insert Titular operation not works :(")

json2 = {   
    "nome": "Dr. Pedro Augusto",
    "data_inicio_contrato": "2020-03-01",
    "telefones": ["0"],
    "emails": ["fake@email.com"],
    "especializa": {
        "tipo": "substituto",
        "data_fim_contrato": "2021-03-01"
    }
}

if professor.updateTest(json2): print(" * Update Titular operation works :)")
else: print(" * Update Titular operation not works :(")

if professor.deleteTest(): print(" * Delete Titular operation works :)")
else: print(" * Delete Titular operation not works :(")

turma = TurmaTest()

json = {
    "data_inicio": "2024-01-15",
    "codigo": "BCC002",
    "cpf": "99999999999",
    "horarios": [{
        "sala": "201",
        "dia": 1,
        "horario": 2
    }, {
        "sala": "201",
        "dia": 3,
        "horario": 2
    }],
    "alunos": [{
        "n_matricula": "202300001",
        "presenca": 10.00,
        "nota_total": 0.0
    }]
}

if turma.insertTest(json): print(" * Insert operation works :)")
else: print(" * Insert operation not works :(")

if turma.getAllTest(): print(" * Get All operation works :)")
else: print(" * Get All operation not works :(")


json = {
    "data_inicio": "2026-01-15",
    "codigo": "ENG001",
    "cpf": "11111111111",
    "horarios": [{
        "sala": "215",
        "dia": 6,
        "horario": 1
    }, {
        "sala": "205",
        "dia": 6,
        "horario": 1
    }],
    "alunos": [{
        "n_matricula": "202300001",
        "presenca": 8.00,
        "nota_total": 2.0
    }]
}

if turma.updateTest(json): print(" * Update operation works :)")
else: print(" * Update operation not works :(")

if turma.deleteTest(): print(" * Delete operation works :)")
else: print(" * Delete operation not works :(")

run_tests()