# coding: utf-8

# imports
from Poterie import Poterie
import GestionStock

def Main():
    """
    """

    GestionStock.CreerStock()
    Poterie.AfficheStock()

    # modifie la propriété d'instance Couleur
    # de la 1ère poterie de la liste (index 0)
    GestionStock.ModifierStock(Poterie.Liste[0], Couleur="jaune")
    Poterie.AfficheStock()

    # supprime la deuxième poterie de la liste (index 1)
    GestionStock.SupprimerStock(1)
    Poterie.AfficheStock()

    # appelle la méthode d'instance TombeParTerre
    # sur une poterie de la liste (la 1ère = index 0)
    Poterie.Liste[0].TombeParTerre()
    Poterie.AfficheStock()


# Code starts here
if __name__ == "__main__":
    Main()
    print()
