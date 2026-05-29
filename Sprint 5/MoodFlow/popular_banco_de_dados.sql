
-- 
-- 1. USUARIOS
-- 
INSERT INTO Usuarios (Nome, Email, Senha_Hash, Data_Criacao) VALUES
('João Silva',    'joao@email.com',    '$2b$12$df8923hXkL9mNpQrStUvWx',  '2026-04-10 08:00:00'),
('Ana Costa',     'ana@email.com',     '$2b$12$h3289fjYzAbCdEfGhIjKlM',  '2026-04-11 09:15:00'),
('Lucas Mendes',  'lucas@email.com',   '$2b$12$kL7p2qRsTuVwXyZaB3cDeF',  '2026-04-12 10:30:00'),
('Mariana Lima',  'mari@email.com',    '$2b$12$nOpQrStUvWxYzAbCdEfGhI',  '2026-04-13 14:00:00'),
('Pedro Rocha',   'pedro@email.com',   '$2b$12$jKlMnOpQrStUvWxYzAbCdE',  '2026-04-14 16:45:00');


-- 
-- 2. TAGS (gatilhos / contextos)
-- 
INSERT INTO Tags (Nome_Tag, Categoria) VALUES
-- Físico / Sono
('Dormiu Pouco',         'Físico / Sono'),
('Dormiu Bem',           'Físico / Sono'),
('Dor de Cabeça',        'Físico / Sono'),
('Cansaço Físico',       'Físico / Sono'),
-- Alimentação
('Excesso de Cafeína',   'Alimentação'),
('Pulou Refeição',       'Alimentação'),
('Comeu Bem',            'Alimentação'),
-- Trabalho / Estudo
('Reunião Longa',        'Trabalho / Estudo'),
('Prova ou Entrega',     'Trabalho / Estudo'),
('Muito Conteúdo',       'Trabalho / Estudo'),
('Dia Produtivo',        'Trabalho / Estudo'),
-- Rotina
('Trânsito',             'Rotina'),
('Exercitou-se',         'Rotina'),
('Saiu com Amigos',      'Rotina'),
('Ficou em Casa',        'Rotina'),
-- Emocional
('Discussão',            'Emocional'),
('Notícias Ruins',       'Emocional'),
('Momento de Lazer',     'Emocional'),
('Meditou',              'Emocional');


-- 
-- 3. CONTATOS_CONFIANCA
-- 
INSERT INTO Contatos_Confianca (ID_Usuario, Nome_Contato, Telefone, Relacao) VALUES
-- João
(1, 'Dra. Fernanda (Psicóloga)', '(21) 99999-1111', 'Psicóloga'),
(1, 'Maria (Namorada)',          '(21) 98888-2222', 'Namorada'),
(1, 'Carlos (Irmão)',            '(21) 97777-3333', 'Familiar'),
-- Ana
(2, 'Dr. Roberto (Psiquiatra)', '(21) 96666-4444', 'Psiquiatra'),
(2, 'Juliana (Melhor Amiga)',   '(21) 95555-5555', 'Amiga'),
-- Lucas
(3, 'Dr. Paulo (Psicólogo)',    '(11) 94444-6666', 'Psicólogo'),
(3, 'Renata (Mãe)',             '(11) 93333-7777', 'Familiar'),
-- Mariana
(4, 'Beatriz (Amiga)',          '(21) 92222-8888', 'Amiga'),
-- Pedro
(5, 'Dra. Camila (Psicóloga)', '(21) 91111-9999', 'Psicóloga'),
(5, 'Rafael (Pai)',             '(21) 90000-1010', 'Familiar');


-- 
-- 4. INTERVENCOES
-- 
INSERT INTO Intervencoes (Titulo, Tipo, Conteudo) VALUES
-- Exercícios Respiratórios
('Respiração 4-7-8',
 'Exercício Respiratório',
 'Inspire pelo nariz por 4 segundos. Segure o ar por 7 segundos. Expire lentamente pela boca por 8 segundos. Repita 4 vezes. Essa técnica ativa o sistema nervoso parassimpático e reduz a ansiedade rapidamente.'),

