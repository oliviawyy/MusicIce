from flask import Flask, render_template, request, redirect
import mysql.connector
from model.musica import recuperar_musicas, salvar_musica
from model.genero import recuperar_generos
from model.musica import excluir_musica

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
    # recuperando os generos 
    generos = recuperar_generos()
    return render_template("administracao.html", 
                           musicas = musicas, 
                           generos = generos )


@app.route("/musica/post", methods = ["POST"])
def api_inserir_musica():
    cantor = request.form.get("input_cantor")
    nome_musica = request.form.get("input_musica")
    duracao = request.form.get("input_duracao")
    imagem = request.form.get("input_imagem")
    nome_genero = request.form.get("select_genero")
    if salvar_musica(cantor,nome_musica,duracao,imagem,nome_genero):
        return redirect("/admin")
    else:
        return "ERRO AO ADICIONAR MÚSICA"

@app.route("/musica/delete/<codigo>")
def deletar_musica(codigo):
    if excluir_musica(codigo):
        return redirect("/admin")

    else:
        return ""




if __name__=="__main__":
    app.run(debug=True)