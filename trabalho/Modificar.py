from tkinter import *
from tkinter import messagebox
import pickle
class pokemon_base():
    def __init__(self,pokemon,posicao, master=None):
        self.pokemon = pokemon
        self.posicao = posicao
        self.base = Toplevel()
        self.base.title("Modificar")
        self.base.geometry("250x400")
        self.titulo = Label(self.base, text= 'Modificar:', font=('Ariel',12))
        self.titulo.pack()
        registra_nome = Frame(self.base,pady= 5)
        registra_nome.pack()
        self.nome = Label(registra_nome,text= 'Nome:')
        self.nome.pack(side=LEFT)
        self.nome_entry = Entry(registra_nome)
        self.nome_entry.pack(side=LEFT)
        self.nome_entry.insert(END,pokemon.nome)
        registra_tipo1 = Frame(self.base,pady= 5)
        registra_tipo1.pack()
        self.tipo1 = Label(registra_tipo1,text= 'Tipo1:')
        self.tipo1.pack(side=LEFT)
        self.tipo1_entry = Entry(registra_tipo1)
        self.tipo1_entry.pack(side=LEFT)
        self.tipo1_entry.insert(END,pokemon.tipo1)
        registra_tipo2 = Frame(self.base,pady= 5)
        registra_tipo2.pack()
        self.tipo2 = Label(registra_tipo2,text= 'Tipo2:')
        self.tipo2.pack(side=LEFT)
        self.tipo2_entry = Entry(registra_tipo2)
        self.tipo2_entry.pack(side=LEFT)
        self.tipo2_entry.insert(END,pokemon.tipo2)
        registra_habilidade1 = Frame(self.base,pady= 5)
        registra_habilidade1.pack()
        self.habilidade1 = Label(registra_habilidade1,text= 'Habilidade:')
        self.habilidade1.pack(side=LEFT)
        self.habilidade1_entry = Entry(registra_habilidade1)
        self.habilidade1_entry.pack(side=LEFT)
        self.habilidade1_entry.insert(END,pokemon.habilidade)
        registra_hp = Frame(self.base,pady= 5)
        registra_hp.pack()
        self.hp = Label(registra_hp,text= 'Hp:')
        self.hp.pack(side=LEFT)
        self.hp_entry = Entry(registra_hp)
        self.hp_entry.pack(side=LEFT)
        registra_attack = Frame(self.base,pady= 5)
        registra_attack.pack()
        self.attack = Label(registra_attack,text= 'Attack:')
        self.attack.pack(side=LEFT)
        self.attack_entry = Entry(registra_attack)
        self.attack_entry.pack(side=LEFT)
        registra_spattack = Frame(self.base,pady= 5)
        registra_spattack.pack()
        self.spattack = Label(registra_spattack,text= 'Sp.Attack:')
        self.spattack.pack(side=LEFT)
        self.spattack_entry = Entry(registra_spattack)
        self.spattack_entry.pack(side=LEFT)
        registra_defense = Frame(self.base,pady= 5)
        registra_defense.pack()
        self.defense = Label(registra_defense,text= 'Defense:')
        self.defense.pack(side=LEFT)
        self.defense_entry = Entry(registra_defense)
        self.defense_entry.pack(side=LEFT)
        registra_spdefense = Frame(self.base,pady= 5)
        registra_spdefense.pack()
        self.spdefense = Label(registra_spdefense,text= 'Sp.Defense:')
        self.spdefense.pack(side=LEFT)
        self.spdefense_entry = Entry(registra_spdefense)
        self.spdefense_entry.pack(side=LEFT)
        registra_speed = Frame(self.base,pady= 5)
        registra_speed.pack()
        self.speed = Label(registra_speed,text= 'Speed:')
        self.speed.pack(side=LEFT)
        self.speed_entry = Entry(registra_speed)
        self.speed_entry.pack(side=LEFT)
        self.botao1 = Button(self.base,text = "Editar",height= 1, width=9,command= self.alterar)
        self.botao1.pack()
        self.butao2 = Button(self.base,text='sair',height=1,width=7,command= self.voltar)
        self.butao2.pack(pady=5)

    def voltar(self):
        self.base.destroy()

    def alterar(self):
        arquivo = open("Pokemons.txt",'rb')
        retorno = pickle.load(arquivo)
        nome = self.nome_entry.get()
        tipo1 = self.tipo1_entry.get()
        tipo2 = self.tipo2_entry.get()
        habilidade1 = self.habilidade1_entry.get()
        hp = self.hp_entry.get()
        attack = self.attack_entry.get()
        spattack = self.spattack_entry.get()
        defense = self.defense_entry.get()
        spdefense = self.spdefense_entry.get()
        speed = self.speed_entry.get()
        self.pokemon.nome = nome
        self.pokemon.tipo1 = tipo1
        self.pokemon.tipo2 = tipo2
        self.pokemon.habilidade = habilidade1
        self.pokemon.hp = hp
        self.pokemon.attack = attack
        self.pokemon.spattack = spattack
        self.pokemon.defense = defense
        self.pokemon.spdefense = spdefense
        self.pokemon.speed = speed
        if self.pokemon.nomes_ev != False:
            if retorno[self.posicao - 1].nomes_ev == False:
                self.pokemon.nomes_ev = (f'{retorno[self.posicao - 1].nome}->{self.pokemon.nome}')
            else:
                self.pokemon.nomes_ev = (f'{retorno[self.posicao - 1].nomes_ev}->{self.pokemon.nome}')
        try:
            if retorno[self.posicao + 1] != False:
                retorno[self.posicao + 1].pre_hp = self.pokemon.hp
                retorno[self.posicao + 1].pre_attack = self.pokemon.attack
                retorno[self.posicao + 1].pre_spattack = self.pokemon.spattack
                retorno[self.posicao + 1].pre_defense = self.pokemon.defense
                retorno[self.posicao + 1].pre_spdefense = self.pokemon.spdefense
                retorno[self.posicao + 1].pre_speed = self.pokemon.speed
                if self.pokemon.nomes_ev == False:
                        retorno[self.posicao + 1].nomes_ev = (f'{self.pokemon.nome}->{retorno[self.posicao + 1].nome}')
                else:
                    retorno[self.posicao + 1].nomes_ev = (f'{self.pokemon.nomes_ev}->{retorno[self.posicao + 1].nome}')
                for evolu in range(self.posicao +2,retorno.index(retorno[-1])+1,1):
                    try:
                        if retorno[evolu].nomes_ev == False:
                            break
                        else:
                            retorno[evolu].nomes_ev = (f'{retorno[evolu-1].nomes_ev}->{retorno[evolu].nome}')
                    except IndexError:
                        break
        except IndexError:
            pass
        retorno[self.posicao] = self.pokemon
        cont = 0
        for pokemon in retorno:
            if pokemon.nome == retorno[self.posicao].nome:
                cont+=1
        if cont <= 1:
            arquivo = open("Pokemons.txt",'wb')
            pickle.dump(retorno,arquivo)
            messagebox.showinfo('Sucesso','Pokémon alterado com sucesso!')
        else:
            messagebox.showerror('Erro','Nome já usado!')