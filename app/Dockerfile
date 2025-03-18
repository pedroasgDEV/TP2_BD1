# Usa uma imagem oficial do Python
FROM python:3.13-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Cria a pasta "app" dentro do WORKDIR
RUN mkdir /app/app

# Copia todos os arquivos do projeto para dentro da pasta "app" dentro do container
COPY . /app/app/

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r app/requirements.txt

# Expõe a porta do Flask (caso necessário)
EXPOSE 3030

# Comando para rodar a aplicação
CMD ["python", "-m", "app"]
