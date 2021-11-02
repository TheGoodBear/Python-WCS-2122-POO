# coding: utf-8

from Poterie import Poterie


def CreerStock():
    """
    """
  
    # créer une nouvelle instance de Poterie
    # nommée Poterie1
    Poterie1 = Poterie(Couleur="bleu")
    # l'ajouter à la liste des instances (Poterie.Liste)
    Poterie.Liste.append(Poterie1)

    # idem pour Poterie2 et Poterie3
    Poterie2 = Poterie(Taille=120, Couleur="vert")
    Poterie.Liste.append(Poterie2)
    Poterie3 = Poterie("Bol", 50)
    Poterie.Liste.append(Poterie3)


def ModifierStock(
    MaPoterie, 
    Couleur = None, 
    EstCassee = None):
    """
        MaPoterie est un objet de type Poterie
    """
  
    # modifie une valeur de propriété d'instance
    # de l'instance MaPoterie
    if Couleur is not None:
        MaPoterie.Couleur = Couleur

    if EstCassee is not None:
        MaPoterie.EstCassee = EstCassee


def SupprimerStock(IndexPoterie):
    """
        MaPoterie est un objet de type Poterie
    """
  
    # modifie une valeur de propriété d'instance
    # de l'instance MaPoterie
    Poterie.Liste.pop(IndexPoterie)



# Code starts here
# if __name__ == "__main__":

#     # print(f"Un {DictPoterie['type']} {DictPoterie['Couleur']} de {DictPoterie['Taille']}cm")

#     Poterie.AfficheStock()
