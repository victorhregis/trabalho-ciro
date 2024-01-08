from tkinter import *
from tkinter import messagebox
import pickle
class janela_excluir():
    def __init__(self, master=None):
        self.excluir = Toplevel()
        self.excluir.title("Excluir")
        self.excluir.geometry("250x100")
        self.sub_titulo1 = Label(self.excluir,text= 'Excluir:',font=('Ariel',12))
        self.frame1 = Frame(self.excluir)
        self.frame1.pack(pady= 5)
        self.nome = Label(self.frame1,text= 'Nome:')
        self.nome.pack(side=LEFT)
        self.nome_entry = Entry(self.frame1)
        self.nome_entry.pack(side=LEFT)
        self.botao1 = Button(self.excluir,text = "Excluir",height= 1, width=9,command= self.remover)
        self.botao1.pack()
        self.butao2 = Button(self.excluir,text='sair',height=1,width=7,command= self.voltar)
        self.butao2.pack(pady=5)

    def voltar(self):
        self.excluir.destroy()

    def remover(self):
        nome = self.nome_entry.get()
        try:
            arquivo = open('Pokemons.txt','rb')
            retorno = pickle.load(arquivo)
            cont = 0
            for pokemon in retorno:
                if pokemon.nome == nome:
                    lista_remover = []
                    lista_remover.append(pokemon)
                    for evolucoes in range(retorno.index(pokemon)+1,retorno.index(retorno[-1])+1,1):
                        if retorno[evolucoes].nomes_ev != False:
                            lista_remover.append(retorno[evolucoes])
                        else:
                            break
                    for removido in lista_remover:
                        retorno.remove(removido)
                    arquivo = open('Pokemons.txt','wb')
                    pickle.dump(retorno,arquivo)     
                    messagebox.showinfo('Sucesso','Pokémon removido com sucesso!')                   
                    cont+=1
                    break
            if cont == 0:
                messagebox.showerror('Erro','O pokémon não está na lista')
        except FileNotFoundError:
            messagebox.showerror('Erro','Não há pokédex')