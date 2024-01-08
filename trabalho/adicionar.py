from tkinter import *
import pickle
from Base import pokemon_base
from evo import pokemon_evo
class janela_adicionar():
    def __init__(self, master=None):
        self.adicionar = Toplevel()
        self.adicionar.title("Menu adicionar")
        self.adicionar.geometry("300x125")
        self.sub_titulo1 = Label(self.adicionar,text= 'Opções:',font=('Ariel',12))
        self.sub_titulo1.pack(pady=5)
        self.botoes_1 = Frame(self.adicionar)
        self.botoes_1.pack()
        self.butao1 = Button(self.botoes_1,text='Base',height= 1, width=9,command= self.janela_base)
        self.butao1.pack(pady= 5,padx=2,side = LEFT)   
        self.butao2 = Button(self.botoes_1,text='Evolução',height= 1, width=9,command= self.janela_evo)
        self.butao2.pack(pady= 5,padx=2,side= LEFT)
        self.butao3 = Button(self.adicionar,text='sair',height=1,width=7,command= self.voltar)
        self.butao3.pack()

    def voltar(self):
        self.adicionar.destroy()

    def janela_base(self):
        self.adicionar.withdraw()
        self.adicionar.wait_window(pokemon_base().base)
        self.adicionar.deiconify()
    
    def janela_evo(self):
        self.adicionar.withdraw()
        self.adicionar.wait_window(pokemon_evo().base)
        self.adicionar.deiconify()