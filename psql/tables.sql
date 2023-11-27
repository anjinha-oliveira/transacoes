CREATE TABLE lojistas (
	id_lojista SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL, 
    cpf_cnpj VARCHAR(14) NOT NULL UNIQUE, 
    email text NOT NULL UNIQUE, 
    senha VARCHAR(10) NOT NULL,
    saldo DECIMAL
);

SELECT * FROM lojistas;

INSERT INTO lojistas (nome, cpf_cnpj, email, senha, saldo) 
	VALUES 
		('Sandra da Silva Santos', '00000000000', 'sandrasilva@gmail.com', '123', 10),
		('Rita Maria Graças', '99999999999', 'ritagracas@gmail.com', '9876', 101.90);

DROP TABLE lojistas;

CREATE TABLE usuarios (
	id_usuario SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL, 
    cpf_cnpj VARCHAR(14) NOT NULL UNIQUE, 
    email TEXT NOT NULL UNIQUE, 
    senha VARCHAR(10) NOT NULL,
    saldo DECIMAL
);

SELECT * FROM usuarios;

INSERT INTO usuarios (nome, cpf_cnpj, email, senha, saldo)
	VALUES 
		('Angela Nascimento Lucia', '99999099099', 'angelanascimento@gmail.com', '5436', 1.300),
		('Luan Fernandes Fonseca', '99999990000', 'luanfernandes@gmail.com', '546', 2.000);


CREATE TABLE transacoes (
	id_transacao SERIAL PRIMARY KEY,
    valor_transacao DECIMAL NOT NULL,
    id_pagador INT NOT NULL,
    id_recebedor INT NOT NULL,
	
	FOREIGN KEY (id_pagador) REFERENCES usuarios (id_usuario),
	FOREIGN KEY (id_recebedor) REFERENCES lojistas (id_lojista)
);

INSERT INTO transacoes (valor_transacao, id_pagador, id_recebedor)
	VALUES
	(20.50, 1, 2);

SELECT * FROM transacoes;
	

