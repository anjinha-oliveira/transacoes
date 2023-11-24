CREATE TABLE lojistas (
	id_lojista SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL, 
    cpf_cnpj VARCHAR(14) NOT NULL UNIQUE, 
    email VARCHAR(20) NOT NULL UNIQUE, 
    senha VARCHAR(10) NOT NULL,
    saldo INT
);
SELECT * FROM lojistas;

CREATE TABLE usuarios (
	id_usuarios SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL, 
    cpf_cnpj VARCHAR(14) NOT NULL UNIQUE, 
    email VARCHAR(20) NOT NULL UNIQUE, 
    senha VARCHAR(10) NOT NULL,
    saldo INT
);
SELECT * FROM usuarios

CREATE TABLE transacoes (
    valor_transacao INT NOT NULL,
    id_pagador INT NOT NULL,
    id_recebedor INT NOT NULL
);

SELECT * FROM tansacoes