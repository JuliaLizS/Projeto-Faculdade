import datetime
import tkinter as tk
from calendar import calendar
from time import strptime, strftime
from tkinter import FLAT, END


from tkcalendar import Calendar

import mysql.connector


# Configurando banco de dados
con = mysql.connector.connect(host = 'localhost', database = 'BANCO_PROJ1', user = 'root', password = '1234')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao serrvidor MySql versão ", db_info)
    cursor = con.cursor()
    cursor.execute("Select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ", linha)


def abrir_janela_cadastro():
    janela = tk.Tk()
    janela.title("Glamour Fashion")
    janela.geometry("650x430+670+260")
    janela.resizable(False, False)
    janela.configure(bg="#FFE8E5")

    # Titulo
    titulo = tk.Label(janela, text="Glamour Fashion", anchor="center", bg="#FFE8E5")
    titulo.config(font=("Cooper Black", 25), fg="#EB0DAD")
    titulo.pack()
    subtitulo = tk.Label(janela, text="CADASTRO DE CLIENTES", anchor="center", bg="#FFE8E5")
    subtitulo.config(font=("Arial", 10))
    subtitulo.pack()

    # Nome
    nome_completo = tk.Entry(janela, font=14, width=58)
    nome_completo.pack()
    nome_completo.place(x=50, y=78)

    # Rotulo Nome
    nome_rotulo = tk.Label(janela, font=("Helvetica", 10), text="Nome:", bg="#FFE8E5")
    nome_rotulo.pack()
    nome_rotulo.place(x=48, y=56)

    def pick_date(event):
        global cal, date_window
        date_window = tk.Toplevel()
        date_window.grab_set()
        date_window.geometry("250x220+590+370")
        cal = Calendar(date_window, selectmode="day", date_pattern="mm/dd/y")
        cal.place(x=0, y=0)

        submit_btn = tk.Button(date_window, text="Salvar", command=grab_date)
        submit_btn.place(x=80, y=190)

    def grab_date():
        nasc_entry.delete(0, END)
        nasc_entry.insert(0, cal.get_date())
        date_window.destroy()

    nasc_entry = tk.Entry(janela, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                          font=("Helvetica", 11, "bold"))
    nasc_entry.place(x=49, y=135, width=100)
    nasc_entry.insert(0, "dd/mm/yyyy")
    nasc_entry.bind("<1>", pick_date)

    # Rotulo nascimento
    nascimento_rotulo = tk.Label(janela, font=("Helvetica", 10), text="Nascimento:", bg="#FFE8E5")
    nascimento_rotulo.pack()
    nascimento_rotulo.place(x=48, y=110)

    # Botao Feminino

    def on_enter(event):
        event.widget.config(state=tk.NORMAL)

    def on_leave(event):
        event.widget.config(state=tk.DISABLED)

    sexo = tk.IntVar()
    sexo.set(1)

    tk.Label(janela, text="Escolha o sexo:", bg="#FFE8E5").place(x=180, y=110)
    tk.Radiobutton(janela, text="F", value=2, variable=sexo, bg="#FFE8E5").place(x=175, y=136)
    tk.Radiobutton(janela, text="M", value=1, bg="#FFE8E5", variable=sexo).place(x=228, y=136)

    # Email
    email = tk.Entry(janela, font=14, width=30)
    email.pack()
    email.place(x=301, y=135)

    # Email Rotulo
    email_rotulo = tk.Label(janela, font=("Helvetica", 10), text="E-mail:", bg="#FFE8E5", )
    email_rotulo.pack()
    email_rotulo.place(x=298, y=110)

    # Rua
    rua = tk.Entry(janela, font=14, width=42)
    rua.pack()
    rua.place(x=50, y=190)

    # Rua rotulo
    rua_rotulo = tk.Label(janela, font=("Helvetica", 10), text="Rua:", bg="#FFE8E5", )
    rua_rotulo.pack()
    rua_rotulo.place(x=48, y=165)

    # Numero
    numero = tk.Entry(janela, font=14, width=6)
    numero.pack()
    numero.place(x=516, y=190)

    # Numero rotulo
    numero_rotulo = tk.Label(janela, font=("Helvetica", 10), text="N°:", bg="#FFE8E5", )
    numero_rotulo.pack()
    numero_rotulo.place(x=514, y=165)

    # Cidade
    cidade = tk.Entry(janela, font=14, width=20)
    cidade.pack()
    cidade.place(x=50, y=250)

    # Cidade rotulo

    rua_rotulo = tk.Label(janela, font=("Helvetica", 10), text="Cidade:", bg="#FFE8E5", )
    rua_rotulo.pack()
    rua_rotulo.place(x=48, y=225)

    # UF
    uf = tk.Entry(janela, font=14, width=5)
    uf.pack()
    uf.place(x=295, y=250)

    # Uf rotulo
    rua_rotulo = tk.Label(janela, font=("Helvetica", 10), text="UF:", bg="#FFE8E5", )
    rua_rotulo.pack()
    rua_rotulo.place(x=293, y=225)

    # bairro
    bairro = tk.Entry(janela, font=14, width=21)
    bairro.pack()
    bairro.place(x=381, y=250)

    # bairro Rotulo
    bairro_rotulo = tk.Label(janela, font=("Helvetica", 10), text="Bairro:", bg="#FFE8E5", )
    bairro_rotulo.pack()
    bairro_rotulo.place(x=379, y=225)

    #! ID CLIENTE 
    id_cliente_gerado = cursor.lastrowid
    '''id_cliente_rotulo = tk.Label(janela, font=("Helvetica", 10), text=f"ID: {id_cliente_gerado}", bg="#FFE8E5", )
    id_cliente_rotulo.pack()
    id_cliente_rotulo.place(x=48, y=285)'''

    # ID ENDEREÇO 

    id_endereco_gerado = cursor.lastrowid

    # Celular DDD
    celular_ddd = tk.Entry(janela, font=14, width=5)
    celular_ddd.pack()
    celular_ddd.place(x=295, y=310)

    # Celular DDD rotulo

    celular_Ddd_rotulo = tk.Label(janela, font=("Helvetica", 10), text="DDD:", bg="#FFE8E5", )
    celular_Ddd_rotulo.pack()
    celular_Ddd_rotulo.place(x=293, y=285)

    #  Celular
    celular = tk.Entry(janela, font=14, width=21)
    celular.pack()
    celular.place(x=381, y=310)

    # Celular rotulo
    celular_rotulo = tk.Label(janela, font=("Helvetica", 10), text="Celular:", bg="#FFE8E5", )
    celular_rotulo.pack()
    celular_rotulo.place(x=379, y=285)

    def salvar_cadastro():
        nome_valor = nome_completo.get()
        sexo_valor = sexo.get()
        nascimento = nasc_entry.get()
        email_valor = email.get()
        endereco_rua = rua.get()
        numero_casa = numero.get()
        cidade_valor = cidade.get()
        uf_valor = uf.get()  # Usando varEstado para obter a UF
        bairro_valor = bairro.get()
        ddd_celular = celular_ddd.get()
        numero_celular = celular.get()

        sql = "INSERT INTO CLIENTE (NOME, SEXO, NASCIMENTO, EMAIL) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nome_valor, sexo_valor, nascimento, email_valor))
        con.commit()

        id_cliente_gerado = cursor.lastrowid  # Obtendo o ID do cliente inserido

        sql = "INSERT INTO ENDERECO (RUA, NUM, BAIRRO, CIDADE, ESTADO, ID_CLIENTE) VALUES (%s, %s, %s, %s, %s, %s)"
        endereco_values = (endereco_rua, numero_casa, bairro_valor, cidade_valor, uf_valor, id_cliente_gerado)
        cursor.execute(sql, endereco_values)
        con.commit()

        sql = "INSERT INTO TELEFONE (DDD, NUMERO, ID_CLIENTE) VALUES (%s, %s, %s)"
        telefone_values = (ddd_celular, numero_celular, id_cliente_gerado)
        cursor.execute(sql, telefone_values)
        con.commit()

        janela.destroy()

    def cancelar_cadastro():
        janela.destroy()

        # Botão "Salvar"

    button_cancelar = tk.Button(janela, text="Cancelar", bg="#EB0DAD", fg="White", font=("Cooper Black", 11), command=cancelar_cadastro)
    button_cancelar.pack()
    button_cancelar.place(x=430, y=370)
    button_cancelar.config(width=9, height=2)

    button_salvar = tk.Button(janela, text="Salvar", bg="#EB0DAD", fg="White", font=("Cooper Black", 11), command=salvar_cadastro)
    button_salvar.pack()
    button_salvar.place(x=540, y=370)
    button_salvar.config(width=9, height=2)