('Respiração Quadrada',
 'Exercício Respiratório',
 'Inspire por 4 segundos. Segure por 4 segundos. Expire por 4 segundos. Segure por 4 segundos. Repita o ciclo por 2 a 3 minutos. Muito usada por atletas e militares para controle do estresse.'),

('Respiração Diafragmática',
 'Exercício Respiratório',
 'Deite-se ou sente-se confortavelmente. Coloque uma mão no peito e outra na barriga. Inspire pelo nariz, sentindo a barriga expandir (não o peito). Expire devagar pela boca. Faça por 5 minutos.'),

-- Ancoragem / Mindfulness
('Técnica 5-4-3-2-1',
 'Ancoragem (Mindfulness)',
 'Nomeie 5 coisas que você pode VER. 4 coisas que pode TOCAR. 3 coisas que pode OUVIR. 2 coisas que pode CHEIRAR. 1 coisa que pode SABOREAR. Essa técnica traz sua mente de volta ao momento presente.'),

('Escaneamento Corporal',
 'Ancoragem (Mindfulness)',
 'Feche os olhos e respire fundo. Comece pelos pés: sinta cada parte do corpo lentamente subindo até a cabeça. Observe tensões sem julgamento. Ao identificar um ponto tenso, respire e solte a tensão ao expirar.'),

('Observação de Pensamentos',
 'Ancoragem (Mindfulness)',
 'Imagine seus pensamentos como nuvens passando no céu. Você é o céu — tranquilo e estável. Não lute contra os pensamentos, apenas observe-os passando. Permaneça como observador por 5 a 10 minutos.'),

-- Modo Crise
('Passo a Passo Crise de Ansiedade',
 'Modo Crise',
 '1. PARE o que está fazendo. 2. Sente-se ou deite-se em local seguro. 3. Respire: inspire 4s, expire 6s. 4. Diga em voz alta: "Estou seguro(a). Isso vai passar." 5. Use a técnica 5-4-3-2-1. 6. Se não melhorar em 10 min, acione seu contato de confiança.'),

('Frase de Ancoragem',
 'Modo Crise',
 'Repita lentamente, em voz alta ou mentalmente: "Eu estou aqui. Eu estou seguro(a). Esse sentimento é temporário. Eu já superei isso antes e vou superar agora." Faça isso enquanto respira devagar.'),

-- Desafios Diários
('Pausa de 3 Minutos',
 'Desafio Diário',
 'Reserve 3 minutos agora para parar tudo e respirar conscientemente. Sem celular, sem tela. Apenas você e sua respiração. Configure um alarme e feche os olhos.'),

('Diário de Gratidão',
 'Desafio Diário',
 'Escreva 3 coisas pelas quais você é grato(a) hoje. Podem ser pequenas — o café da manhã, uma mensagem de um amigo, o sol pela janela. Gratidão reconecta o cérebro ao positivo.');


-- 
-- 5. DESAFIOS_DIARIOS
-- 
INSERT INTO Desafios_Diarios (Titulo, Descricao, Categoria) VALUES
('Respire por 3 minutos',
 'Faça uma pausa de 3 minutos e pratique respiração consciente. Sem telas, sem distrações.',
 'Respiração'),

('Reduza 30 min de celular',
 'Diminua 30 minutos do seu tempo de tela hoje. Use esse tempo para caminhar, ler ou descansar.',
 'Tela'),

('Durma antes da meia-noite',
 'Tente ir para a cama antes das 00h. O sono de qualidade reduz a ansiedade significativamente.',
 'Sono'),

('Tome água regularmente',
 'Beba pelo menos 2 litros de água hoje. A desidratação pode intensificar sintomas de ansiedade.',
 'Alimentação'),

