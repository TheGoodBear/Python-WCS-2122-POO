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

    # Exercice 1 + 3
    FaireNaitre()

    # Exercice 2
    # FaireViellir()

    # end
    print("\nAu revoir")


def FaireNaitre() -> None:
    """
        Demander à l'utilisateur 
        combien d'animaux doivent naitre    
    """
    
    # get animal data from file
    AnimalsData = ReadFromFile('./Exercice 3/data')

    # get number of animals to create
    NumberOfAnimals = 0

    # Repeat while the input is not a number
    # or is not between 2 and 10
    while NumberOfAnimals < 2 or NumberOfAnimals > 10:
        try:
            NumberOfAnimals = int(input("Combien d'animaux dois-je faire naitre ? (entre 2 - 10) : "))
        except ValueError:
            print("Il faut saisir un nombre entre 2 et 10")

    # Get all the keys from the AnimalsData dict
    Species = list(AnimalsData)
    
    # create appropriate number of animals
    for Number in range(NumberOfAnimals):
        # get a random species
        SelectedSpecies = random.choice(Species)
        
        # get a random name from possible names in selected species
        # and be sure name is not already taken
        SelectedName = [
            Name 
            for Name 
            in AnimalsData[SelectedSpecies]["names"] 
            if not Name in 
                [
                    AnimalName.Name
                    for AnimalName 
                    in Animal.List
                ]
            ]

        # create a new animal with random properties
        Animal(
            SelectedSpecies,
            random.choice(AnimalsData[SelectedSpecies]["colors"]),
            random.choice(SelectedName),
            AnimalsData[SelectedSpecies]["gender"],
            random.randint(
                AnimalsData[SelectedSpecies]["minSpeed"], 
                AnimalsData[SelectedSpecies]["maxSpeed"])
            )

    # print list, sorted or not
    SortBy = None
    PossibleFields = ["Name", "Species", "Color", "MaxSpeed"]

    # Ask to the player if he want to sort the output
    while SortBy not in PossibleFields and SortBy != '':
        print("Par quoi veux-tu trier la liste (vide pour ne pas trier): ")
        print(", ".join(PossibleFields))
        SortBy = input("")

    # print list
    Animal.Print(SortBy)


def ReadFromFile(name: str) -> dict[dict]:
    """
        Returns a dict of dict containing data for each animal
        loaded from a json file
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
                # Start1 = time.time()
                for MyAnimal in Animal.List:
                    if ((Specie == "" or MyAnimal.Species == Specie)
                        and (Color == "" or MyAnimal.Color == Color)):
                        MyAnimal.Vieillir(NbYears)
                # Duration1 = time.time() - Start1
                # print(f"Durée Boucle For : {round(Duration1, 4)}")

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
