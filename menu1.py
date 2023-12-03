import tkinter as tk
from tkinter import Listbox
from cadastro1 import abrir_janela_cadastro
from alteracao_cadastro1 import abrir_janela_alterar_cadastro
import mysql.connector
import alteracao_cadastro1 as alteracao

cliente_id = None

con = mysql.connector.connect(host = 'localhost', database = 'BANCO_PROJ1', user = 'root', password = '1234')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao serrvidor MySql versão ", db_info)
    cursor = con.cursor()
    cursor.execute("Select database();")
    linha = cursor.fetchone()
    print("Conectado ao banco de dados ", linha)

# Função para listar clientes
def listar_clientes():
    lista_clientes.delete(0, tk.END)
    value = nome_pesquisa.get()
    like_nome_pesquisa = f'%{value}%'
    try:
        cursor.execute("SELECT IDCLIENTE, NOME, EMAIL FROM CLIENTE WHERE NOME LIKE %s", (like_nome_pesquisa,))
        for cliente in cursor.fetchall():
            lista_clientes.insert(tk.END, f"{cliente[0]} - {cliente[1]} - {cliente[2]}")
    except mysql.connector.Error as err:
        print(f"Erro ao listar clientes: {err}")
    con.commit()


# Função para selecionar clientes para abrir os dados em outra aba
def selecionar_cliente():
    global cliente_id
    selected_item = lista_clientes.get(lista_clientes.curselection())
    if selected_item:
        cliente_id = int(selected_item.split(" - ")[0])
        cursor.execute("SELECT IDCLIENTE FROM CLIENTE WHERE NOME LIKE %s", (cliente_id,))

def excluir_cliente():
    # Obter o índice do cliente selecionado
    selected_index = lista_clientes.curselection()

    # Certificar-se de que algo está realmente selecionado
    if selected_index:
        selected_item = lista_clientes.get(selected_index)

        selected_id = int(selected_item.split(" - ")[0])

        while cursor.nextset():
            pass
        cursor.execute("DELETE FROM CLIENTE WHERE IDCLIENTE=%s", (selected_id,))
    con.commit()
    listar_clientes()


def abrir_janela_alterar_cadastro_selecionado():
    global cliente_id
    print('passou na função abrir...selecionado')
    if cliente_id is not None:
        abrir_janela_alterar_cadastro(cliente_id)
        print('passou no IF da função abrir...selecionado')



menu = tk.Tk()
menu.title("Menu Clientes")
menu.geometry("700x435+660+250")
menu.resizable(False, False)
menu.configure(bg="#FFE8E5")

# Nome
nome_pesquisa = tk.Entry(menu, font=14, width=42)
nome_pesquisa.pack()
nome_pesquisa.place(x=100, y=60)

# Rotulo Nome
nome_pesquisa_rotulo = tk.Label(menu, text="Nome:", font=("Helvetica", 11), bg="#FFE8E5")
nome_pesquisa_rotulo.pack()
nome_pesquisa_rotulo.place(x=50, y=60)


#! Botão de Pesquisar Cliente
button_pesquisar_cliente = tk.Button(menu, text="Pesq. Cliente", font=("Cooper Black", 12), bg="#EB0DAD", fg="White", command=listar_clientes)
button_pesquisar_cliente.pack()
button_pesquisar_cliente.place(x=300, y=130)
button_pesquisar_cliente.config(width=10, height=1)

# Cadastrar
button_cadastrar = tk.Button(menu, text="Cadastrar", bg="#EB0DAD", fg="White", font=("Cooper Black", 11), command=abrir_janela_cadastro)
button_cadastrar.pack()
button_cadastrar.place(x=546, y=6)
button_cadastrar.config(width=10, height=1)

# Cadastrar rotulo
data_rotulo = tk.Label(menu, text="Clique para cadastrar um cliente.", font=("Helvetica", 9), bg="#FFE8E5")
data_rotulo.pack()
data_rotulo.place(x=355, y=10)

# Frame para lista de clientes e barra de rolagem
frame_lista = tk.Frame(menu)
frame_lista.pack()
frame_lista.place(x=45, y=180, width=600, height=200)

# Listbox - Caixa pra listar cliente
lista_clientes = Listbox(frame_lista)
lista_clientes.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Barra de rolagem vertical
scrollbar = tk.Scrollbar(frame_lista, orient=tk.VERTICAL, command=lista_clientes.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
lista_clientes.config(yscrollcommand=scrollbar.set)

lista_clientes.bind('<<ListboxSelect>>', lambda event: selecionar_cliente())


def fechar_menu():
    menu.destroy()

#! Botão "FECHAR"
button_cancelar = tk.Button(menu, text="Fechar", bg="#EB0DAD", fg="White", font=("Cooper Black", 11), command=fechar_menu)
button_cancelar.pack()
button_cancelar.place(x=50, y=390)
button_cancelar.config(width=8, height=1)

#! Botão "EXCLUIR CLIENTE"
button_excluir = tk.Button(menu, text="Excluir", bg="Dark Red", fg="White", font=("Cooper Black", 11), command=excluir_cliente)
button_excluir.pack()
button_excluir.place(x=436, y=390)
button_excluir.config(width=8, height=1)

#! BOTÃO ALTERAR DADOS DO CLIENTE
button_alterar = tk.Button(menu, text="Alterar", bg="Green", fg="White", font=("Cooper Black", 11), command = abrir_janela_alterar_cadastro_selecionado)
button_alterar.pack()
button_alterar.place(x=546, y=390)
button_alterar.config(width=8, height=1)
''''''

listar_clientes()


menu.mainloop()


