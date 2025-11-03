"""
Fonctions utilitaires pour l'application.
"""


def afficher_titre(titre: str, largeur: int = 50) -> None:
    """
    Affiche un titre formaté.
    
    Args:
        titre: Le titre à afficher
        largeur: Largeur totale de l'affichage (par défaut: 50)
    """
    print(f"\n{'='*largeur}")
    print(f"{titre.center(largeur)}")
    print(f"{'='*largeur}\n")


def formater_prix(prix: float, devise: str = "€") -> str:
    """
    Formate un prix avec deux décimales et le symbole de devise.
    
    Args:
        prix: Le prix à formater
        devise: Le symbole de la devise (par défaut: "€")
    
    Returns:
        str: Prix formaté
    """
    return f"{prix:.2f}{devise}"


def afficher_variable_avec_type(nom: str, valeur, prefixe: str = "  • ") -> None:
    """
    Affiche une variable avec sa valeur et son type.
    
    Args:
        nom: Nom de la variable
        valeur: Valeur de la variable
        prefixe: Préfixe à afficher (par défaut: "  • ")
    """
    # Formater la valeur selon son type
    if isinstance(valeur, str):
        valeur_affichee = f"'{valeur}'"
    elif isinstance(valeur, dict):
        valeur_affichee = "{...}"
    elif isinstance(valeur, (int, float)):
        valeur_affichee = str(valeur)
    else:
        valeur_affichee = f"<{type(valeur).__name__} instance>"
    
    print(f"{prefixe}{nom} = {valeur_affichee} → type: {type(valeur).__name__}")
