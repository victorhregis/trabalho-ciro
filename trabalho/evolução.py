from pokemon import Pokemon
class Evolução(Pokemon):
    def __init__(self, nome: str, tipo1: str, tipo2: str, habilidade: str, hp: int, attack: int, spattack: int, defense: int, spdefense: int, speed: int,pre_nome:str):
        super().__init__(nome, tipo1, tipo2, habilidade, hp, attack, spattack, defense, spdefense, speed)
        self.pre_nome = pre_nome
    def pre_ev_status(self,pre_hp:int,pre_attack:int,pre_spattack:int,pre_defense:int,pre_spdefense:int,pre_speed:int):
        self.pre_hp = pre_hp
        self.pre_attack = pre_attack
        self.pre_spattack = pre_spattack
        self.pre_defense = pre_defense
        self.pre_spdefense = pre_spdefense
        self.pre_speed = pre_speed
    def linha_evo(self,nomes_ev:str):
        if nomes_ev == False:
            self.nomes_ev = (f'{self.pre_nome}->{self.nome}')
        else:
            self.nomes_ev = (f'{nomes_ev}->{self.nome}')