('Caminhe por 15 minutos',
 'Faça uma caminhada leve de 15 minutos. Não precisa ser rápida — apenas mova o corpo.',
 'Movimento'),

('Escreva sobre seu dia',
 'Dedique 5 minutos para escrever livremente sobre como foi seu dia. Sem julgamentos.',
 'Reflexão'),

('Evite cafeína depois das 14h',
 'Não consuma café, chá preto ou energéticos após as 14h. Isso melhora o sono e reduz a ansiedade.',
 'Alimentação'),

('Conecte-se com alguém',
 'Mande mensagem ou ligue para um amigo ou familiar. Conexão social é um antídoto natural para a ansiedade.',
 'Social');


-- 
-- 6. REGISTROS_HUMOR  (histórico dos últimos 30 dias — João)
-- 
INSERT INTO Registros_Humor (ID_Usuario, Data_Hora, Nivel_Ansiedade, Humor_Emoji, Texto_Livre) VALUES
-- Semana 1
(1, '2026-04-10 08:30:00', 3, 1, 'Acordei bem, tomei café tranquilo. Dia começando com calma.'),
(1, '2026-04-10 21:00:00', 4, 2, 'Tarde um pouco pesada no trabalho, mas nada demais.'),
(1, '2026-04-11 09:00:00', 6, 7, 'Reunião inesperada logo cedo. Me senti pressionado.'),
(1, '2026-04-12 10:00:00', 8, 8, 'Muita matéria acumulada, prova de Álgebra Linear chegando. Coração acelerado.'),
(1, '2026-04-12 20:00:00', 5, 1, 'Estudei bastante, me sinto mais preparado agora.'),
(1, '2026-04-13 09:30:00', 9, 8, 'Dia da prova. Ansiedade no teto antes de entrar na sala.'),
(1, '2026-04-13 18:00:00', 4, 3, 'A prova foi melhor do que eu esperava. Aliviado!'),
(1, '2026-04-14 10:00:00', 2, 3, 'Fim de semana chegando. Me sinto leve.'),
-- Semana 2
(1, '2026-04-15 11:00:00', 3, 4, 'Passei o dia com a família. Momentos bons.'),
(1, '2026-04-16 08:00:00', 5, 7, 'Segunda-feira pesada. Difícil começar.'),
(1, '2026-04-17 09:00:00', 7, 8, 'Prazo de entrega amanhã. Trabalhando até tarde.'),
(1, '2026-04-18 08:30:00', 6, 2, 'Dormi pouco. Cansado e irritado.'),
(1, '2026-04-19 10:00:00', 4, 1, 'Entrega feita. Respirei aliviado.'),
-- Semana 3
(1, '2026-04-21 09:00:00', 3, 3, 'Fui correr pela manhã. Me sinto bem.'),
(1, '2026-04-22 20:00:00', 7, 7, 'Discussão com a namorada. Ansiedade alta à noite.'),
(1, '2026-04-23 09:00:00', 5, 1, 'Conversei com ela, resolvemos. Me sinto melhor.'),
(1, '2026-04-24 11:00:00', 2, 4, 'Dia tranquilo, fiz meditação pela manhã.'),
-- Semana 4
(1, '2026-04-28 09:00:00', 6, 8, 'Semana apertada se aproximando. Ansiedade voltando.'),
(1, '2026-04-29 21:00:00', 8, 7, 'Não consegui dormir direito. Pensamentos acelerados.'),
(1, '2026-04-30 08:30:00', 5, 1, 'Usei a respiração 4-7-8 antes de dormir. Ajudou bastante.');

