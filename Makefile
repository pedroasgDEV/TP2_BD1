# Criar containers e esperar até que o serviço esteja pronto
buil_containers:
	docker-compose up -d --build

# Criar ambiente virtual
create_env:
	python -m venv .tp2_bd1 

# Instalar as dependências do projeto
install_requirements: create_env
	.tp2_bd1/bin/pip install -r test/requirements.txt

# Rodar os testes
test: install_requirements
	.tp2_bd1/bin/python -m test

# Finalizar containers, volumes e imagens e remover cache do Python e enviromente
clean:
	docker-compose down --volumes --rmi all
	deactivate; rm -rf .tp2_bd1
	find . -type d -name '__pycache__' -exec rm -r {} +

