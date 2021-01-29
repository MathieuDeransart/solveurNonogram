from Nonogram import Nonogram
import matplotlib.pyplot as plt
import numpy as np

# -1 pour résoudre un problème quelconque
# de 0 à 6 pour voir les différents tests
numero_test = 2  # 3 ne fonctionne pas

if numero_test == -1:
    largeur = int(input("Largeur de la grille :"))
    hauteur = int(input("Hauteur de la grille :"))
    dessin = Nonogram(hauteur, largeur)
    dessin.saisie_indications()
    dessin.resolution()
    dessin.afficher()

elif numero_test == 0:
    ligne = 3
    colonne = 2
    indication_lignes = [[1], [1], [1]]
    indication_colonnes = [[1, 1], [1]]

    dessin = Nonogram(ligne, colonne, indication_lignes, indication_colonnes)
    print(dessin.table)
    print(dessin.resolution())
    dessin.afficher()

elif numero_test == 1:
    ligne = 2
    colonne = 6
    indication_lignes = [[2, 1], [1, 3]]
    indication_colonnes = [[1], [2], [], [1], [1], [2]]

    dessin = Nonogram(ligne, colonne, indication_lignes, indication_colonnes)
    print(dessin.table)
    print(dessin.resolution())
    dessin.afficher()

elif numero_test == 2:
    ligne = 6
    colonne = 6
    indication_lignes = [[2, 1], [1, 3], [1, 2], [3], [4], [1]]
    indication_colonnes = [[1], [5], [2], [5], [2, 1], [2]]

    dessin = Nonogram(ligne, colonne, indication_lignes, indication_colonnes)
    print(dessin.table)
    print(dessin.resolution())
    print(dessin.table)
    plt.imshow(dessin.table)
    plt.show()

    dessin.create_indication_from_table()
    print(dessin.indication_lignes)
    print(dessin.indication_colonnes)

elif numero_test == 3:
    ligne = 25
    colonne = 25
    indication_lignes = [[7], [11], [3, 3], [3, 3], [4, 2],
                         [3, 2], [2, 1, 2], [3, 6, 1], [2, 2, 1, 2], [1, 1, 6, 1],
                         [2, 2, 1, 2], [3, 2, 2, 2], [3, 2, 4, 1, 1], [2, 4, 1, 1, 2, 2, 1], [2, 12, 2, 1],
                         [1, 1, 15, 1], [1, 2, 2, 6, 2, 1], [5, 5, 1, 1], [4, 5, 3], [3, 6, 2],
                         [3, 1, 5, 1], [2, 1, 2, 2, 2], [1, 5, 1, 2], [1, 5, 1, 2], [7, 1, 2]]
    indication_colonnes = [[6, 6, 7], [6, 4, 5, 1], [4, 1, 3, 5, 3], [3, 2, 4, 4], [2, 1, 3],
                           [1, 2, 4], [2, 2, 1, 6], [2, 6, 3], [2, 12], [2, 12],
                           [2, 7], [2, 2, 8], [2, 1, 4, 5], [2, 1, 3, 3], [2, 3, 1, 2],
                           [2, 9], [1, 1, 1, 2, 2], [2, 2, 1, 2], [2, 1, 1, 1], [2, 2, 3],
                           [3, 3], [2, 2, 2], [2, 1, 4], [2, 2], [6]]

    dessin = Nonogram(ligne, colonne, indication_lignes, indication_colonnes)
    print(dessin.table)
    print(dessin.resolution())
    print(dessin.table)
    plt.imshow(dessin.table)
    plt.show()

elif numero_test == 4:
    ligne = 15
    colonne = 15
    indication_lignes = [[3], [5], [4, 3], [7], [5],
                         [3], [5], [1, 8], [3, 3, 3], [7, 3, 2],
                         [5, 4, 2], [8, 2], [10], [2, 3], [6]]
    indication_colonnes = [[3], [4], [5], [4], [5],
                           [6], [3, 2, 1], [2, 2, 5], [4, 2, 6], [8, 2, 3],
                           [8, 2, 1, 1], [2, 6, 2, 1], [4, 6], [2, 4], [1]]

    dessin = Nonogram(ligne, colonne, indication_lignes, indication_colonnes)
    print(dessin.table)
    print(dessin.resolution())
    print(dessin.table)
    plt.imshow(dessin.table)
    plt.show()

elif numero_test == 5:
    ligne = 25
    colonne = 20
    indication_lignes = [[3, 8], [3, 10], [3, 5, 4], [3, 4, 3], [3, 5, 1, 4],
                         [3, 3, 1, 1, 3], [3, 4, 2], [3, 6, 1, 3], [3, 8, 5], [3, 2, 2, 8],
                         [5, 1, 7], [4, 1, 7], [3, 1, 4, 1], [2, 2, 2], [1, 3, 1, 2],
                         [1, 4, 2, 2, 2], [2, 2, 2, 1, 1], [2, 4, 1, 2], [3, 1, 1, 1, 2], [5, 2, 4],
                         [1, 2, 4], [2, 4], [2, 1], [2, 1], [1, 1]]
    indication_colonnes = [[17, 2], [14, 2, 2], [13, 2, 2], [2, 1, 4], [2, 1, 2],
                           [2, 3, 1], [3, 4, 1], [5, 2, 1, 2], [8, 3, 2, 2], [10, 5, 1],
                           [5, 4, 1, 6], [6, 2, 2], [3, 2, 1, 1], [2, 2, 3, 2, 2], [2, 1, 4, 5],
                           [3, 2, 7, 1], [16, 2], [12, 4], [3, 5, 1], [5]]

    dessin = Nonogram(ligne, colonne, indication_lignes, indication_colonnes)
    print(dessin.table)
    print(dessin.resolution())
    print(dessin.table)
    plt.imshow(dessin.table)
    plt.show()

elif numero_test == 6:
    dessin = Nonogram(25, 20)
    dessin.dessiner()
    dessin.create_indication_from_table()
    print(dessin.indication_lignes)
    print(dessin.indication_colonnes)

    dessin2 = Nonogram(25, 20, dessin.indication_lignes, dessin.indication_colonnes)
    dessin2.resolution()
    plt.imshow(dessin2.table)
    plt.show()

elif numero_test == 7:
    dessin = Nonogram(25, 20)
    dessin.table = np.array([[1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
     [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
     [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0],
     [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0],
     [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
     [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
     [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
     [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0],
     [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
     [1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
     [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
     [1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
     [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
     [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0],
     [1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
     [0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
     [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
     [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    dessin.create_indication_from_table()
    print(dessin.indication_lignes)
    print(dessin.indication_colonnes)

