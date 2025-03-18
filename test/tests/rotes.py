import requests

BASE_URL = "http://127.0.0.1:3030/api"

def test_aluno():
    url = f"{BASE_URL}/aluno"
    data = {   
        "n_matricula": "21.1.4015",
        "nome": "Pedro Augusto",
        "data_matricula": "2021-02-01",
        "curso": 2,
        "telefones": ["5538998107189"],
        "emails": ["pedro.asg@aluno.ufop.edu.br"]
    }
    response = requests.post(url, json=data)
    assert response.status_code == 201
    n_matricula = response.json().get("n_matricula")
    
    response = requests.get(url)
    assert response.status_code == 200
    
    data_update = {"nome": "Fake Augusto"}
    response = requests.put(f"{url}/{n_matricula}", json=data_update)
    assert response.status_code == 204
    
    response = requests.delete(f"{url}/{n_matricula}")
    assert response.status_code == 204

def test_areas():
    url = f"{BASE_URL}/areas"
    data = {
        "nome": "Ciência de Dados",
        "descricao": "A Ciência de Dados é um campo interdisciplinar que combina estatística, matemática, programação e conhecimento de domínio para extrair insights a partir de grandes volumes de dados. Envolve técnicas de análise de dados, aprendizado de máquina, visualização e processamento de dados para apoiar a tomada de decisões.",
        "curso": [2, 3]
    }
    response = requests.post(url, json=data)
    assert response.status_code == 201
    area_id = response.json().get("id")
    
    response = requests.get(url)
    assert response.status_code == 200
    
    data_update = {"descricao": "Nova descrição."}
    response = requests.put(f"{url}/{area_id}", json=data_update)
    assert response.status_code == 204
    
    response = requests.delete(f"{url}/{area_id}")
    assert response.status_code == 204

def test_avaliacao():
    url = f"{BASE_URL}/avaliacao"
    data = {
        "id_turma": 1,
        "data_aplicacao": "2023-06-15",
        "nota_maxima": 10.0,
        "nota_alunos": [{
            "n_matricula": "202300001",
            "nota": 1.0
        }]
    }
    response = requests.post(url, json=data)
    assert response.status_code == 201
    id_turma = response.json().get("id_turma")
    data_aplicacao = response.json().get("data_aplicacao")
    
    response = requests.get(url)
    assert response.status_code == 200
    
    response = requests.delete(f"{url}/{id_turma}/{data_aplicacao}")
    assert response.status_code == 204

def test_curso():
    url = f"{BASE_URL}/curso"
    data = {
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
    response = requests.post(url, json=data)
    assert response.status_code == 201
    codigo = response.json().get("codigo")
    
    response = requests.get(url)
    assert response.status_code == 200

    data_update = {"nome": "fake name"}
    response = requests.put(f"{url}/{codigo}", json=data_update)
    assert response.status_code == 204
    
    response = requests.delete(f"{url}/{codigo}")
    assert response.status_code == 204

def test_disciplina():
    url = f"{BASE_URL}/disciplina"
    data = {
        "codigo": "BCC321",
        "nome": "Banco de Dados 2",
        "codigo_curso": 2
    }
    response = requests.post(url, json=data)
    assert response.status_code == 201
    codigo = response.json().get("codigo")
    
    response = requests.get(url)
    assert response.status_code == 200

    data_update = {"nome": "fake name"}
    response = requests.put(f"{url}/{codigo}", json=data_update)
    assert response.status_code == 204
    
    response = requests.delete(f"{url}/{codigo}")
    assert response.status_code == 204

def test_professor():
    url = f"{BASE_URL}/professor"
    data = {   
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
    response = requests.post(url, json=data)
    assert response.status_code == 201
    cpf = response.json().get("cpf")
    
    response = requests.get(url)
    assert response.status_code == 200

    data_update = {"nome": "fake name"}
    response = requests.put(f"{url}/{cpf}", json=data_update)
    assert response.status_code == 204
    
    response = requests.delete(f"{url}/{cpf}")
    assert response.status_code == 204

def test_turma():
    url = f"{BASE_URL}/turma"
    data = {
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
    response = requests.post(url, json=data)
    assert response.status_code == 201
    turma_id = response.json().get("id")
    
    response = requests.get(url)
    assert response.status_code == 200

    data_update = {"data_inicio": "2012-12-12"}
    response = requests.put(f"{url}/{turma_id}", json=data_update)
    assert response.status_code == 204
    
    response = requests.delete(f"{url}/{turma_id}")
    assert response.status_code == 204

def run_tests():
    print("--------------------------Teste de rotas---------------------------")
    test_aluno()
    test_areas()
    test_avaliacao()
    test_curso()
    test_disciplina()
    test_professor()
    test_turma()
    print("--------------------Todos os testes passaram!----------------------")

