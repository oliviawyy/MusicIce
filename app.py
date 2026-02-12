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

    cursor = conexao.cursor(dictionary=True)
    return render_template("principal.html")


if __name__=="__main__":
    app.run(debug=True)