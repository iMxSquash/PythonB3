# app/utils.py

# function to greet a person by name
def saluer(nom: str) -> None:
    print(f"Bonjour, {nom} !") 

def add(a: int, b: int, *args: int) -> int:
    """Retourne la somme de deux entiers."""
    return a + b

def divide(a: float, b: float = 1.0) -> float:
    """Retourne le resultat de la division de a par b."""
    if b == 0:
        raise ValueError("Le diviseur ne peut pas etre zero.")
    return a / b

def addition_multiple(*param: int) -> int:
    """Retourne la somme de plusieurs entiers donnes en arguments."""
    print(f"Parametres recus: {param}")
    print(f"Type de parametres: {type(param)}")
    total = 0
    for nbr in param:
        total += nbr
    return total

def afficher_info(**info: str) -> None:
    """Affiche les informations fournies en arguments nommes."""
    for cle, valeur in info.items():
        print(f"{cle}: {valeur}")