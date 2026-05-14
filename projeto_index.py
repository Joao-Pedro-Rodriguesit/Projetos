
from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox
from tkinter import ttk
from datetime import date
import sqlite3

janela = Tk() #cria a janela do tkinter

class Funcao(): #classe cujo o objetivo é criar as tabelas e o banco de dados

    def conectar_bd(self): #função que vai conectar o banco de dados, caso ele não exista, ele será criado
        self.conexao = sqlite3.connect("cadastro_aluno.db") #estabelece a conexão com o SQL criando um BD se ele não existir
        self.cursor = self.conexao.cursor() #cria um cursor para executar os comandos SQL

    def desconectar_bd(self): #função que vai desconectar o BD, fechando sua conexão
        self.conexao.close()

    def montar_tabela(self): #função que vai montar a tabela, conectando o BD, se a tabela que representa a entidade não existir, ela será criada
        self.conectar_bd()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            turma TEXT,
            data_nascimento TEXT
        )
        """) #criar uma tabela se não existir alunos, id é autoincrementável, sendo a PK, nome, turma e data são atributos qualquer do tipo texto

        self.conexao.commit() #confirma as alterações feitas no BD
        self.desconectar_bd() #desconecta a conexão com o BD

funcao = Funcao() #estabelece a var de função para que a classe Funcao seja chamada e suas funções executadas
funcao.montar_tabela() #chama a função montar tabela para criar o BD e a tabela caso eles não existam
janela.title("Cadastro de Alunos") #define o título da janela do tkinter
janela.geometry("1200x600") #cria o tamanho da janela do tkinter
janela.configure(bg="#6e6e6e") #background da janela
janela.resizable(width=False, height=False) #suspende a possibilidade de redimensionar a janela, ou seja, alterar a altura e largura da janela tkinter


left_frame = Frame(janela, width=550, height=1000, bg="#d4d4d4", relief="sunken")
left_frame.pack(side=RIGHT) #define o lado onde o frame vai ser posicionado, estabelecendo um contraste para que os botões/campos sejam inseridos

left_frame2 = Frame(janela, width=450, height=1000, bg="#d4d4d4", relief="sunken")
left_frame2.pack(side=LEFT)


# -------- CAMPOS --------

Label(left_frame, text="Nome Completo", font=("Arial", 12), bg="#d4d4d4").place(x=10, y=20) #criar a label para o campo nome

Nome_user_entry = Entry(left_frame, width=30, font=("Arial", 16)) #cria o campo da label nome
Nome_user_entry.place(x=10, y=50) #define a largura e altura do campo nome

Label(left_frame, text="Cursos", font=("Arial", 12), bg="#d4d4d4").place(x=10, y=80) #cria a label para o campo curso

turma_radiobuttom = StringVar() #define a turma/texto curso como um botão do tipo Radios
turma_radiobuttom.set("Informática") #define o valor padrão do botão de turma/curso como Informática

Radiobutton(left_frame, text="Informática", variable=turma_radiobuttom, value="Informática", bg="#d4d4d4").place(x=10, y=100) 
Radiobutton(left_frame, text="Administração", variable=turma_radiobuttom, value="Administração", bg="#d4d4d4").place(x=10, y=130)
Radiobutton(left_frame, text="Enfermagem", variable=turma_radiobuttom, value="Enfermagem", bg="#d4d4d4").place(x=10, y=160)
Radiobutton(left_frame, text="Estetica", variable=turma_radiobuttom, value="Estetica", bg="#d4d4d4").place(x=10, y=190)
Radiobutton(left_frame, text="Finanças", variable=turma_radiobuttom, value="Finanças", bg="#d4d4d4").place(x=10, y=220)
#define todos os botões de turma/curso do tipo Radios

Label(left_frame, text="Data de Nascimento", font=("Arial", 12), bg="#d4d4d4").place(x=10, y=250) #cria a label para o campo data 

Data_user_nasc = DateEntry(left_frame) #cria o campo da label data, utilizando a biblioteca tkcalendar (a biblioteca tkcalendar não vem instalada no python, é necessário ir no CMD e digitar "pip install tkcalendar" para que a instalação seja feita e que a biblioteca possa ser usada)
Data_user_nasc.place(x=15, y=280) #define a largura e altura do campo data


# -------- TABELA --------

abas = ttk.Treeview(
    left_frame2,
    columns=("ID", "Nome", "Turma", "Data"),
    show="headings"
) #cria a tabela treeview, ou seja, a tabela que será utilizada para ver os nomes, ids, datas e turmas dos alunos cadastrados 

abas.heading("ID", text="ID") #define a aba de texto ID, ou seja, a coluna onde os IDs dos alunos cadastrados serão mostrados
abas.heading("Nome", text="Nome") #define a aba de texto Nome, ou seja, a coluna onde os nomes dos alunos cadastrados serão mostrados
abas.heading("Turma", text="Curso") #define a aba de texto Turma, ou seja, a coluna onde os cursos dos alunos cadastrados serão mostrados
abas.heading("Data", text="Data de Nascimento") #define a aba de texto Data, ou seja, a coluna onde as datas de nascimento dos alunos cadastrados serão mostrados

abas.column("ID", width=60) #define a largura da coluna ID, ou seja, a coluna onde os IDs dos alunos cadastrados serão mostrados
abas.column("Nome", width=150) #define a largura da coluna Nome, ou seja, a coluna onde os nomes dos alunos cadastrados serão mostrados
abas.column("Turma", width=100) #define a largura da coluna Turma, ou seja, a coluna onde as turmas dos alunos cadastrados serão mostrados
abas.column("Data", width=100) #define a largura da coluna Data, ou seja, a coluna onde as datas de nascimento dos alunos cadastrados serão mostrados

abas.place(x=10, y=10) #define a posição da tabela, onde ela será mostrada na janela tkinter



# -------- FUNÇÕES --------

def limpar(): #função que é utilizada para limpar os campos de texto após o cadastro
    Nome_user_entry.delete(0, END) #limpa o campo de texto do nome, ou seja, apaga o que foi digitado no campo de nome
    turma_radiobuttom.set("Informática") #define o valor do botão de turma/curso como Informática, ou seja, o valor padrão do botão de turma/curso
    Data_user_nasc.set_date(date.today()) #define a data do campo data como a data atual, ou seja, a data do dia em que o cadastro está sendo feito


def mostrar_alunos(): #função que é utilizada para mostrar os alunos cadastrados na tabela treeview

    for item in abas.get_children(): #pecorre os items da tabela e os deleta, ou seja, limpa a tabela para que os dados sejam atualizados e não tenha repetição de dados
        abas.delete(item) #deleta os items da tabela, ou seja, limpa a tabela para que os dados sejam atualizados e não tenha repetição de dados

    funcao.conectar_bd() #função que conecta o BD

    lista = funcao.cursor.execute(
        "SELECT * FROM alunos"
    ).fetchall() #executa o comando SQL para selecionar todos os dados da tabela alunos, ou seja, seleciona os dados dos alunos cadastros e os armazena na var lista
#fetchall() é utilizado para buscar todos os resultados da consulta SQL e armazená-los em uma lista, ou seja, armazena os dados dos alunos cadastrados em uma lista para que eles possam ser mostrados na tabela treeview
    for linha in lista:
        abas.insert("", END, values=linha) #insere os dados da var linha, ou seja, os dados dos alunos que são cadastrados na tabela treeview e são exibidos na janela tkinter
#ou seja, isso é para que os dados sejam armazenados no SQL e depois executado no treeview
    funcao.desconectar_bd() #desconecta o Banco de Dados


def cadastro(): #função responsável por cadastrar os alunos e armazenar os dados no BD, sendo exibitos no treeview

    nome = Nome_user_entry.get() #variável que armazena o nome digitado no campo de texto do nome, ou seja, o nome do aluno que está sendo cadastrado
    turma = turma_radiobuttom.get() #variável que armazena o valor selecionado no botão de turma/curso, ou seja, o curso do aluno que está sendo cadastrado
    data = Data_user_nasc.get() #variável que armazena a data selecionada no campo de data, ou seja, a data de nascimento do aluno que está sendo cadastrado

    if nome == "":
        messagebox.showwarning("Aviso", "Digite um nome")
        return #se nome for igual a 0, ou seja, se o campo de nome estiver vazio, irá exibir um caixa de messagem dizendo que é necessário digitar um nome para que o cadastro seja executado

    funcao.conectar_bd() #conecta o BD para armazenar os dados de aluno no SQL

    funcao.cursor.execute("""
        INSERT INTO alunos (nome, turma, data_nascimento)
        VALUES (?, ?, ?)
    """, (nome, turma, data)) #executa o comando SQL para inserir os dados dos alunos e atribuir valores a eles, ou seja, insere os dados do aluno que está sendo cadastrado no SQL, onde o nome, turma e data de nascimento são os valores que estão sendo inseridos no SQL

    funcao.conexao.commit() #confirma as alterações feitas no BD, ou seja, confirmar o cadastro do aluno no SQL para que os dados sejam armazenados e possam ser mostrados

    funcao.desconectar_bd() #desconecta o BD

    mostrar_alunos() #chama a função mostrar alunos para que os dados do aluno que foi cadastrado sejam mostrados na tabela treeview
    limpar() #chama a função limpar para que os campos de texto sejam limpos após o cadastro do aluno, ou seja, para que os campos de texto fiquem vazios e prontos para um novo cadastro


# -------- BOTÃO --------

Button(
    left_frame,
    text="Cadastrar",
    font=("Arial", 12),
    width=15,
    command=cadastro
).place(x=10, y=350) #cria o botão de cadastro para que a função de cadastro seja executada quando o botão for clicado
def limpar_treeview():

    resposta = messagebox.askyesno("Confirmação", "Deseja apagar todos os alunos?") #exibe uma caixa de mensagem para confirmar se o usuário deseja apagar todos os alunos cadastrados, ou seja, limpar a tabela treeview e o SQL, onde o usuário pode escolher entre sim ou não para confirmar a ação de limpar a tabela

    if resposta: #se a resposta for sim, ou seja, se o usuário confirmar que deseja apagar todos os alunos cadastrados, a função de limpar tabela será executada para apagar os dados dos alunos cadastrados no SQL e limpar a tabela treeview
 
        funcao.conectar_bd() #conecta o BD para executar o comando SQL de deletar os dados dos alunos cadastrados no SQL

        funcao.cursor.execute("DELETE FROM alunos") #executa o comando SQL para deletar todos os dados da tabela alunos, ou seja, excluir todos os dados dos alunos cadastrados no SQL para que a tabela fique vazia
        funcao.cursor.execute("DELETE FROM sqlite_sequence WHERE name='alunos'") #executa o comando SQL para resetar o autoincremento da tabela alunos, ou seja, para que os IDs dos alunos cadastrados sejam reiniciados a partir do número 1 após a exclusão de todos os dados dos alunos cadastrados no SQL
        funcao.conexao.commit() #confirma as alterações feitas no BD, ou seja, confirmar a exclusão dos dados dos alunos cadastrados no SQL para que os dados sejam apagados e a tabela fique vazia
        funcao.desconectar_bd() #desconecta o BD após a exclusão dos dados dos alunos cadastrados no SQL

        for item in abas.get_children():
            abas.delete(item) #pecorre os items da tabela e os deleta, ou seja, limpa a tabela para que os dados sejam atualizados e não tenha repetição de dados, ou seja, limpa a tabela treeview para que ela fique vazia após a exclusão dos dados dos alunos cadastrados no SQL

botao_limpar_treeview = Button(left_frame2, text="Limpar Tabela", font=("Arial", 12), width=15, command=limpar_treeview) #cria o botão de limpar tabela para que a função de limpar tabela seja executada quando o botão for clicado
botao_limpar_treeview.place(x=135, y=300) #define a posição do botão de limpar tabela, onde ele será mostrado na janela tkinter


mostrar_alunos() #chama a função mostrar alunos para que os dados dos alunos cadastrados sejam mostrados na tabela treeview

janela.mainloop() #mantém a janela tkinter aberta para que o programa seja executado e possa ser utilizado 