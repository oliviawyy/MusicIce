from flask import Flask, render_template
import mysql.connector
from model.musica import recuperar_musicas
from model.genero import recuperar_generos

app = Flask(__name__)

@app.route("/home", methods=["GET"])
@app.route("/")
def principal():
    
    # recuperando os dados 
    musicas = recuperar_musicas()

    # recuperando o generpo
    generos = recuperar_generos()
    return render_template("principal.html", musicas = musicas, generos = generos )

@app.route("/admin")
def pagina_admin():
    musicas = recuperar_musicas()
    return render_template("administracao.html", musicas = musicas)

if __name__=="__main__":
    app.run(debug=True)