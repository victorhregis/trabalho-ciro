from tkinter import *
import pickle
from usuario import Usuario
class registrar():
    def __init__(self, master=None):
        self.registra = Toplevel()
        self.registra.title("Menu login")
        self.registra.geometry("300x200")
        titulo = Label(self.registra, text= 'registrar', font=('Ariel',15,'bold'))
        titulo.pack()
        registra_nome = Frame(self.registra,pady= 10)
        registra_nome.pack()
        nome = Label(registra_nome,text= 'Nome:')
        nome.pack(side=LEFT)
        self.nome_entry = Entry(registra_nome)
        self.nome_entry.pack(side=LEFT)
        registra_senha = Frame(self.registra,pady= 10)
        registra_senha.pack()
        senha = Label(registra_senha,text= 'Senha:')
        senha.pack(side=LEFT)
        self.senha_entry = Entry(registra_senha)
        self.senha_entry.pack(side=LEFT)
        butao1 = Button(self.registra,text='Registrar',height= 1, width=7,command=self.registrar)
        butao1.pack(pady= 5)   
        butao2 = Button(self.registra,text='Sair',height= 1, width=7,command=self.voltar)
        butao2.pack(pady= 5)
        self.mensagem = Label(self.registra, text="")
        self.mensagem.pack()
    def voltar(self):
        self.registra.destroy()
    def registrar(self):
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