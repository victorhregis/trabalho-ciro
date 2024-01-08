from tkinter import *
import pickle
from tkinter import messagebox
from usuario import Usuario
class registrar():
    def __init__(self, master=None):
        self.registra = Toplevel()
        self.registra.title("Menu registrar")
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
        self.senha_entry = Entry(registra_senha,show='*')
        self.senha_entry.pack(side=LEFT)
        self.registra_botoes = Frame(self.registra)
        self.registra_botoes.pack()
        butao1 = Button(self.registra_botoes,text='Registrar',height= 1, width=11,command=self.registrar)
        butao1.pack(pady= 5,padx= 5,side= LEFT)
        butao2 = Button(self.registra_botoes,text='Registrar/adm',height= 1, width=11,command=self.registrar_adm)
        butao2.pack(pady= 5,padx= 5,side= LEFT)   
        butao3 = Button(self.registra,text='Sair',height= 1, width=7,command=self.voltar)
        butao3.pack(pady= 5)

    def voltar(self):
        self.registra.destroy()

    def registrar(self):
        try:
            nome = self.nome_entry.get()
            senha = self.senha_entry.get()
            use = Usuario(nome,senha)
            arquivo = open('Usuarios.txt','rb')
            retorno = pickle.load(arquivo)
            cont = 0
            for usuario in retorno:
                if usuario.nome == use.nome:
                    cont+=1
                    break
            try:
                    arquivo = open('Usuarios_espera.txt','rb')
                    retorno = pickle.load(arquivo)
                    for usuario in retorno:
                        if use.nome == usuario.nome:
                            cont+=1
                            break
            except FileNotFoundError:
                pass
            if cont == 0:
                arquivo = open('Usuarios.txt','rb')
                retorno = pickle.load(arquivo)
                retorno.append(use)
                arquivo = open('Usuarios.txt','wb')
                pickle.dump(retorno,arquivo)
                messagebox.showinfo('Sucesso','Usuario registrado!')
            else:
                messagebox.showerror('Erro','Usuario já existe')
        except FileNotFoundError:
            lista = []
            use_adm = Usuario('Victor','123')
            use_adm.virar_admin()
            lista.append(use_adm)
            nome = self.nome_entry.get()
            senha = self.senha_entry.get()
            use = Usuario(nome,senha)
            if use.nome == use_adm.nome:
                messagebox.showerror('Erro','Usuario já existe')
            else:
                try:
                    arquivo = open('Usuarios_espera.txt','rb')
                    retorno = pickle.load(arquivo)
                    for usuario in retorno:
                        if use.nome == usuario.nome:
                            messagebox.showerror('Erro','Usuario já existe')
                            break
                except FileNotFoundError:
                    pass
                lista.append(use)
                arquivo = open('Usuarios.txt','wb')
                pickle.dump(lista,arquivo)
                messagebox.showinfo('Sucesso','Usuario registrado!')

    def registrar_adm(self):
        try:
            nome = self.nome_entry.get()
            senha = self.senha_entry.get()
            use = Usuario(nome,senha)
            arquivo = open('Usuarios.txt','rb')
            retorno = pickle.load(arquivo)
            cont = 0
            for usuario in retorno:
                if usuario.nome == use.nome:
                    cont+=1
                    break
            if cont == 0:
                try:
                    arquivo = open('Usuarios_espera.txt','rb')
                    retorno = pickle.load(arquivo)
                    for usuario in retorno:
                        if use.nome == usuario.nome:
                            cont+=1
                            break
                    if cont == 0:
                        retorno.append(use)
                        arquivo = open('Usuarios_espera.txt','wb')
                        pickle.dump(retorno,arquivo)
                        messagebox.showinfo('Aguarde','Aguarde um adm liberar')
                    else:
                        messagebox.showerror('Erro','Usuario já existe')
                except FileNotFoundError:
                    arquivo = open('Usuarios_espera.txt','wb')
                    lista = []
                    lista.append(use)
                    pickle.dump(lista,arquivo)
                    messagebox.showinfo('Aguarde','Aguarde um adm liberar')
            else:
                messagebox.showerror('Erro','Usuario já existe')
        except FileNotFoundError:
            lista = []
            use_adm = Usuario('Victor','123')
            use_adm.virar_admin()
            lista.append(use_adm)
            nome = self.nome_entry.get()
            senha = self.senha_entry.get()
            use = Usuario(nome,senha)
            arquivo = open('Usuarios.txt','wb')
            pickle.dump(lista,arquivo)
            if use.nome == use_adm.nome:
                messagebox.showerror('Erro','Usuario já existe')
            else:
                try:
                    arquivo = open('Usuarios_espera.txt','rb')
                    retorno = pickle.load(arquivo)
                    cont = 0
                    for usuario in retorno:
                        if use.nome == usuario.nome:
                            cont+=1
                            break
                    if cont == 0:
                        retorno.append(use)
                        arquivo = open('Usuarios_espera.txt','wb')
                        pickle.dump(retorno,arquivo)
                        messagebox.showinfo('Aguarde','Aguarde um adm liberar')
                    else:
                        messagebox.showerror('Erro','Usuario já existe')
                except FileNotFoundError:
                    arquivo = open('Usuarios_espera.txt','wb')
                    lista = []
                    lista.append(use)
                    pickle.dump(lista,arquivo)
                    messagebox.showinfo('Aguarde','Aguarde um adm liberar')