-- Criar dominios
CREATE DOMAIN d_coeficiente AS FLOAT
CHECK (VALUE >= 0 AND VALUE <= 10);

CREATE DOMAIN d_dia AS INT
CHECK (VALUE >= 0 AND VALUE < 7);

CREATE DOMAIN d_horario AS INT
CHECK (VALUE >= 0 AND VALUE < 12);

-- Entidade Curso
CREATE TABLE IF NOT EXISTS curso (
    codigo SERIAL,
    nome VARCHAR(255) NOT NULL,
    CONSTRAINT pk_curso PRIMARY KEY (codigo)
);

CREATE TABLE IF NOT EXISTS telefone_curso (
    numero VARCHAR(15) NOT NULL, 
    codigo INT NOT NULL,
    CONSTRAINT pk_telefone_curso PRIMARY KEY (numero, codigo),
    CONSTRAINT fk_telefone_curso FOREIGN KEY (codigo)
        REFERENCES curso (codigo)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS email_curso (
    email VARCHAR(255) NOT NULL, 
    codigo INT NOT NULL,
    CONSTRAINT pk_email_curso PRIMARY KEY (email, codigo),
    CONSTRAINT fk_email_curso FOREIGN KEY (codigo)
        REFERENCES curso (codigo)
        ON DELETE CASCADE
);

-- União Pessoa
CREATE TABLE IF NOT EXISTS pessoa (
    id SERIAL,
    codigo INT NOT NULL,
    CONSTRAINT pk_pessoa PRIMARY KEY (id),
    CONSTRAINT fk_pessoa FOREIGN KEY (codigo)
        REFERENCES curso (codigo)
);

-- Entidade Aluno
CREATE TABLE IF NOT EXISTS aluno (
    n_matricula CHAR(9) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    data_matricula DATE NOT NULL,
    id INT NOT NULL UNIQUE,
    CONSTRAINT pk_aluno PRIMARY KEY (n_matricula),
    CONSTRAINT fk_aluno FOREIGN KEY (id)
        REFERENCES pessoa (id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS telefone_aluno (
    numero VARCHAR(15) NOT NULL, 
    n_matricula CHAR(9) NOT NULL,
    CONSTRAINT pk_telefone_aluno PRIMARY KEY (numero, n_matricula),
    CONSTRAINT fk_telefone_aluno FOREIGN KEY (n_matricula)
        REFERENCES aluno (n_matricula)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS email_aluno (
    email VARCHAR(255) NOT NULL, 
    n_matricula CHAR(9) NOT NULL,
    CONSTRAINT pk_email_aluno PRIMARY KEY (email, n_matricula),
    CONSTRAINT fk_email_aluno FOREIGN KEY (n_matricula)
        REFERENCES aluno (n_matricula)
        ON DELETE CASCADE
);

-- Entidade Professor
CREATE TABLE IF NOT EXISTS professor (
    cpf CHAR(11) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    data_inicio_contrato DATE NOT NULL,
    id INT NOT NULL UNIQUE,
    CONSTRAINT pk_professor PRIMARY KEY (cpf),
    CONSTRAINT fk_professor FOREIGN KEY (id)
        REFERENCES pessoa (id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS telefone_professor (
    numero VARCHAR(15) NOT NULL, 
    cpf CHAR(11) NOT NULL,
    CONSTRAINT pk_telefone_professor PRIMARY KEY (numero, cpf),
    CONSTRAINT fk_telefone_professor FOREIGN KEY (cpf)
        REFERENCES professor (cpf)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS email_professor (
    email VARCHAR(255) NOT NULL, 
    cpf CHAR(11) NOT NULL,
    CONSTRAINT pk_email_professor PRIMARY KEY (email, cpf),
    CONSTRAINT fk_email_professor FOREIGN KEY (cpf)
        REFERENCES professor (cpf)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS professor_substituto (
    cpf CHAR(11) NOT NULL,
    data_fim_contrato DATE NOT NULL,
    CONSTRAINT pk_professor_substituto PRIMARY KEY (cpf),
    CONSTRAINT fk_professor_substituto FOREIGN KEY (cpf)
        REFERENCES professor (cpf)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS professor_titular (
    cpf CHAR(11) NOT NULL,
    CONSTRAINT pk_professor_titular PRIMARY KEY (cpf),
    CONSTRAINT fk_professor_titular FOREIGN KEY (cpf)
        REFERENCES professor (cpf)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS coordenador (
    cpf CHAR(11) NOT NULL,
    codigo INT NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL,
    CONSTRAINT pk_coordenador PRIMARY KEY (cpf),
    CONSTRAINT fk_coordenador_cpf FOREIGN KEY (cpf)
        REFERENCES professor_titular (cpf)
        ON DELETE CASCADE,
    CONSTRAINT fk_coordenador_codigo FOREIGN KEY (codigo)
        REFERENCES curso (codigo)
        ON DELETE CASCADE
);

-- Entidade Area_Interesse
CREATE TABLE IF NOT EXISTS area_interesse (
    id SERIAL,
    nome VARCHAR(255) NOT NULL,
    descricao VARCHAR(500),
    CONSTRAINT pk_area_interesse PRIMARY KEY (id)
);

-- Entidade Disciplina
CREATE TABLE IF NOT EXISTS disciplina (
    codigo CHAR(6) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    codigo_curso INT NOT NULL,
    CONSTRAINT pk_disciplina PRIMARY KEY (codigo),
    CONSTRAINT fk_disciplina FOREIGN KEY (codigo_curso)
        REFERENCES curso (codigo)
        ON DELETE CASCADE
);

-- Entidade Turma
CREATE TABLE IF NOT EXISTS turma (
    id SERIAL,
    data_inicio DATE NOT NULL,
    codigo CHAR(6) NOT NULL,
    cpf CHAR(11) NULL,
    CONSTRAINT pk_turma PRIMARY KEY (id),
    CONSTRAINT fk_turma_codigo FOREIGN KEY (codigo)
        REFERENCES disciplina (codigo)
        ON DELETE CASCADE,
    CONSTRAINT fk_turma_cpf FOREIGN KEY (cpf)
        REFERENCES professor (cpf)
);

CREATE TABLE IF NOT EXISTS horarios (
    sala char(3) NOT NULL,
    dia d_dia NOT NULL, -- Seg = 0, Ter = 1, Qua = 2, Qui = 3, Sex = 4, Sab = 5, Dom = 6
    horario d_horario NOT NULL, -- Cada dia é dividido em 12 Horarios de 50 min, de 0 a 11
    id INT NOT NULL,
    CONSTRAINT pk_horarios PRIMARY KEY (sala, dia, horario),
    CONSTRAINT fk_horarios FOREIGN KEY (id)
        REFERENCES turma (id)
        ON DELETE CASCADE
);

-- Entidade Fraca Avaliação
CREATE TABLE IF NOT EXISTS avaliacao (
    id INT NOT NULL,
    data_aplicacao DATE NOT NULL,
    nota_maxima d_coeficiente NOT NULL,
    CONSTRAINT pk_avaliacao PRIMARY KEY (id, data_aplicacao),
    CONSTRAINT fk_avaliacao FOREIGN KEY (id)
        REFERENCES turma (id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS area_do (
    id INT NOT NULL,
    codigo INT NOT NULL,
    CONSTRAINT pk_area_do PRIMARY KEY (id, codigo),
    CONSTRAINT fk_area_do_id FOREIGN KEY (id)
        REFERENCES area_interesse (id)
        ON DELETE CASCADE,
    CONSTRAINT fk_area_do_codigo FOREIGN KEY (codigo)
        REFERENCES curso (codigo)
);

CREATE TABLE IF NOT EXISTS se_interessa (
    id INT NOT NULL,
    cpf CHAR(11) NOT NULL,
    CONSTRAINT pk_se_interessa PRIMARY KEY (id, cpf),
    CONSTRAINT fk_se_interessa_id FOREIGN KEY (id)
        REFERENCES area_interesse (id)
        ON DELETE CASCADE,
    CONSTRAINT fk_se_interessa_cpf FOREIGN KEY (cpf)
        REFERENCES professor_titular (cpf)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS possui (
    n_matricula CHAR(9) NOT NULL,
    id INT NOT NULL,
    data_aplicacao DATE NOT NULL,
    nota d_coeficiente NOT NULL,
    CONSTRAINT pk_possui PRIMARY KEY (n_matricula, id, data_aplicacao),
    CONSTRAINT fk_possui_n_matricula FOREIGN KEY (n_matricula)
        REFERENCES aluno (n_matricula)
        ON DELETE CASCADE,
    CONSTRAINT fk_possui_id_data FOREIGN KEY (id, data_aplicacao)
        REFERENCES avaliacao (id, data_aplicacao)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS participa (
    n_matricula CHAR(9) NOT NULL,
    id INT NOT NULL,
    presenca d_coeficiente NOT NULL,
    nota_total d_coeficiente NOT NULL,
    CONSTRAINT pk_participa PRIMARY KEY (n_matricula, id),
    CONSTRAINT fk_participa_n_matricula FOREIGN KEY (n_matricula)
        REFERENCES aluno (n_matricula)
        ON DELETE CASCADE,
    CONSTRAINT fk_participa_id FOREIGN KEY (id)
        REFERENCES turma (id)
        ON DELETE CASCADE
);