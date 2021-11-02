# coding: utf-8

class Poterie:
    """
        Modèle pour créer des poteries
    """

    # Propriétés de classe
    Liste = []

    # Méthodes d'instance
    # le premier argument doit être self (c'est à dire l'objet courant)
    # argument invisible lors de l'appel
    def __init__(
        self, 
        Type = "Vase", 
        Taille = 100, 
        Couleur = "marron"):
        """
            Constructeur
        """

        # propriétés d'instance
        self.Type = Type
        self.Taille = Taille
        self.Couleur = Couleur
        self.EstCassee = False

    
    def TombeParTerre(self):
        """
        """

        self.EstCassee = True

    
    # Méthodes de classe
    # le premier argument doit être cls (c'est à dire la classe)
    # argument invisible lors de l'appel
    @classmethod
    def AfficheStock(cls):
        """
            Affiche la liste de mon stock de poteries
        """
        
        print(f"\nMon stock de {len(cls.Liste)} poteries")

        # pour chaque poterie de ma liste (de poteries)
        for MaPoterie in cls.Liste:
            # afficher les infos de la poterie
            CasseString = " cassé" if MaPoterie.EstCassee else ""
            print(f"Un {MaPoterie.Type} {MaPoterie.Couleur} de {MaPoterie.Taille}cm{CasseString}")
