from tkinter import *
from pokédex import janela_pokédex

class janela_user:
    def __init__(self, master=None):
        self.user = Toplevel()
        self.user.title("Menu user")
        self.user.geometry("300x175")
        self.titulo = Label(self.user, text= 'Bem vindo usuário!', font=('Ariel',15,'bold'))
        self.titulo.pack(pady= 5)
        self.sub_titulo = Label(self.user,text= 'Opções Usuário:',font=('Ariel',12))
        self.sub_titulo.pack(pady=5)
        self.butao1 = Button(self.user, text='Pokédex',height=1,width= 9,command=self.poked)
        self.butao1.pack(pady= 5)
        self.butao2 = Button(self.user,text = 'Sair',height=1,width=7,command=self.voltar)
        self.butao2.pack(pady=5)
    
    def voltar(self):
        self.user.destroy()
    
    def poked(self):
        self.user.withdraw()
        self.user.wait_window(janela_pokédex().pokedex)
        self.user.deiconify()
