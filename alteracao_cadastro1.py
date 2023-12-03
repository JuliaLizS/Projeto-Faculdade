import tkinter as tk
from tkinter import messagebox
import mysql.connector
from tkcalendar import Calendar
from tkinter import FLAT, END

# Configurando CONEXÃO com banco de dados
con = mysql.connector.connect(host = 'localhost', database = 'BANCO_PROJ1', user = 'root', password = '1234')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao serrvidor MySql versão ", db_info)
    cursor = con.cursor()
    cursor.execute("Select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ", linha)


def obter_dados_do_cliente(cliente_id):
    try:
        cursor = con.cursor()
        cursor.execute("SELECT C.IDCLIENTE, C.NOME, C.SEXO, C.NASCIMENTO, C.EMAIL, E.RUA, E.NUM, E.BAIRRO, E.CIDADE, E.ESTADO, T.DDD, T.NUMERO FROM CLIENTE AS C INNER JOIN ENDERECO AS E ON C.IDCLIENTE = E.ID_CLIENTE INNER JOIN TELEFONE AS T ON C.IDCLIENTE = T.ID_CLIENTE WHERE C.IDCLIENTE = %s", (cliente_id,))
        dados = cursor.fetchone()
        cursor.close()
        return dados
    except mysql.connector.Error as err:
        print(f"Erro ao obter dados do cliente: {err}")
        return None
        
def abrir_janela_alterar_cadastro_selecionado(cliente_id):
    abrir_janela_alterar_cadastro(cliente_id)

