# coding: utf-8



# DictPoterie = {
#     "Type" : "Vase",
#     "Taille" : 100,
#     "Couleur" : "Marron"
# }



# Code starts here
if __name__ == "__main__":

    # print(f"Un {DictPoterie['type']} {DictPoterie['Couleur']} de {DictPoterie['Taille']}cm")

    ListePoteries = []

    # Poterie1 est :
    #   une variable de main
    #   un objet
    #   une instance de la classe Poterie

    Poterie1 = Poterie(Couleur="bleu")
    ListePoteries.append(Poterie1)
    Poterie2 = Poterie(Taille=120, Couleur="vert")
    ListePoteries.append(Poterie2)
    Poterie3 = Poterie("Bol", 50)
    ListePoteries.append(Poterie3)

    # print(f"Un {Poterie1.Type} {Poterie1.Couleur} de {Poterie1.Taille}cm")
    # print(f"Un {Poterie2.Type} {Poterie2.Couleur} de {Poterie2.Taille}cm")
    # print(f"Un {Poterie3.Type} {Poterie3.Couleur} de {Poterie3.Taille}cm")

    AfficheStockPoteries()

    print()

    Poterie1.Couleur = "jaune"
    AfficheStockPoteries()
