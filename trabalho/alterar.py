from tkinter import *
from tkinter import messagebox
import pickle
from Modificar import pokemon_base
class janela_alterar():
    def __init__(self, master=None):
        self.alterar = Toplevel()
        self.alterar.title("alterar")
        self.alterar.geometry("250x100")
        self.sub_titulo1 = Label(self.alterar,text= 'Alterar:',font=('Ariel',12))
        self.frame1 = Frame(self.alterar)
        self.frame1.pack(pady= 5)
        self.nome = Label(self.frame1,text= 'Nome:')
        self.nome.pack(side=LEFT)
        self.nome_entry = Entry(self.frame1)
        self.nome_entry.pack(side=LEFT)
        self.botao1 = Button(self.alterar,text = "Alterar",height= 1, width=9,command= self.remover)
        self.botao1.pack()
        self.butao2 = Button(self.alterar,text='sair',height=1,width=7,command= self.voltar)
        self.butao2.pack(pady=5)

    def voltar(self):
        self.alterar.destroy()

    def remover(self):
        nome = self.nome_entry.get()
        try:
            arquivo = open('Pokemons.txt','rb')
            retorno = pickle.load(arquivo)
            cont = 0
            for pokemon in retorno:
                if pokemon.nome == nome:
                    posicao = retorno.index(pokemon)
                    self.alterar.withdraw()
                    self.alterar.wait_window(pokemon_base(pokemon,posicao).base)
                    self.alterar.deiconify()       
                    cont+=1
                    break
            if cont == 0:
                messagebox.showerror('Erro','O pokémon não está na lista')
        except FileNotFoundError:
            messagebox.showerror('Erro','Não há pokédex')