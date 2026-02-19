use MusicTube;
INSERT INTO `musictube`.`genero`
(`nome`,
`icone`,
`cor`)
VALUES
("Rock","","red"),
("Pop","","blue"),
("MPB","","#FACADA");


INSERT INTO `musictube`.`musica`
(`cantor`,
`duracao`,
`nome`,
`url_imagem`,
`nome_genero`)
VALUES
("KISS",
"00:03:58",
"I Was Made For Lovin' You",
"https://whiplash.net/imagens_promo_22/kiss_casablanca.jpg?nocache",
"Rock"),
("Ace of Base",
"00:03:31",
"Happy Nation",
"https://akamai.sscdn.co/uploadfile/letras/fotos/0/f/a/7/0fa73657275360ff70663e64f6b310cc.jpg",
"Pop"),
("Claudinho e Buchecha",
"00:04:09",
"Quero te encontrar",
"https://billboard.com.br/wp-content/uploads/2023/09/claudinho-e-buchecha-foto-jpg.webp",
"MPB");
