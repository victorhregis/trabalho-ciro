class Usuario():
    def __init__(self,nome,senha):
        self.nome = nome
        self.senha = senha
        self.__admin = False
    def virar_admin(self):
        self.__admin = True