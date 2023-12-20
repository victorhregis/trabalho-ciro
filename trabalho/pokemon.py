class Pokemon():
    nomes_ev = False
    def __init__(self,nome:str,tipo1:str,tipo2:str,habilidade:str,habilidade2:str,descrisao:str,hp:int,attack:int,spattack:int,defense:int,spdefense:int,speed:int):
        self.nome = nome
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.habilidade = habilidade
        self.habilidade2 = habilidade2
        self.descrisao = descrisao
        self.hp = hp
        self.attack = attack
        self.spattack = spattack
        self.defense = defense
        self.spdefense = spdefense
        self.speed = speed