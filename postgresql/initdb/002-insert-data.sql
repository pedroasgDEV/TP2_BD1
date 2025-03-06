-- Inserção de Cursos
INSERT INTO Curso (codigo, nome) VALUES 
(1, 'Engenharia de Software'),
(2, 'Ciência da Computação'),
(3, 'Matemática');

-- Inserção de Telefones e Emails dos Cursos
INSERT INTO telefone_curso (numero, codigo) VALUES 
('1111-1111', 1),
('2222-2222', 2),
('3333-3333', 3);

INSERT INTO email_curso (email, codigo) VALUES 
('engsoft@universidade.com', 1),
('ccomp@universidade.com', 2),
('mat@universidade.com', 3);

INSERT INTO Pessoa (ID, codigo) VALUES
(1, 1), (2, 2), (3, 3), (4, 1), (5, 2), (6, 3),
(7, 1), (8, 2), (9, 3), (10, 1), (11, 2), (12, 3),
(13, 1), (14, 2), (15, 3), (16, 1), (17, 2), (18, 3);

-- Inserção de Alunos
INSERT INTO Aluno (n_matricula, nome, data_matricula, ID) VALUES 
('202300001', 'Alice Souza', '2023-02-15', 1),
('202300002', 'Bruno Lima', '2023-02-16', 2),
('202300003', 'Carla Mendes', '2023-02-17', 3),
('202300004', 'Pedro Augusto', '2023-02-18', 4),
('202300005', 'Maria Clara', '2023-02-19', 5),
('202300006', 'João Henrrique', '2023-02-20', 6),
('202300007', 'Mauricio Lopes', '2023-02-21', 7),
('202300008', 'Sofia Gonçalves', '2023-02-22', 8),
('202300009', 'Miguel Sousa', '2023-02-23', 9);

-- Telefones e Emails dos Alunos
INSERT INTO telefone_aluno (numero, n_matricula) VALUES 
('9999-0001', '202300001'),
('9999-0002', '202300002'),
('9999-0003', '202300003'),
('9999-0004', '202300004'),
('9999-0005', '202300005'),
('9999-0006', '202300006'),
('9999-0007', '202300007'),
('9999-0008', '202300008'),
('9999-0009', '202300009');

INSERT INTO email_aluno (email, n_matricula) VALUES 
('alice@exemplo.com', '202300001'),
('bruno@exemplo.com', '202300002'),
('carla@exemplo.com', '202300003'),
('pedro@exemplo.com', '202300004'),
('maria@exemplo.com', '202300005'),
('joao@exemplo.com', '202300006'),
('mauricio@exemplo.com', '202300007'),
('sofia@exemplo.com', '202300008'),
('miguel@exemplo.com', '202300009');

-- Inserção de Professores
INSERT INTO Professor (CPF, nome, data_inicio_contrato, ID) VALUES 
('11111111111', 'Dr. Marcos Silva', '2020-03-01', 10),
('22222222222', 'Dra. Fernanda Costa', '2019-04-10', 11),
('33333333333', 'Dr. João Pereira', '2018-05-20', 12),
('44444444444', 'Dra. Zildete Lopes', '2020-03-02', 13),
('55555555555', 'Dr. Guilherme Neves', '2015-04-10', 14),
('66666666666', 'Dra. Clara Lopes', '2011-05-20', 15),
('77777777777', 'Dr. João Augusto', '2023-03-01', 16),
('88888888888', 'Dr. Fernando Neves', '2024-04-10', 17),
('99999999999', 'Dr. Luiz Henrrique', '2018-05-21', 18);

-- Telefones e Emails dos Professores
INSERT INTO telefone_professor (numero, CPF) VALUES 
('8888-0001', '11111111111'),
('8888-0002', '22222222222'),
('8888-0003', '33333333333'),
('8888-0004', '44444444444'),
('8888-0005', '55555555555'),
('8888-0006', '66666666666'),
('8888-0007', '77777777777'),
('8888-0008', '88888888888'),
('8888-0009', '99999999999');

