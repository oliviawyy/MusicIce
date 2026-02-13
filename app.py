from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)


@app.route("/home", methods=["GET"])
@app.route("/")
def principal():
    # conectando o banco de dados 
    conexao = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="MusicTube"
    )

    # criando o cursor 
    cursor = conexao.cursor(dictionary=True)

    # executando a conssulta
    cursor.execute("select codigo, cantor, duracao, nome, url_imagem, nome_genero from musica;")

    # recuperando os dados 
    musicas = cursor.fetchall()

    # executando a consulta do genero
    cursor.execute("SELECT nome, icone, cor from genero;")

    # recuperando o generpo
    generos = cursor.fetchall()

    # fechando a conexao
    conexao.close()

    return render_template("principal.html", musicas = musicas, generos = generos )


if __name__=="__main__":
    app.run(debug=True)