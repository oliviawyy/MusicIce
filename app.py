from flask import Flask, render_template, request, redirect, session, flash
import mysql.connector
from model.musica import recuperar_musicas, salvar_musica
from model.genero import recuperar_generos
from model.musica import excluir_musica
from model.musica import alterar_musica
from model.cadastro import cadastro_usuario
from model.login import verificar_usuario

app = Flask(__name__)

app.secret_key = "oliviawyy"

@app.route("/home", methods=["GET"])
@app.route("/")
def principal():
    
    # recuperando os dados 
    musicas = recuperar_musicas(True)

    # recuperando o generpo
    generos = recuperar_generos()
    return render_template("principal.html", musicas = musicas, generos = generos )

@app.route("/admin")
def pagina_admin():
    if "usuario_logado" not in session:
        return redirect("/login")
    
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

@app.route("/musica/ativar/<codigo>/<status>")
def mudar_status_musica(codigo,status):
    alterar_musica(codigo, status)
    return redirect("/admin")

@app.route("/cadastro")
def pagina_cadastro ():
    return render_template("cadastrar.html") 

@app.route("/cadastro", methods=["POST"])
def rota_cadastrar():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    cadastro = cadastro_usuario(usuario, senha)

    if cadastro:
        session["usuario_logado"] = usuario
        return redirect("/admin")
    else:
        return redirect("/login")
    
@app.route("/usuario/login", methods=["POST"])
def usuario_login():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    login = verificar_usuario(usuario, senha)

    if login != None:
        session["usuario_logado"] = login
        flash(f"Seja bem-vindo, {login.nome}", "sucess")
        return redirect("/admin")
    else:
        flash("Usuário ou senha inválida!", "danger")
        return redirect("/login")

@app.route("/login")
def pagina_login():
    if "usuario_logado" in session:
        return redirect("admin")
    return render_template("login.html")

@app.route("/logoff")
def logoff():
    session.clear
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)