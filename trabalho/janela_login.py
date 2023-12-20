from tkinter import *
import pickle
from usuario import Usuario
class login():
    def __init__(self, master=None):
        self.logar = Toplevel()
        self.logar.title("Menu login")
        self.logar.geometry("300x200")
        titulo = Label(self.logar, text= 'Logar', font=('Ariel',15,'bold'))
        titulo.pack()
        logar_nome = Frame(self.logar,pady= 10)
        logar_nome.pack()
        nome = Label(logar_nome,text= 'Nome:')
        nome.pack(side=LEFT)
        self.nome_entry = Entry(logar_nome)
        self.nome_entry.pack(side=LEFT)
        logar_senha = Frame(self.logar,pady= 10)
        logar_senha.pack()
        senha = Label(logar_senha,text= 'Senha:')
        senha.pack(side=LEFT)
        self.senha_entry = Entry(logar_senha)
        self.senha_entry.pack(side=LEFT)
        butao1 = Button(self.logar,text='Logar',height= 1, width=7,command=self.loga)
        butao1.pack(pady= 5)   
        butao2 = Button(self.logar,text='sair',height= 1, width=7,command=self.voltar)
        butao2.pack(pady= 5)
        self.mensagem = Label(self.logar, text="")
        self.mensagem.pack()
    def voltar(self):
        self.logar.destroy()
    def loga(self):
        try:
            use = Usuario(self.nome_entry.get(),self.senha_entry.get())
            arquivo = open('Usuarios.txt','rb')
            retorno = pickle.load(arquivo)
            cont = 0
            for usuario in retorno:
                if usuario.nome == use.nome:
                    cont+=1
                    break
            if cont == 0:
                Message('yo','Usuario não existente')
        except FileNotFoundError:
            lista = []
            use_adm = Usuario('Victor','123')
            use_adm.virar_admin()
            lista.append(use_adm)
            use = Usuario(self.nome_entry,self.senha_entry)
            if use.nome == use_adm.nome and use.senha == use_adm.senha:
                self.mensagem['text'] = 'Logado com sucesso!'
            else:
                Message('yo','Usuario não existente')