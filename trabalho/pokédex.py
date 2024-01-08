from tkinter import *
import pickle
from tkinter import messagebox
class janela_pokédex():
    def __init__(self, master=None):
        self.pokedex = Toplevel()
        self.pokedex.title("Pokédex")
        self.pokedex.geometry("500x360")
        try:
            try:
                self.pag = 0
                arquivo = open('Pokemons.txt','rb')
                retorno = pickle.load(arquivo)
                retorno[0]
                self.nome = Label(self.pokedex,text= 'Pokémon:',font=('Ariel',12,'bold'))
                self.nome.pack()
                self.frame1 = Frame(self.pokedex)
                self.frame1.pack()
                self.tabela = Text(self.frame1,height=15,width=40)
                self.tabela.pack(pady=5)
                self.tabela.insert(END,'posição:' + str(self.pag +1) + "\n" + "\n")
                self.tabela.insert(END,"Nome:" + retorno[0].nome + "\n" + "\n")
                if retorno[0].tipo1 == retorno[0].tipo2:
                    self.tabela.insert(END,'Tipo:' + retorno[0].tipo1 + "\n")
                else:
                    self.tabela.insert(END,'Tipos:' + retorno[0].tipo1 + "/" + retorno[0].tipo2 + "\n")
                self.tabela.insert(END,"Habilidade:" + retorno[0].habilidade + "\n" +"\n")
                self.tabela.insert(END,'Hp:' + retorno[0].hp + "\n")
                self.tabela.insert(END,'Attack:' + retorno[0].attack + "\n")
                self.tabela.insert(END,'Spattack:' + retorno[0].spattack + "\n")
                self.tabela.insert(END,'Defense:' + retorno[0].defense + "\n")
                self.tabela.insert(END,'Spdefense:' + retorno[0].spdefense + "\n")
                self.tabela.insert(END,'Speed:' + retorno[0].speed + "\n")
                self.frame2 = Frame(self.pokedex)
                self.frame2.pack()
                self.botao1 = Button(self.frame2,text = "<",height= 1, width=7,command= self.esquerda)
                self.botao1.pack(pady=5,padx=5,side=LEFT)
                self.butao2 = Button(self.frame2,text='>',height=1,width=7,command= self.direita)
                self.butao2.pack(pady=5,padx=5,side=LEFT)
                self.butao3 = Button(self.pokedex,text='Sair',height=1,width=7,command= self.voltar)
                self.butao3.pack()
            except IndexError:
                self.nome = Label(self.pokedex,text= 'Pokédex não existe!',font=('Ariel',12,'bold'))
                self.nome.pack()
                self.butao3 = Button(self.pokedex,text='Sair',height=1,width=7,command= self.voltar)
                self.butao3.pack()
        except FileNotFoundError:
            self.nome = Label(self.pokedex,text= 'Pokédex não existe!',font=('Ariel',12,'bold'))
            self.nome.pack()
            self.butao3 = Button(self.pokedex,text='Sair',height=1,width=7,command= self.voltar)
            self.butao3.pack()
    def voltar(self):
        self.pokedex.destroy()
    
    def esquerda(self):
        arquivo = open('Pokemons.txt','rb')
        retorno = pickle.load(arquivo)
        if self.pag == 0:
            messagebox.showerror('Erro','não ha pokémons nesse sentido')
        else:
            self.tabela.delete('1.0',END)
            self.pag -=1
            self.tabela.insert(END,'posição:' + str(self.pag +1) + "\n" + "\n")
            self.tabela.insert(END,'Nome:' + retorno[self.pag].nome + "\n" + "\n")
            if retorno[self.pag].tipo1 == retorno[self.pag].tipo2:
                self.tabela.insert(END,'Tipo:' + retorno[self.pag].tipo1 + "\n")
            else:
                self.tabela.insert(END,'Tipos:' + retorno[self.pag].tipo1 + "/" + retorno[self.pag].tipo2 + "\n")
            self.tabela.insert(END,'Habilidade:' + retorno[self.pag].habilidade + "\n")
            if retorno[self.pag].nomes_ev == False:
                self.tabela.insert(END,"\n")
                self.tabela.insert(END,'Hp:'+ retorno[self.pag].hp + "\n")
                self.tabela.insert(END, 'Attack:'+ retorno[self.pag].attack + "\n")
                self.tabela.insert(END, 'Spattack:' + retorno[self.pag].spattack + "\n")
                self.tabela.insert(END, 'Defense:'+retorno[self.pag].defense + "\n")
                self.tabela.insert(END, 'Spdefense:'+retorno[self.pag].spdefense + "\n")
                self.tabela.insert(END, 'Speed:'+retorno[self.pag].speed + "\n")
            else:
                self.tabela.insert(END,'Linha evolutiva:'+ retorno[self.pag].nomes_ev + "\n" + "\n")
                self.tabela.insert(END,'Hp:'+ retorno[self.pag].pre_hp + '->'+ retorno[self.pag].hp + "\n")
                self.tabela.insert(END, 'Attack:'+ retorno[self.pag].pre_attack + '->'+ retorno[self.pag].attack + "\n")
                self.tabela.insert(END, 'Spattack:' + retorno[self.pag].pre_spattack + '->' + retorno[self.pag].spattack + "\n")
                self.tabela.insert(END, 'Defense:'+retorno[self.pag].pre_defense + '->' + retorno[self.pag].defense + "\n")
                self.tabela.insert(END, 'Spdefense:'+retorno[self.pag].pre_spdefense + '->' + retorno[self.pag].spdefense + "\n")
                self.tabela.insert(END, 'Speed:'+retorno[self.pag].pre_speed + '->' + retorno[self.pag].speed + "\n")

    def direita(self):
        arquivo = open('Pokemons.txt','rb')
        retorno = pickle.load(arquivo)
        if self.pag == retorno.index(retorno[-1]):
            messagebox.showerror('Erro','não ha pokémons nesse sentido')
        else:
            self.tabela.delete('1.0',END)
            self.pag +=1
            self.tabela.insert(END,'posição:' + str(self.pag +1) + "\n" + "\n")
            self.tabela.insert(END,'Nome:' + retorno[self.pag].nome + "\n" + "\n")
            if retorno[self.pag].tipo1 == retorno[self.pag].tipo2:
                self.tabela.insert(END,'Tipo:' + retorno[self.pag].tipo1 + "\n")
            else:
                self.tabela.insert(END,'Tipos:' + retorno[self.pag].tipo1 + "/" + retorno[self.pag].tipo2 + "\n")
            self.tabela.insert(END,'Habilidade:' + retorno[self.pag].habilidade + "\n")
            if retorno[self.pag].nomes_ev == False:
                self.tabela.insert(END,"\n")
                self.tabela.insert(END,'Hp:'+ retorno[self.pag].hp + "\n")
                self.tabela.insert(END, 'Attack:'+ retorno[self.pag].attack + "\n")
                self.tabela.insert(END, 'Spattack:' + retorno[self.pag].spattack + "\n")
                self.tabela.insert(END, 'Defense:'+retorno[self.pag].defense + "\n")
                self.tabela.insert(END, 'Spdefense:'+retorno[self.pag].spdefense + "\n")
                self.tabela.insert(END, 'Speed:'+retorno[self.pag].speed + "\n")
            else:
                self.tabela.insert(END,'Linha evolutiva:'+ retorno[self.pag].nomes_ev + "\n" + "\n")
                self.tabela.insert(END,'Hp:'+ retorno[self.pag].pre_hp + '->'+ retorno[self.pag].hp + "\n")
                self.tabela.insert(END, 'Attack:'+ retorno[self.pag].pre_attack + '->'+ retorno[self.pag].attack + "\n")
                self.tabela.insert(END, 'Spattack:' + retorno[self.pag].pre_spattack + '->' + retorno[self.pag].spattack + "\n")
                self.tabela.insert(END, 'Defense:'+retorno[self.pag].pre_defense + '->' + retorno[self.pag].defense + "\n")
                self.tabela.insert(END, 'Spdefense:'+retorno[self.pag].pre_spdefense + '->' + retorno[self.pag].spdefense + "\n")
                self.tabela.insert(END, 'Speed:'+retorno[self.pag].pre_speed + '->' + retorno[self.pag].speed + "\n")