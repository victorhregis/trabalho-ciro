from tkinter import *
from tkinter import messagebox
import pickle

class janela_liberar_adm():
    def __init__(self, master=None):
        self.libera = Toplevel()
        self.libera.title("Menu liberar")
        self.libera.geometry("300x235")
        self.titulo = Label(self.libera, text= 'Pedidos:', font=('Ariel',12))
        self.titulo.pack(pady= 5)
        try:
            arquivo = open('Usuarios_espera.txt','rb')
            retorno = pickle.load(arquivo)
            try:
                retorno[0]
                self.frame_tabela = Frame(self.libera)
                self.frame_tabela.pack(pady=5)
                self.tabela = Text(self.frame_tabela,height=5,width=25)
                self.tabela.pack()
                for use in retorno:
                    self.tabela.insert(END,'Nome:' + use.nome + "\n")
                self.frame1 = Frame(self.libera)
                self.frame1.pack(pady= 5)
                self.nome = Label(self.frame1,text= 'Nome:')
                self.nome.pack(side=LEFT)
                self.nome_entry = Entry(self.frame1)
                self.nome_entry.pack(side=LEFT)
                self.frame_botoes = Frame(self.libera)
                self.frame_botoes.pack(pady=5)
                self.botao1 = Button(self.frame_botoes,text='Aprovar',height=1,width=9,command=self.aprovar)
                self.botao1.pack(side=LEFT,padx=2)
                self.botao2 = Button(self.frame_botoes,text='Recusar',height=1,width=9,command=self.recusar)
                self.botao2.pack(side=LEFT,padx=2)

            except IndexError:
                self.titulo2 = Label(self.libera, text= 'Nenhum Pedido!', font=('Ariel',10))
                self.titulo2.pack(pady=10)
        except FileNotFoundError:
            self.titulo2 = Label(self.libera, text= 'Nenhum Pedido!', font=('Ariel',10))
            self.titulo2.pack(pady=10)
        self.frame_sair = Frame(self.libera)
        self.frame_sair.pack(pady= 5)
        self.butao_sair = Button(self.frame_sair,text = 'Sair',height=1,width=7,command=self.voltar)
        self.butao_sair.pack()

    def voltar(self):
        self.libera.destroy()
    
    def aprovar(self):
        user = self.nome_entry.get()
        arquivo = open('Usuarios_espera.txt','rb')
        retorno = pickle.load(arquivo)
        cont = 0
        for adm in retorno:
            if adm.nome == user:
                adm.virar_admin()
                retorno.remove(adm)
                arquivo = open('Usuarios_espera.txt','wb')
                pickle.dump(retorno,arquivo)
                arquivo = open('Usuarios.txt','rb')
                retorno = pickle.load(arquivo)
                retorno.append(adm)
                arquivo = open('Usuarios.txt','wb')
                pickle.dump(retorno,arquivo)
                messagebox.showinfo('Sucesso','Liberado!')
                self.tabela.delete('1.0',END)
                arquivo = open('Usuarios_espera.txt','rb')
                retorno = pickle.load(arquivo)
                if not retorno:
                    self.tabela.destroy()
                    self.texto = Label(self.frame_tabela, text= 'Nenhum Pedido!', font=('Ariel',10))
                    self.texto.pack()
                    self.frame1.destroy()
                    self.frame_botoes.destroy()
                else:    
                    for use in retorno:
                        self.tabela.insert(END,'Nome:' + use.nome + "\n")                
                cont +=1
                break
        if cont == 0:
            messagebox.showerror('Erro','Nome incorreto!')

    def recusar(self):
        user = self.nome_entry.get()
        arquivo = open('Usuarios_espera.txt','rb')
        retorno = pickle.load(arquivo)
        cont = 0
        for adm in retorno:
            if adm.nome == user:
                retorno.remove(adm)
                arquivo = open('Usuarios_espera.txt','wb')
                pickle.dump(retorno,arquivo)

                messagebox.showinfo('Sucesso','Recusado!')
                self.tabela.delete('1.0',END)
                arquivo = open('Usuarios_espera.txt','rb')
                retorno = pickle.load(arquivo)
                if not retorno:
                    self.tabela.destroy()
                    self.texto = Label(self.frame_tabela, text= 'Nenhum Pedido!', font=('Ariel',10))
                    self.texto.pack()
                    self.frame1.destroy()
                    self.frame_botoes.destroy()
                else:    
                    for use in retorno:
                        self.tabela.insert(END,'Nome:' + use.nome + "\n")                
                cont +=1
                break
        if cont == 0:
            messagebox.showerror('Erro','Nome incorreto!')