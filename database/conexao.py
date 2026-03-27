import mysql.connector


def conectar():

    tipo_conexao = "NUVEM"
    if tipo_conexao == "LOCAL":
        conexao = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="root",
        database="MusicTube"
        
    )
    else:
        conexao = mysql.connector.connect(
        host="servidor-olivia-servidor-olivia.a.aivencloud.com",
        port="22681",
        user="avnadmin",
        password="AVNS_J6yhXvAVBZ0f6eyeelN",
        database="MusicTube"
        
    )

    #Criando o cursor

    cursor = conexao.cursor(dictionary=True)

    return conexao, cursor
