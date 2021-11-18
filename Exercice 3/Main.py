# coding: utf-8

# imports
import random
import time
import json
from Animal import Animal

# functions
def Main() -> None:
    """
    """

    print("Animaux du monde\n")

    # Exercice 1
    FaireNaitre()

    # Exercice 2
    FaireViellir()

    # end
    print("\nAu revoir")


def FaireNaitre() -> None:
    """
        Demander à l'utilisateur 
        combien d'animaux doivent naitre    
    """
    AnimalsData = openFile('./Exercice 3/data')

    # get number of animals to create
    NumberOfAnimals = 0

    while NumberOfAnimals < 2 or NumberOfAnimals > 10:
        try:
            NumberOfAnimals = int(input("Combien d'animaux dois-je faire naitre ? (entre 2 - 10) : "))
        except ValueError:
            print("Il faut saisir un nombre entre 2 et 10")

    Species = list(AnimalsData)
    
    # create appropriate number of animals
    for Number in range(NumberOfAnimals):
        SelectedSpecie = random.choice(Species)
        SelectedName = [
            Name 
            for Name 
            in AnimalsData[SelectedSpecie]["names"] 
            if not Name in 
                [
                    AnimalName.Name
                    for AnimalName 
                    in Animal.List
                ]
            ]

        Animal(
            SelectedSpecie,
            random.choice(AnimalsData[SelectedSpecie]["colors"]),
            random.choice(SelectedName),
            AnimalsData[SelectedSpecie]["gender"],
            random.randint(
                AnimalsData[SelectedSpecie]["minSpeed"], 
                AnimalsData[SelectedSpecie]["maxSpeed"])
            )

    # print list
    ToSort = ''

    while ToSort not in ('y', 'n'):
        ToSort = input("Veux tu afficher les animaux triés par expèces (y,n): ").lower()

    
    Animal.Print(ToSort)


def openFile(name: str) -> dict[dict]:
    """
    Functions wich retrurns a dict of dict containing data for each animal
    """
    try:
        with open(f"{name}.json", encoding="utf-8") as file:
            AnimalsData = json.load(file)
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé !")
        exit()

    return AnimalsData


def FaireViellir() -> None:
    """
        Demander à l'utilisateur 
        - de quelle espèce et/ou de quelle couleur (parmi les espèces et couleurs possibles)
            il souhaite faire vieillir les animaux
        - de combien d'années    
    """
  
    NbYears = None
    try:

        while(NbYears is None or NbYears > 0):
            print("\nFaire vieillir...")
            NbYears = int(input("De combien d'années : "))

            if NbYears > 0:
                Specie = None
                while(Specie != "" and Specie not in Animal.Species):
                    print(f"Espèces possibles : {', '.join(Animal.Species)}")
                    Specie = input("De quelle espèce : ")
                Color = None
                while(Color != "" and Color not in Animal.Colors):
                    print(f"Couleurs possibles : {', '.join(Animal.Colors)}")
                    Color = input("De quelle couleur : ")

                # méthode basique
                Start1 = time.time()
                for MyAnimal in Animal.List:
                    if ((Specie == "" or MyAnimal.Species == Specie)
                        and (Color == "" or MyAnimal.Color == Color)):
                        MyAnimal.Vieillir(NbYears)
                Duration1 = time.time() - Start1
                print(f"Durée Boucle For : {round(Duration1, 4)}")

                # méthode avec filter    
                # Start2 = time.time()                                           
                # AnimalsToGrowOlder = list(
                #     filter(
                #         lambda AnimalIterated:
                #         (AnimalIterated.Species.lower() == Specie.lower() or Specie =="")
                #         and 
                #         (AnimalIterated.Color.lower() == Color.lower() or Color==""),
                #         Animal.List
                #         )
                #     )
                # for AnimalIterated in AnimalsToGrowOlder:
                #     AnimalIterated.Vieillir(NbYears)
                # Duration2 = time.time() - Start2
                # print(f"Durée Filter : {round(Duration2, 4)}")
                
                # méthode avec compréhension de liste   
                # Start3 = time.time()                                             
                # [TheAnimal.Vieillir(NbYears) for TheAnimal in Animal.List if (
                #     (Specie == "" or TheAnimal.Species == Specie) and 
                #     (Color == "" or TheAnimal.Color == Color)
                #     )]
                # Duration3 = time.time() - Start3                
                # print(f"Durée Compréhension : {round(Duration3, 4)}")


    except ValueError:
        pass

    # affiche la liste
    Animal.Print()



# Code starts here
if __name__ == "__main__":
    Main()
