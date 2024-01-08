from tkinter import *
from adicionar import janela_adicionar
from excluir import janela_excluir
from alterar import janela_alterar
from pokédex import janela_pokédex
from liberar_adm import janela_liberar_adm
class janela_adm():
    def __init__(self, master=None):
        self.adm = Toplevel()
        self.adm.title("Menu adm")
        self.adm.geometry("300x215")
        self.titulo = Label(self.adm, text= 'Bem vindo ADM!', font=('Ariel',15,'bold'))
        self.titulo.pack(pady=5)
        self.sub_titulo1 = Label(self.adm,text= 'Opções Pokémon:',font=('Ariel',12))
        self.sub_titulo1.pack(pady=5)
        self.botoes_1 = Frame(self.adm)
        self.botoes_1.pack()
        self.butao1 = Button(self.botoes_1,text='Adicionar',height= 1, width=9,command= self.adiciona)
        self.butao1.pack(pady= 5,padx=2,side = LEFT)   
        self.butao2 = Button(self.botoes_1,text='Editar',height= 1, width=9,command= self.altera)
        self.butao2.pack(pady= 5,padx=2,side= LEFT)
        self.butao3 = Button(self.botoes_1,text='Remover',height=1,width=9,command=self.exclui)
        self.butao3.pack(pady= 5,padx=2,side= LEFT)
        self.sub_titulo2 = Label(self.adm,text= 'Opções Usuário:',font=('Ariel',12))
        self.sub_titulo2.pack(pady=5)
        self.botoes_2 = Frame(self.adm)
        self.botoes_2.pack()
        self.butao5 = Button(self.botoes_2, text='Pokédex',height=1,width= 9,command=self.poked)
        self.butao5.pack(pady= 5,padx=2,side= LEFT)
        self.butao5 = Button(self.botoes_2, text='Libera Adm',height=1,width= 9,command=self.liberar)
        self.butao5.pack(pady= 5,padx=2,side= LEFT)
        self.butao6 = Button(self.adm,text = 'Sair',height=1,width=7,command=self.voltar)
        self.butao6.pack()


    def voltar(self):
        self.adm.destroy()
    
    def adiciona(self):
        self.adm.withdraw()
        self.adm.wait_window(janela_adicionar().adicionar)
        self.adm.deiconify()
    
    def exclui(self):
        self.adm.withdraw()
        self.adm.wait_window(janela_excluir().excluir)
        self.adm.deiconify()

    def altera(self):
        self.adm.withdraw()
        self.adm.wait_window(janela_alterar().alterar)
        self.adm.deiconify()

    def poked(self):
        self.adm.withdraw()
        self.adm.wait_window(janela_pokédex().pokedex)
        self.adm.deiconify()

    def liberar(self):
        self.adm.withdraw()
        self.adm.wait_window(janela_liberar_adm().libera)
        self.adm.deiconify()