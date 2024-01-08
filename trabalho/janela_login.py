from tkinter import *
import pickle
from tkinter import messagebox
from usuario import Usuario
from Janela_adm import janela_adm
from Janela_usuario import janela_user
class login():
    def __init__(self, master=None):
        self.logar = Toplevel()
        self.logar.title("Menu login")
        self.logar.geometry("300x175")
        titulo = Label(self.logar, text= 'Logar', font=('Ariel',15,'bold'))
        titulo.pack()
        logar_nome = Frame(self.logar,pady= 10)
        logar_nome.pack()
        nome = Label(logar_nome,text= 'Nome:')
        nome.pack(side=LEFT)
        self.nome_entry = Entry(logar_nome)
        self.nome_entry.pack(side=LEFT)
        logar_senha = Frame(self.logar)
        logar_senha.pack()
        senha = Label(logar_senha,text= 'Senha:')
        senha.pack(side=LEFT)
        self.senha_entry = Entry(logar_senha,show='*')
        self.senha_entry.pack(side=LEFT)
        butao1 = Button(self.logar,text='Logar',height= 1, width=7,command=self.loga)
        butao1.pack(pady= 10)   
        butao2 = Button(self.logar,text='sair',height= 1, width=5,command=self.voltar)
        butao2.pack()
    def voltar(self):
        self.logar.destroy()
    def loga(self):
        try:
            nome = self.nome_entry.get()
            senha = self.senha_entry.get()
            use = Usuario(nome,senha)
            arquivo = open('Usuarios.txt','rb')
            retorno = pickle.load(arquivo)
            cont = 0
            for usuario in retorno:
                if usuario.nome == use.nome and usuario.senha == use.senha:
                    cont+=1
                    if usuario.return_adm() == True:
                        self.logar.withdraw()
                        self.logar.wait_window(janela_adm().adm)
                        self.logar.deiconify()
                    else:
                        self.logar.withdraw()
                        self.logar.wait_window(janela_user().user)
                        self.logar.deiconify()
                    break
            if cont == 0:
                messagebox.showerror('Erro','Usuario não existe')
        except FileNotFoundError:
            lista = []
            nome = self.nome_entry.get()
            senha = self.senha_entry.get()
            use_adm = Usuario('Victor','123')
            use_adm.virar_admin()
            lista.append(use_adm)
            arquivo = open('Usuarios.txt','wb')
            pickle.dump(lista,arquivo)
            if nome == use_adm.nome and senha == use_adm.senha:
                self.logar.withdraw()
                self.logar.wait_window(janela_adm().adm)
                self.logar.deiconify()
            else:
                messagebox.showerror('Erro','Usuario não existe')