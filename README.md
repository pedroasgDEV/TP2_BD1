#TP2 - Banco de Dados 1

## Alunos: 

- **Pedro Augusto Gonçalves**
- **Camila Torres**
- **Henrique Lauar**
- **Luísa Notaro**
- **Matheus Drumond**
- **Rafael Stylita**

Este repositório contém o código e as instruções para automatizar a criação de containers Docker, configuração de ambiente virtual, instalação de dependências e execução de testes. O `Makefile` foi utilizado para simplificar esse processo.

## Estrutura do Repositório

- **`Modelo ERE/`**: Contém os itens 1 e 2 do trabalho.
- **`postgresql/initdb/`**: Contém o item 3 do trabalho.
- **`app/` e `frontend/`**: Contêm o item 4 do trabalho.

## Requisitos

Antes de rodar os comandos do `Makefile`, certifique-se de que você possui as seguintes ferramentas instaladas:

- **Docker** e **Docker Compose**: Para a criação e gerenciamento de containers.
- **Python**: Para criar o ambiente virtual e rodar os testes.
- **Make**: Para executar as regras do `Makefile`.

## Como Usar

### 1. Subir os Containers

A primeira coisa a fazer é subir os containers Docker para a execução do projeto. Isso vai criar o ambiente necessário para o banco de dados e o aplicativo.

Para subir os containers, execute:

```bash
make buil_containers
```

Este comando vai rodar o `docker-compose` para subir os containers definidos no arquivo `docker-compose.yml`. O parâmetro `--build` garante que os containers sejam construídos a partir das imagens mais recentes.

### 2. Criar o Ambiente Virtual

Após subir os containers, o próximo passo é criar um ambiente virtual para o projeto. Isso isola as dependências Python do sistema.

Para criar o ambiente virtual, execute:

```bash
make create_env
```

Isso vai criar uma pasta chamada `.tp2_bd1`, onde o ambiente virtual será configurado.

### 3. Instalar as Dependências

Uma vez criado o ambiente virtual, você precisa instalar as dependências do projeto, que estão listadas no arquivo `test/requirements.txt`.

Para instalar as dependências, execute:

```bash
make install_requirements
```

Isso vai instalar todas as bibliotecas necessárias para o funcionamento do projeto dentro do ambiente virtual.

### 4. Rodar os Testes

Após instalar as dependências, você pode rodar os testes para verificar se tudo está funcionando corretamente.

Para rodar os testes, execute:

```bash
make test
```

Este comando vai rodar os testes Python definidos na pasta `test/` usando o ambiente virtual criado anteriormente.

### 5. Limpar o Ambiente

Após terminar de trabalhar no projeto, você pode limpar o ambiente, finalizando os containers, removendo volumes, imagens Docker, o ambiente virtual e caches Python.

Para limpar o ambiente, execute:

```bash
make clean
```

Este comando vai:

- Finalizar os containers com `docker-compose down --volumes --rmi all`.
- Desativar o ambiente virtual e remover a pasta `.tp2_bd1`.
- Remover os caches Python (`__pycache__`).

## Estrutura das Pastas

Aqui está uma visão geral de como as pastas estão organizadas:

- **`Modelo ERE/`**: Contém os itens 1 e 2 do trabalho.
- **`postgresql/initdb/`**: Contém o item 3 do trabalho.
- **`app/` e `frontend/`**: Contêm o item 4 do trabalho, que envolve a aplicação e o front-end.