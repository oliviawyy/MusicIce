from database.conexao import conectar 

def recuperar_musicas():
    #passo 1 e 2 já feito
    conexao, cursor = conectar()

    cursor.execute("SELECT codigo, cantor, duracao, nome, img_capa, nome_genero, ativo FROM musica;")

    musicas = cursor.fetchall()

    conexao.close()

    return musicas


def salvar_musica(cantor:str, nome_musica:str, duracao:str, imagem:str, genero:str) -> bool:
    """
    eu adiciono a sua musica no banco de dados
    """

    try:
        # conectando ao banco
        conexao, cursor = conectar()

        # executar insert
        cursor.execute("""
                            INSERT INTO musica
                                (cantor, nome, duracao, img_capa, nome_genero)
                            VALUES
                                (%s, %s, %s, %s, %s);
                        """,
                        [cantor, nome_musica, duracao, imagem, genero]
                        )
        
        conexao.commit()
        
        conexao.close()

        return True
    
    except Exception as erro:
        print(erro)
        return False
    

def excluir_musica(codigo:int) -> bool:
    """Essa função serve para excluir a musica"""
    try:
        conexao, cursor = conectar()

        cursor.execute("""
        DELETE FROM musica
        WHERE codigo = %s
                       
        """, 
        [codigo])
        conexao.commit()

        conexao.close()

        return True

    except Exception as erro:
        print(erro)
        return False

def alterar_musica(codigo:int, status:bool):
    """ essa funcao serve para alterar"""
    try:
        conexao, cursor = conectar()

        cursor.execute("""
        UPDATE musica
        SET ativo = %s
        WHERE CODIGO = %s""")