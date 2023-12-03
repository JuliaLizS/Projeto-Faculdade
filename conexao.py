import mysql.connector

def conexao_banco1():
    # Configurando banco de dados
    con = mysql.connector.connect(host = 'localhost', database = 'BANCO_PROJ1', user = 'root', password = '1234')

    if con.is_connected():
        db_info = con.get_server_info()
        print("Conectado ao serrvidor MySql versão ", db_info)
        cursor = con.cursor()
        cursor.execute("Select database();")
        linha = cursor.fetchone()
        print("Conectado ao banco de dados ", linha)