def abrir_janela_alterar_cadastro(cliente_id):
    if cliente_id is not None:
        dados_do_cliente = obter_dados_do_cliente(cliente_id)
        if dados_do_cliente:
            janela = tk.Toplevel()
            janela.title("Alterar dados do cliente")
            janela.geometry("650x430+670+260")
            janela.resizable(False, False)
            janela.configure(bg="#FFE8E5")

            # Titulo
            titulo = tk.Label(janela, text="Glamour Fashion", anchor="center", bg="#FFE8E5",font=("Cooper Black", 25), fg="#EB0DAD")
            titulo.pack()

            # Subtitulo
            subtitulo = tk.Label(janela, text="ALTERAR DADOS DO CLIENTE", anchor="center", bg="#FFE8E5", font=("Arial", 10))
            subtitulo.pack()
            
            # Rotulo Nome
            nome_rotulo = tk.Label(janela, font=("Helvetica", 10), text="Nome:", bg="#FFE8E5")
            nome_rotulo.pack()
            nome_rotulo.place(x=50, y=78)

            # Nome
            nome_completo = tk.Entry(janela, font=("Helvetica", 10), width=58)
            nome_completo.insert(1,dados_do_cliente[1])
            nome_completo.pack()
            nome_completo.place(x=100, y=78)

            def pick_date(event):
                global cal, date_window
                date_window = tk.Toplevel()
                date_window.grab_set()
                date_window.geometry("250x220+590+370")
                cal = Calendar(date_window, selectmode="day", date_pattern="dd/MM/yyyy")
                cal.place(x=0, y=0)

                submit_btn = tk.Button(date_window, text="Salvar", command=grab_date)
                submit_btn.place(x=80, y=190)


            def grab_date():
                nasc_entry.delete(0, END)
                nasc_entry.insert(0, cal.get_date())
                date_window.destroy()

            # Rotulo nascimento
            nascimento_rotulo = tk.Label(janela, font=("Helvetica", 10), text="Nascimento:", bg="#FFE8E5")
            nascimento_rotulo.place(x=48, y=110)

            nasc_entry = tk.Entry(janela, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69", font=("Helvetica", 11, "bold"))
            nasc_entry.insert(3,dados_do_cliente[3])
            nasc_entry.place(x=49, y=135, width=100)
            nasc_entry.bind("<1>", pick_date)


            # Botao Feminino
            sexo = tk.IntVar()
            sexo.set(1)

            tk.Label(janela, text="Escolha o sexo:", bg="#FFE8E5").place(x=180, y=110)
            tk.Radiobutton(janela, text="F", value=2, variable=sexo, bg="#FFE8E5").place(x=175, y=136)
            tk.Radiobutton(janela, text="M", value=1, bg="#FFE8E5", variable=sexo).place(x=228, y=136)

            # Email
            email = tk.Entry(janela, font=14, width=30)
            email.insert(4,dados_do_cliente[4])
            email.pack()
            email.place(x=301, y=135)

            # Email Rotulo
            email_rotulo = tk.Label(janela, font=("Helvetica", 10), text="E-mail:", bg="#FFE8E5",)
            email_rotulo.pack()
            email_rotulo.place(x=298, y=110)

            # Rua
            rua = tk.Entry(janela, font=14, width=42)
            rua.insert(5,dados_do_cliente[5])
            rua.pack()
            rua.place(x=50, y=190)

            # Rua rotulo
            rua_rotulo = tk.Label(janela, font=("Helvetica", 10), text="Rua:", bg="#FFE8E5",)
            rua_rotulo.pack()
            rua_rotulo.place(x=48, y=165)

            # Numero casa
            numero = tk.Entry(janela, font=14, width=6)
            numero.insert(6,dados_do_cliente[6])
            numero.pack()
            numero.place(x=516, y=190)

            # Numero rotulo
            numero_rotulo = tk.Label(janela, font=("Helvetica", 10), text="N°:", bg="#FFE8E5",)
            numero_rotulo.pack()
            numero_rotulo.place(x=514, y=165)

            # Cidade
            cidade = tk.Entry(janela, font=14, width=20)
            cidade.insert(8,dados_do_cliente[8])
            cidade.pack()
            cidade.place(x=50, y=250)

            # Cidade rotulo

            cidade_rotulo = tk.Label(janela, font=("Helvetica", 10), text="Cidade:", bg="#FFE8E5",)
            cidade_rotulo.pack()
            cidade_rotulo.place(x=48, y=225)

            # UF
            uf = tk.Entry(janela, font=14, width=5)
            uf.insert(9,dados_do_cliente[9])
            uf.pack()
            uf.place(x=295, y=250)

            # Uf rotulo
            rua_rotulo = tk.Label(janela, font=("Helvetica", 10), text="UF:", bg="#FFE8E5",)
            rua_rotulo.pack()
            rua_rotulo.place(x=293, y=225)

            # Bairro
            bairro = tk.Entry(janela, font=14, width=21)
            bairro.insert(7,dados_do_cliente[7])
            bairro.pack()
            bairro.place(x=381, y=250)

            # Bairro Rotulo
            bairro_rotulo = tk.Label(janela, font=("Helvetica", 10), text="Bairro:", bg="#FFE8E5",)
            bairro_rotulo.pack()
            bairro_rotulo.place(x=379, y=225)

            # ID
            id_cliente = tk.Entry(janela, font=14, width=5)
            id_cliente.insert(0,dados_do_cliente[0])
            id_cliente.pack()
            id_cliente.place(x=50, y=310)

            id_cliente.config(state='readonly')

            # ID rotulo

            id_rotulo = tk.Label(janela, font=("Helvetica", 10),  text="ID:", bg="#FFE8E5")
            id_rotulo.pack()
            id_rotulo.place(x=48, y=285)

            # Celular DDD
            celular_ddd = tk.Entry(janela, font=14, width=5)
            celular_ddd.insert(10,dados_do_cliente[10])
            celular_ddd.pack()
            celular_ddd.place(x=295, y=310)

            # Celular DDD rotulo

            celular_Ddd_rotulo = tk.Label(janela, font=("Helvetica", 10), text="DDD:", bg="#FFE8E5",)
            celular_Ddd_rotulo.pack()
            celular_Ddd_rotulo.place(x=293, y=285)

            #  Celular
            celular = tk.Entry(janela, font=14, width=21)
            celular.insert(11,dados_do_cliente[11])
            celular.pack()
            celular.place(x=381, y=310)

            # Celular rotulo
            celular_rotulo = tk.Label(janela, font=("Helvetica", 10), text="Celular:", bg="#FFE8E5",)
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
                uf_valor = uf.get()
                bairro_valor = bairro.get()
                ddd_celular = celular_ddd.get()
                numero_celular = celular.get()

                #! PARA ALTERAR DADOS NO BANCO

                # DADOS TABELA CLIENTE
                cursor.execute("UPDATE CLIENTE SET NOME=%s, SEXO=%s, NASCIMENTO=%s, EMAIL=%s WHERE IDCLIENTE=%s", (nome_valor, sexo_valor, nascimento, email_valor, cliente_id))
                con.commit()

                # DADOS TABELA ENDERECO
                cursor.execute("UPDATE ENDERECO SET RUA=%s, NUM=%s, BAIRRO=%s, CIDADE=%s, ESTADO=%s WHERE ID_CLIENTE=%s", (endereco_rua, numero_casa, bairro_valor, cidade_valor, uf_valor, cliente_id))
                con.commit()

                # DADOS TABELA TELEFONE
                cursor.execute("UPDATE TELEFONE SET DDD=%s, NUMERO=%s WHERE ID_CLIENTE=%s", (ddd_celular, numero_celular, cliente_id))
                con.commit()

                #! ATÉ AQUI
                
                
                janela.destroy()

            def cancelar_cadastro():
                janela.destroy()

            # Botão "Cancelar"
            button_cancelar = tk.Button(janela, text="Cancelar", bg="#EB0DAD", fg="White", font=("Cooper Black", 11), command=cancelar_cadastro)
            button_cancelar.pack()
            button_cancelar.place(x=430, y=370)
            button_cancelar.config(width=9, height=2)
            

            # Botão "Salvar"
            button_salvar = tk.Button(janela, text="Salvar", bg="#EB0DAD", fg="White", font=("Cooper Black", 11), command=salvar_cadastro)
            button_salvar.pack()
            button_salvar.place(x=540, y=370)
            button_salvar.config(width=9, height=2)

            janela.mainloop()