-- Registros de Ana
INSERT INTO Registros_Humor (ID_Usuario, Data_Hora, Nivel_Ansiedade, Humor_Emoji, Texto_Livre) VALUES
(2, '2026-04-11 08:00:00', 4, 1, 'Primeiro dia usando o app. Acordei bem.'),
(2, '2026-04-12 20:00:00', 6, 7, 'Trabalho acumulado. Me sinto sobrecarregada.'),
(2, '2026-04-15 10:00:00', 3, 3, 'Fim de semana ótimo com amigas. Leve!'),
(2, '2026-04-20 21:00:00', 7, 8, 'Semana pesada. Ansiedade alta à noite.'),
(2, '2026-04-25 09:00:00', 5, 4, 'Fiz terapia hoje. Me sinto mais esperançosa.');

-- Registros de Lucas
INSERT INTO Registros_Humor (ID_Usuario, Data_Hora, Nivel_Ansiedade, Humor_Emoji, Texto_Livre) VALUES
(3, '2026-04-13 07:30:00', 8, 8, 'Ataque de pânico ao acordar. Usei o modo crise.'),
(3, '2026-04-13 10:00:00', 4, 1, 'Melhorou depois da respiração. Ligou para o psicólogo.'),
(3, '2026-04-20 09:00:00', 3, 3, 'Semana tranquila. Exercícios ajudando muito.');


-- 
-- 7. REGISTROS_TAGS  (ligando registros às tags)
-- 
INSERT INTO Registros_Tags (ID_Registro, ID_Tag) VALUES
-- João dia 10/04 manhã (ID 1): dormiu bem + dia produtivo
(1, 2), (1, 11),
-- João dia 10/04 noite (ID 2): reunião longa
(2, 8),
-- João dia 11/04 (ID 3): reunião longa + trânsito
(3, 8), (3, 12),
-- João dia 12/04 manhã (ID 4): prova/entrega + excesso de cafeína + dormiu pouco
(4, 9), (4, 5), (4, 1),
-- João dia 12/04 noite (ID 5): dia produtivo
(5, 11),
-- João dia 13/04 manhã - prova (ID 6): prova/entrega
(6, 9),
-- João dia 13/04 tarde (ID 7): momento de lazer
(7, 18),
-- João dia 14/04 (ID 8): momento de lazer + exercitou-se
(8, 18), (8, 13),
-- João dia 15/04 (ID 9): saiu com amigos
(9, 14),
-- João dia 17/04 (ID 11): prova/entrega + dormiu pouco
(11, 9), (11, 1),
-- João dia 18/04 (ID 12): dormiu pouco + cansaço físico
(12, 1), (12, 4),
-- João dia 21/04 (ID 14): exercitou-se
(14, 13),
-- João dia 22/04 (ID 15): discussão
(15, 16),
-- João dia 24/04 (ID 17): meditou + ficou em casa
(17, 19), (17, 15),
-- João dia 29/04 (ID 19): dormiu pouco + notícias ruins
(19, 1), (19, 17),
-- João dia 30/04 (ID 20): meditou
(20, 19);


-- 
-- 8. HISTORICO_INTERVENCOES
--    (intervenções usadas, inclusive disparadas pelo Modo Crise)
-- 
INSERT INTO Historico_Intervencoes (ID_Usuario, ID_Intervencao, ID_Registro, Data_Hora, Concluida) VALUES
-- João usou respiração 4-7-8 no dia da prova
(1, 1, 6,  '2026-04-13 08:45:00', TRUE),
-- João usou técnica 5-4-3-2-1 quando ansiedade estava 8
(1, 4, 4,  '2026-04-12 10:30:00', TRUE),
-- João usou frase de ancoragem após discussão
(1, 8, 15, '2026-04-22 20:30:00', TRUE),
-- João usou respiração 4-7-8 antes de dormir (ansiedade 8)
(1, 1, 19, '2026-04-29 22:00:00', TRUE),
-- João usou observação de pensamentos
(1, 6, 17, '2026-04-24 11:30:00', TRUE),
-- Ana usou escaneamento corporal
(2, 5, 22, '2026-04-20 21:30:00', TRUE),
-- Lucas — MODO CRISE acionado (ansiedade 8 → ataque de pânico)
(3, 7, 26, '2026-04-13 07:35:00', TRUE),
(3, 1, 26, '2026-04-13 07:40:00', TRUE),
-- Lucas usou pausa de 3 min
(3, 9, 28, '2026-04-20 09:15:00', TRUE);


