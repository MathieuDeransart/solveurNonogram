from tkinter import *
from functools import partial
import numpy as np


class FenetreRenseignement():

    def __init__(self, largeurFenetre, hauteurFenetre, data=None):
        self.largeurFenetre = largeurFenetre
        self.hauteurFenetre = hauteurFenetre
        self.f = Tk()
        if data is None:
            data = np.zeros((hauteurFenetre, largeurFenetre), dtype=int)
        self.boutons = [[Button(self.f, text=str(data[i, j]), highlightbackground='white', fg='black', command=partial(self.changeTexte, i, j)) for j in range(largeurFenetre)] for i in range(hauteurFenetre)]
        for i in range(hauteurFenetre):
            for j in range(largeurFenetre):
                self.boutons[i][j].grid(row=i, column=j)
        self.quitter = Button(self.f, text="Valider", command=partial(self.f.quit))
        self.quitter.grid(row=hauteurFenetre+1, column=largeurFenetre+1)
        self.f.mainloop()

    def changeTexte(self, i, j):
        print(i, j)
        if self.boutons[i][j]["text"] == "0":
            self.boutons[i][j]["text"] = "1"
            self.boutons[i][j]["highlightbackground"] = 'black'
            self.boutons[i][j]["fg"] = 'white'
        else:
            self.boutons[i][j]["text"] = "0"
            self.boutons[i][j]["highlightbackground"] = 'white'
            self.boutons[i][j]["fg"] = 'black'

    def entrer(self):
        self.f.mainloop()

    def getGrid(self):
        grille = [[None for j in range(self.largeurFenetre)] for i in range(self.hauteurFenetre)]
        for i in range(self.hauteurFenetre):
            for j in range(self.largeurFenetre):
                if self.boutons[i][j]["text"] == "0": grille[i][j]= 0
                if self.boutons[i][j]["text"] == "1": grille[i][j]= 1
        return grille