INSERT INTO email_professor (email, CPF) VALUES 
('marcos@universidade.com', '11111111111'),
('fernanda@universidade.com', '22222222222'),
('joao_per@universidade.com', '33333333333'),
('zildete@universidade.com', '44444444444'),
('guilherme@universidade.com', '55555555555'),
('clara@universidade.com', '66666666666'),
('joao_aug@universidade.com', '77777777777'),
('fernando@universidade.com', '88888888888'),
('luiz@universidade.com', '99999999999');

-- Especialização Professores
INSERT INTO Professor_Substituto (CPF, data_fim_contrato) VALUES
('11111111111', '2021-03-01'),
('22222222222', '2020-04-10'),
('33333333333', '2019-05-20');

INSERT INTO Professor_Titular (CPF) VALUES
('44444444444'), ('55555555555'), ('66666666666'),
('77777777777'), ('88888888888'), ('99999999999');

INSERT INTO Coordenador (CPF) VALUES
('44444444444'), ('55555555555'), ('66666666666');

-- Inserção de Areas de Interesse
INSERT INTO Area_Interesse (ID, nome) VALUES
(1, 'Inteligencia Artificial'),
(2, 'Otimização'),
(3, 'Modelagem Matematica');

-- Inserção de Disciplinas
INSERT INTO Disciplina (codigo, nome, codigo_curso) VALUES 
('ENG001', 'Banco de Dados', 1),
('BCC002', 'Estrutura de Dados', 2),
('MAT003', 'Calculo 3', 3);

-- Inserção de Turmas e horarios
INSERT INTO Turma (ID, data_inicio, codigo, CPF) VALUES 
(1, '2024-01-15', 'ENG001', '77777777777'),
(2, '2024-02-10', 'BCC002', '88888888888'),
(3, '2024-03-05', 'MAT003', '99999999999');

INSERT INTO horarios (sala, dia, horario, ID) VALUES 
('201', 1, 1, 1),
('202', 1, 1, 2),
('203', 1, 1, 3);

-- Inserção de Avaliações
INSERT INTO Avaliacao (ID, data_aplicacao, nota_maxima) VALUES 
(1, '2024-06-10', 4.0),
(2, '2024-06-15', 3.0),
(3, '2024-06-20', 6.0);

-- Inserção de Relacionamentos
INSERT INTO coordena (CPF, codigo, data_inicio, data_fim) VALUES
('44444444444', 1, '2021-03-02', '2022-03-02'),
('55555555555', 2, '2016-04-10', '2017-04-10'),
('66666666666', 3, '2012-05-20', '2013-05-20');

INSERT INTO area_do (ID, codigo) VALUES
(1, 1), (2, 2), (3, 3);

INSERT INTO se_interessa (ID, CPF) VALUES
(1, '44444444444'), (2, '55555555555'), (3, '66666666666'),
(1, '77777777777'), (2, '88888888888'), (3, '99999999999');

INSERT INTO possui (n_matricula, ID, data_aplicacao, nota) VALUES
('202300001', 1, '2024-06-10', 4.0),
('202300002', 2, '2024-06-15', 1.5),
('202300003', 3, '2024-06-20', 5.0),
('202300004', 1, '2024-06-10', 3.0),
('202300005', 2, '2024-06-15', 3.0),
('202300006', 3, '2024-06-20', 6.0),
('202300007', 1, '2024-06-10', 1.0),
('202300008', 2, '2024-06-15', 2.0),
('202300009', 3, '2024-06-20', 2.0);

INSERT INTO participa (n_matricula, ID, presenca, nota_total) VALUES
('202300001', 1, 1.00, 4.0),
('202300002', 2, 0.65, 1.5),
('202300003', 3, 0.78, 5.0),
('202300004', 1, 0.95, 3.0),
('202300005', 2, 0.98, 3.0),
('202300006', 3, 0.56, 6.0),
('202300007', 1, 0.00, 1.0),
('202300008', 2, 0.87, 2.0),
('202300009', 3, 0.80, 2.0);