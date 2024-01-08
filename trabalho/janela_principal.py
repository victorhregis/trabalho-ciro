from tkinter import *
from janela_login import login
from janela_registrar import registrar
class janela():
    def __init__(self,mestre = Tk):
        mestre.geometry("300x150")
        titulo = Label(mestre, text= 'Bem vindo!', font=('Ariel',15,'bold'))
        titulo.pack(padx=15,pady=15)
        mestre.title('Menu principal')
        butoes = Frame(mestre)
        butoes.pack()
        butao1 = Button(butoes,text='logar',height= 1, width=10,command=self.logar)
        butao1.pack(side= LEFT,padx=5)
        butao2 = Button(butoes,text='registrar',height= 1, width=10,command=self.regist)
        butao2.pack(side= LEFT,padx=5)
        butao4 = Button(mestre,text='sair',height= 1, width=7,command=mestre.destroy)
        butao4.pack(padx=30,pady=12)
    def logar(self):
        mestre.withdraw()
        mestre.wait_window(login().logar)
        mestre.deiconify()
    def regist(self):
        mestre.withdraw()
        mestre.wait_window(registrar().registra)
        mestre.deiconify()
mestre = Tk()
janela(mestre)
mestre.mainloop()