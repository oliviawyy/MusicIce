from database.conexao import conectar

def cadastro_usuario(usuario:str, senha:str)-> list:
    """
    cadastrando o usuario
    """

    try:
        # conectando ao banco
        conexao, cursor = conectar()

        # executar insert
        cursor.execute("""
                            INSERT INTO usuarios
                                (usuario, senha)
                            VALUES
                                (%s, %s;
                        """,
                        [usuario, senha]
                        )
        conexao.commit()
        
        conexao.close()

        return True
    
    except Exception as erro:
        print(erro)
        return False
    