-- 
-- 9. USUARIO_DESAFIOS
-- 
INSERT INTO Usuario_Desafios (ID_Usuario, ID_Desafio, Data_Aceite, Concluido, Data_Conclusao) VALUES
-- João
(1, 1, '2026-04-10', TRUE,  '2026-04-10'),  -- respirar 3 min ✓
(1, 2, '2026-04-11', TRUE,  '2026-04-11'),  -- reduzir celular ✓
(1, 5, '2026-04-12', FALSE, NULL),           -- caminhada (não concluiu)
(1, 3, '2026-04-13', TRUE,  '2026-04-13'),  -- dormir antes meia-noite ✓
(1, 6, '2026-04-14', TRUE,  '2026-04-14'),  -- escrever sobre o dia ✓
(1, 1, '2026-04-21', TRUE,  '2026-04-21'),  -- respirar 3 min ✓ (repetiu)
(1, 7, '2026-04-22', TRUE,  '2026-04-22'),  -- evitar cafeína ✓
-- Ana
(2, 1, '2026-04-11', TRUE,  '2026-04-11'),
(2, 8, '2026-04-15', TRUE,  '2026-04-15'),  -- conectar com alguém ✓
(2, 6, '2026-04-20', FALSE, NULL),
-- Lucas
(3, 1, '2026-04-13', TRUE,  '2026-04-13'),
(3, 4, '2026-04-14', TRUE,  '2026-04-14'),  -- beber água ✓
(3, 5, '2026-04-20', TRUE,  '2026-04-20'),  -- caminhada ✓
-- Mariana
(4, 3, '2026-04-13', TRUE,  '2026-04-13'),
(4, 6, '2026-04-14', FALSE, NULL),
-- Pedro
(5, 2, '2026-04-14', TRUE,  '2026-04-14'),
(5, 5, '2026-04-15', TRUE,  '2026-04-15');


-- 
-- VERIFICAÇÃO — consultas para conferir os dados inseridos
-- 

-- Total de registros por tabela:
-- SELECT 'Usuarios'               AS Tabela, COUNT(*) AS Total FROM Usuarios
-- UNION SELECT 'Registros_Humor',  COUNT(*) FROM Registros_Humor
-- UNION SELECT 'Tags',             COUNT(*) FROM Tags
-- UNION SELECT 'Registros_Tags',   COUNT(*) FROM Registros_Tags
-- UNION SELECT 'Contatos',         COUNT(*) FROM Contatos_Confianca
-- UNION SELECT 'Intervencoes',     COUNT(*) FROM Intervencoes
-- UNION SELECT 'Hist_Intervencoes',COUNT(*) FROM Historico_Intervencoes
-- UNION SELECT 'Desafios_Diarios', COUNT(*) FROM Desafios_Diarios
-- UNION SELECT 'Usuario_Desafios', COUNT(*) FROM Usuario_Desafios;

-- Linha do tempo emocional do João (ID 1):
-- SELECT rh.Data_Hora, rh.Nivel_Ansiedade, rh.Humor_Emoji, rh.Texto_Livre,
--        GROUP_CONCAT(t.Nome_Tag SEPARATOR ', ') AS Gatilhos
-- FROM Registros_Humor rh
-- LEFT JOIN Registros_Tags rt ON rh.ID_Registro = rt.ID_Registro
-- LEFT JOIN Tags t             ON rt.ID_Tag      = t.ID_Tag
-- WHERE rh.ID_Usuario = 1
-- GROUP BY rh.ID_Registro
-- ORDER BY rh.Data_Hora;
