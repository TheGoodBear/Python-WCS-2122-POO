from enum import Enum

# Civilite = ("Mr", "Mme", "Mle", "")

# MaCivilite = Civilite[0]
# MaCivilite2 = Civilite[2]

# print(MaCivilite)
# print(MaCivilite2)

class Civility(Enum):
    Mr = "Mr"
    Mme = "Mme"
    Mle = "Mle"
    Undefined = ""


class SeverityLevel(Enum):
    Info = {"name" : "Information", "level" : 1}
    Warning = {"name" : "Alerte", "level" : 3}
    Critical = {"name" : "Erreur critique", "level" : 5}
def PrintError(Message, Severity = SeverityLevel.Warning):
    """
    """
    
    print(f"({Severity.value['level']}) {Severity.value['name']} : {Message}")


if __name__ == "__main__":      

    # MyCivility  = Civility.Mr
    # print(MyCivility.value)

    PrintError("Ceci est une simple alerte")
    PrintError("Message d'informaton", SeverityLevel.Info)
    PrintError("Attention, ça va pêter !!!", SeverityLevel.Critical)
    