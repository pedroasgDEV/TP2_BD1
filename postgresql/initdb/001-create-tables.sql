-- Entidade Curso
CREATE TABLE IF NOT EXISTS Curso (
    codigo INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    CONSTRAINT PK_Curso PRIMARY KEY (codigo)
);

CREATE TABLE IF NOT EXISTS telefone_curso (
    numero VARCHAR(15) NOT NULL, 
    codigo INT NOT NULL,
    CONSTRAINT PK_telefone_curso PRIMARY KEY (numero, codigo),
    CONSTRAINT FK_telefone_curso FOREIGN KEY (codigo)
        REFERENCES Curso (codigo)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS email_curso (
    email VARCHAR(255) NOT NULL, 
    codigo INT NOT NULL,
    CONSTRAINT PK_email_curso PRIMARY KEY (email, codigo),
    CONSTRAINT FK_email_curso FOREIGN KEY (codigo)
        REFERENCES Curso (codigo)
        ON DELETE CASCADE
);

-- União Pessoa
CREATE TABLE IF NOT EXISTS Pessoa (
    ID INT NOT NULL AUTO_INCREMENT,
    codigo INT NOT NULL,
    CONSTRAINT PK_Pessoa PRIMARY KEY (ID),
    CONSTRAINT FK_Pessoa FOREIGN KEY (codigo)
        REFERENCES Curso (codigo)
);

-- Entidade Aluno
CREATE TABLE IF NOT EXISTS Aluno (
    n_matricula CHAR(9) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    data_matricula DATE NOT NULL,
    ID INT NOT NULL UNIQUE,
    CONSTRAINT PK_Aluno PRIMARY KEY (n_matricula),
    CONSTRAINT FK_Aluno FOREIGN KEY (ID)
        REFERENCES Pessoa (ID)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS telefone_aluno (
    numero VARCHAR(15) NOT NULL, 
    n_matricula CHAR(9) NOT NULL,
    CONSTRAINT PK_telefone_aluno PRIMARY KEY (numero, n_matricula),
    CONSTRAINT FK_telefone_aluno FOREIGN KEY (n_matricula)
        REFERENCES Aluno (n_matricula)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS email_aluno (
    email VARCHAR(255) NOT NULL, 
    n_matricula CHAR(9) NOT NULL,
    CONSTRAINT PK_email_aluno PRIMARY KEY (email, n_matricula),
    CONSTRAINT FK_email_aluno FOREIGN KEY (n_matricula)
        REFERENCES Aluno (n_matricula)
        ON DELETE CASCADE
);

-- Entidade Professor
CREATE TABLE IF NOT EXISTS Professor (
    CPF CHAR(11) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    data_inicio_contrato DATE NOT NULL,
    ID INT NOT NULL UNIQUE,
    CONSTRAINT PK_Professor PRIMARY KEY (CPF),
    CONSTRAINT FK_Professor FOREIGN KEY (ID)
        REFERENCES Pessoa (ID)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS telefone_professor (
    numero VARCHAR(15) NOT NULL, 
    CPF CHAR(11) NOT NULL,
    CONSTRAINT PK_telefone_professor PRIMARY KEY (numero, CPF),
    CONSTRAINT FK_telefone_professor FOREIGN KEY (CPF)
        REFERENCES Professor (CPF)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS email_professor (
    email VARCHAR(255) NOT NULL, 
    CPF CHAR(11) NOT NULL,
    CONSTRAINT PK_email_professor PRIMARY KEY (email, CPF),
    CONSTRAINT FK_email_professor FOREIGN KEY (CPF)
        REFERENCES Professor (CPF)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Professor_Substituto (
    CPF CHAR(11) NOT NULL,
    data_fim_contrato DATE NOT NULL,
    CONSTRAINT PK_Professor_Substituto PRIMARY KEY (CPF),
    CONSTRAINT FK_Professor_Substituto FOREIGN KEY (CPF)
        REFERENCES Professor (CPF)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Professor_Titular (
    CPF CHAR(11) NOT NULL,
    CONSTRAINT PK_Professor_Titular PRIMARY KEY (CPF),
    CONSTRAINT FK_Professor_Titular FOREIGN KEY (CPF)
        REFERENCES Professor (CPF)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Coordenador (
    CPF CHAR(11) NOT NULL,
    CONSTRAINT PK_Coordenador PRIMARY KEY (CPF),
    CONSTRAINT FK_Coordenador FOREIGN KEY (CPF)
        REFERENCES Professor_Titular (CPF)
        ON DELETE CASCADE
);

-- Entidade Area_Interesse
CREATE TABLE IF NOT EXISTS Area_Interesse (
    ID INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    descricao VARCHAR(500),
    CONSTRAINT PK_Area_Interesse PRIMARY KEY (codigo)
);

-- Entidade Disciplina
CREATE TABLE IF NOT EXISTS Disciplina (
    codigo CHAR(6) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    codigo_curso INT NOT NULL,
    CONSTRAINT PK_Disciplina PRIMARY KEY (codigo),
    CONSTRAINT FK_Disciplina FOREIGN KEY (codigo_curso)
        REFERENCES Curso (codigo)
);

-- Entidade Turma
CREATE TABLE IF NOT EXISTS Turma (
    ID INT NOT NULL AUTO_INCREMENT,
    data_inicio DATE NOT NULL,
    codigo INT NOT NULL,
    CPF CHAR(11) NULL,
    CONSTRAINT PK_Turma PRIMARY KEY (ID),
    CONSTRAINT FK_Turma_codigo FOREIGN KEY (codigo)
        REFERENCES Disciplina (codigo)
        ON DELETE CASCADE,
    CONSTRAINT FK_Turma_codigo FOREIGN KEY (CPF)
        REFERENCES Professor (CPF)
);

CREATE TABLE IF NOT EXISTS horarios (
    sala char(3) NOT NULL,
    dia INT NOT NULL, -- Seg = 1, Ter = 2, Qua = 3, Qui = 4, Sex = 5, Sab = 6
    horario INT NOT NULL, -- Cada dia é dividido em 12 Horarios de 50 min, de 1° a 12°
    ID INT NOT NULL,
    CONSTRAINT PK_horarios PRIMARY KEY (sala, dia, horario),
    CONSTRAINT FK_horarios FOREIGN KEY (ID)
        REFERENCES Turma (ID)
        ON DELETE CASCADE
);

-- Entidade Fraca Avaliação
CREATE TABLE IF NOT EXISTS Avaliacao (
    ID INT NOT NULL,
    data_aplicacao DATE NOT NULL,
    nota_maxima FLOAT NOT NULL,
    CONSTRAINT PK_Avaliacao PRIMARY KEY (ID, data_aplicacao),
    CONSTRAINT FK_Avaliacao FOREIGN KEY (ID)
        REFERENCES Turma (ID)
        ON DELETE CASCADE
);

-- Relacionamentos
CREATE TABLE IF NOT EXISTS coordena (
    CPF CHAR(11) NOT NULL,
    codigo INT NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    CONSTRAINT PK_coordena PRIMARY KEY (CPF, codigo),
    CONSTRAINT FK_coordena_CPF FOREIGN KEY (CPF)
        REFERENCES Coordenador (CPF),
    CONSTRAINT FK_coordena_codigo FOREIGN KEY (codigo)
        REFERENCES Curso (codigo)
);

CREATE TABLE IF NOT EXISTS area_do (
    ID INT NOT NULL,
    codigo INT NOT NULL,
    CONSTRAINT PK_area_do PRIMARY KEY (ID, codigo),
    CONSTRAINT FK_area_do_ID FOREIGN KEY (ID)
        REFERENCES Area_Interesse (ID)
        ON DELETE CASCADE,
    CONSTRAINT FK_area_do_codigo FOREIGN KEY (codigo)
        REFERENCES Curso (codigo)
);

CREATE TABLE IF NOT EXISTS se_interessa (
    ID INT NOT NULL,
    CPF CHAR(11) NOT NULL,
    CONSTRAINT PK_se_interessa PRIMARY KEY (ID, CPF),
    CONSTRAINT FK_se_interessa_ID FOREIGN KEY (ID)
        REFERENCES Area_Interesse (ID)
        ON DELETE CASCADE,
    CONSTRAINT FK_se_interessa_CPF FOREIGN KEY (CPF)
        REFERENCES Professor_Titular (CPF)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS possui (
    n_matricula CHAR(9) NOT NULL,
    ID INT NOT NULL,
    data_aplicacao DATE NOT NULL,
    nota FLOAT NOT NULL,
    CONSTRAINT PK_possui PRIMARY KEY (n_matricula, ID, data_aplicacao),
    CONSTRAINT FK_possui_n_matricula FOREIGN KEY (n_matricula)
        REFERENCES Aluno (n_matricula)
        ON DELETE CASCADE,
    CONSTRAINT FK_possui_id_data FOREIGN KEY (ID, data_aplicacao)
        REFERENCES Avaliacao (ID, data_aplicacao)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS participa (
    n_matricula CHAR(9) NOT NULL,
    ID INT NOT NULL,
    presenca FLOAT NOT NULL,
    nota_total FLOAT NOT NULL,
    CONSTRAINT PK_participa PRIMARY KEY (n_matricula, ID),
    CONSTRAINT FK_participa_n_matricula FOREIGN KEY (n_matricula)
        REFERENCES Aluno (n_matricula)
        ON DELETE CASCADE,
    CONSTRAINT FK_participa_id FOREIGN KEY (ID)
        REFERENCES Turma (ID)
);