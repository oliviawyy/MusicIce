from database.conexao import conectar


def recuperar_generos():
    conexao, cursor = conectar()

    # executando a conssulta
    cursor.execute("select nome, icone, cor from genero;")

    generos = cursor.fetchall()

    conexao.close()

    return generos