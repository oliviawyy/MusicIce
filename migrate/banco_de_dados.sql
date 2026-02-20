CREATE DATABASE IF NOT EXISTS MusicTube;
USE musictube;
CREATE TABLE IF NOT EXISTS genero (
    nome VARCHAR(30) NOT NULL PRIMARY KEY,
    icone VARCHAR(255),
    cor VARCHAR(30)
);
CREATE TABLE IF NOT EXISTS musica (
 codigo INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
 img_capa VARCHAR(255),
 nome VARCHAR(120),
 cantor VARCHAR(50),
 duracao TIME(6),
 nome_genero VARCHAR(30),
 CONSTRAINT fk_musica_genero FOREIGN KEY (nome_genero) REFERENCES genero(nome)
);