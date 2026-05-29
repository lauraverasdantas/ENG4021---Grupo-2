
-- 1. USUARIOS
--    Armazena os dados de cadastro e autenticação do usuário

CREATE TABLE Usuarios (
    ID_Usuario      INT           PRIMARY KEY AUTO_INCREMENT,
    Nome            VARCHAR(100)  NOT NULL,
    Email           VARCHAR(150)  NOT NULL UNIQUE,
    Senha_Hash      VARCHAR(255)  NOT NULL,
    Data_Criacao    DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Exemplo de registros:
-- INSERT INTO Usuarios (Nome, Email, Senha_Hash, Data_Criacao) VALUES
-- ('João Silva', 'joao@email.com', '*df8923h...', '2026-04-10 00:00:00'),
-- ('Ana Costa',  'ana@email.com',  '*h3289fj...', '2026-04-11 00:00:00');



-- 2. REGISTROS_HUMOR
--    Cada entrada do diário: nível de ansiedade, emoji de humor
--    e texto livre escrito pelo usuário naquele momento

CREATE TABLE Registros_Humor (
    ID_Registro         INT           PRIMARY KEY AUTO_INCREMENT,
    ID_Usuario          INT           NOT NULL,
    Data_Hora           DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Nivel_Ansiedade     TINYINT       NOT NULL CHECK (Nivel_Ansiedade BETWEEN 1 AND 10),
    Humor_Emoji         TINYINT       NOT NULL CHECK (Humor_Emoji BETWEEN 1 AND 9),
    -- Referência aos emojis:
    -- 1=Normal  2=Triste  3=Feliz  4=Esperançoso  5=Raivoso
    -- 6=Apaixonado  7=Preocupado  8=Ansioso  9=Entediado
    Texto_Livre         TEXT,

    CONSTRAINT fk_registro_usuario
        FOREIGN KEY (ID_Usuario) REFERENCES Usuarios(ID_Usuario)
        ON DELETE CASCADE
);

-- Exemplo de registros:
-- INSERT INTO Registros_Humor (ID_Usuario, Data_Hora, Nivel_Ansiedade, Humor_Emoji, Texto_Livre) VALUES
-- (1, '2026-04-10 09:00:00', 3, 1, 'Acordei bem, tomei café tranquilo.'),
-- (1, '2026-04-10 14:30:00', 8, 7, 'Muita matéria acumulada, prova de Álgebra Linear chegando...');



-- 3. TAGS
--    Categorias/gatilhos que o usuário pode associar a um
--    registro (ex: "Dormiu Pouco", "Reunião Longa")

CREATE TABLE Tags (
    ID_Tag      INT          PRIMARY KEY AUTO_INCREMENT,
    Nome_Tag    VARCHAR(100) NOT NULL,
    Categoria   VARCHAR(100) NOT NULL
    -- Categorias sugeridas: Físico/Sono, Alimentação, Trabalho/Estudo, Rotina
);

-- Exemplo de registros:
-- INSERT INTO Tags (Nome_Tag, Categoria) VALUES
-- ('Dormiu Pouco',      'Físico / Sono'),
-- ('Excesso de Cafeína','Alimentação'),
-- ('Reunião Longa',     'Trabalho / Estudo'),
-- ('Trânsito',          'Rotina');



-- 4. REGISTROS_TAGS  (tabela associativa N:N)
--    Liga um registro de humor a uma ou mais tags/gatilhos

CREATE TABLE Registros_Tags (
    ID_Registro INT NOT NULL,
    ID_Tag      INT NOT NULL,

    PRIMARY KEY (ID_Registro, ID_Tag),

    CONSTRAINT fk_rt_registro
        FOREIGN KEY (ID_Registro) REFERENCES Registros_Humor(ID_Registro)
        ON DELETE CASCADE,

    CONSTRAINT fk_rt_tag
        FOREIGN KEY (ID_Tag) REFERENCES Tags(ID_Tag)
        ON DELETE CASCADE
);



-- 5. CONTATOS_CONFIANCA
--    Pessoas ou profissionais que o usuário pode acionar
--    no Modo Crise (amigo, familiar, psicólogo etc.)

CREATE TABLE Contatos_Confianca (
    ID_Contato  INT          PRIMARY KEY AUTO_INCREMENT,
    ID_Usuario  INT          NOT NULL,
    Nome_Contato VARCHAR(100) NOT NULL,
    Telefone    VARCHAR(20)  NOT NULL,
    Relacao     VARCHAR(80),
    -- Ex: 'Psicólogo', 'Namorada', 'Amigo', 'Familiar'

    CONSTRAINT fk_contato_usuario
        FOREIGN KEY (ID_Usuario) REFERENCES Usuarios(ID_Usuario)
        ON DELETE CASCADE
);

-- Exemplo de registros:
-- INSERT INTO Contatos_Confianca (ID_Usuario, Nome_Contato, Telefone, Relacao) VALUES
-- (1, 'Dr. Roberto', '(21) 99999-1111', 'Psicólogo'),
-- (1, 'Maria',       '(21) 98888-2222', 'Namorada');



-- 6. INTERVENCOES
--    Biblioteca de técnicas e exercícios oferecidos pelo app
--    (respiração, mindfulness, ancoragem etc.)

CREATE TABLE Intervencoes (
    ID_Intervencao  INT           PRIMARY KEY AUTO_INCREMENT,
    Titulo          VARCHAR(150)  NOT NULL,
    Tipo            VARCHAR(100)  NOT NULL,
    -- Ex: 'Exercício Respiratório', 'Ancoragem (Mindfulness)',
    --     'Desafio Diário', 'Modo Crise'
    Conteudo        TEXT          NOT NULL
);

-- Exemplo de registros:
-- INSERT INTO Intervencoes (Titulo, Tipo, Conteudo) VALUES
-- ('Respiração 4-7-8',    'Exercício Respiratório',      'Inspire por 4s, segure por 7s, expire por 8s...'),
-- ('Técnica 5-4-3-2-1',  'Ancoragem (Mindfulness)',     'Encontre 5 coisas que você pode ver, 4 que pode tocar...');



-- 7. HISTORICO_INTERVENCOES
--    Registra quais intervenções foram usadas por cada usuário
--    e em qual momento, permitindo análise de padrões

CREATE TABLE Historico_Intervencoes (
    ID_Historico    INT      PRIMARY KEY AUTO_INCREMENT,
    ID_Usuario      INT      NOT NULL,
    ID_Intervencao  INT      NOT NULL,
    ID_Registro     INT,     -- registro de humor que disparou a intervenção (opcional)
    Data_Hora       DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    Concluida       BOOLEAN  NOT NULL DEFAULT FALSE,

    CONSTRAINT fk_hi_usuario
        FOREIGN KEY (ID_Usuario)     REFERENCES Usuarios(ID_Usuario)      ON DELETE CASCADE,
    CONSTRAINT fk_hi_intervencao
        FOREIGN KEY (ID_Intervencao) REFERENCES Intervencoes(ID_Intervencao) ON DELETE CASCADE,
    CONSTRAINT fk_hi_registro
        FOREIGN KEY (ID_Registro)    REFERENCES Registros_Humor(ID_Registro)  ON DELETE SET NULL
);



-- 8. DESAFIOS_DIARIOS
--    Pequenas ações sugeridas pelo app no dia a dia
--    (ex: "Respire por 3 min", "Reduza 30 min de celular")

CREATE TABLE Desafios_Diarios (
    ID_Desafio  INT          PRIMARY KEY AUTO_INCREMENT,
    Titulo      VARCHAR(150) NOT NULL,
    Descricao   TEXT,
    Categoria   VARCHAR(80)
    -- Ex: 'Respiração', 'Sono', 'Movimento', 'Tela'
);



-- 9. USUARIO_DESAFIOS  (adesão do usuário aos desafios)
--    Registra se o usuário aceitou/completou cada desafio

CREATE TABLE Usuario_Desafios (
    ID_Usuario      INT      NOT NULL,
    ID_Desafio      INT      NOT NULL,
    Data_Aceite     DATE     NOT NULL,
    Concluido       BOOLEAN  NOT NULL DEFAULT FALSE,
    Data_Conclusao  DATE,

    PRIMARY KEY (ID_Usuario, ID_Desafio, Data_Aceite),

    CONSTRAINT fk_ud_usuario
        FOREIGN KEY (ID_Usuario)  REFERENCES Usuarios(ID_Usuario)        ON DELETE CASCADE,
    CONSTRAINT fk_ud_desafio
        FOREIGN KEY (ID_Desafio)  REFERENCES Desafios_Diarios(ID_Desafio) ON DELETE CASCADE
);



-- ÍNDICES — aceleram as consultas mais comuns do app


-- Buscar todos os registros de um usuário em ordem cronológica
CREATE INDEX idx_registros_usuario_data
    ON Registros_Humor (ID_Usuario, Data_Hora DESC);

-- Detectar padrões: registros com ansiedade alta
CREATE INDEX idx_registros_nivel
    ON Registros_Humor (ID_Usuario, Nivel_Ansiedade);

-- Histórico de intervenções por usuário
CREATE INDEX idx_historico_usuario
    ON Historico_Intervencoes (ID_Usuario, Data_Hora DESC);



