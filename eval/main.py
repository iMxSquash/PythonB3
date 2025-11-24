"""
Programme principal de simulation de combat entre le Magicien Blanc et le Roi Sorcier.

Ce module orchestre le combat entre deux personnages issus de l'univers du Seigneur
des Anneaux. Le combat se déroule automatiquement jusqu'à la victoire de l'un des
combattants.
"""

import time
import random
from app.classes.MagicienBlanc import MagicienBlanc
from app.classes.RoiSorcier import RoiSorcier
from app.classes.Personnage import Personnage
from app.utils.combat_utils import (
    afficher_titre,
    afficher_intro,
    afficher_separateur,
    annoncer_vainqueur,
)


def executer_tour(attaquant: Personnage, defenseur: Personnage, numero_tour: int) -> None:
    """Exécute un tour de combat.

    Args:
        attaquant: Le personnage qui attaque ce tour
        defenseur: Le personnage qui défend ce tour
        numero_tour: Le numéro du tour actuel
    """
    print(f"🎯 Tour {numero_tour} - {attaquant.nom} attaque !")
    time.sleep(0.5)
    attaquant.frappe(defenseur)
    time.sleep(0.5)


def determiner_ordre_combat(
    joueur1: Personnage, joueur2: Personnage
) -> tuple[Personnage, Personnage]:
    """Détermine l'ordre de combat en fonction de la propriété de classe 'tour'.

    Args:
        joueur1: Le premier joueur (Magicien Blanc)
        joueur2: Le second joueur (Roi Sorcier)

    Returns:
        Tuple contenant l'attaquant et le défenseur pour ce tour
    """
    if Personnage.tour == "joueur1":
        Personnage.tour = "joueur2"
        return joueur1, joueur2
    else:
        Personnage.tour = "joueur1"
        return joueur2, joueur1


def lancer_combat() -> None:
    """Lance et gère le déroulement complet du combat."""
    # Initialisation des combattants
    magicien = MagicienBlanc()
    roi_sorcier = RoiSorcier()

    # Détermination aléatoire du premier joueur
    Personnage.tour = random.choice(["joueur1", "joueur2"])
    premier = "✨ Magicien Blanc" if Personnage.tour == "joueur1" else "👑 Roi Sorcier"
    
    # Affichage du titre et de l'introduction
    afficher_titre()
    afficher_intro(magicien, roi_sorcier)
    print(f"🎲 {premier} commence le combat !\n")
    time.sleep(1)

    # Boucle principale du combat
    numero_tour = 1

    while magicien.est_vivant and roi_sorcier.est_vivant:
        # Déterminer qui attaque ce tour
        attaquant, defenseur = determiner_ordre_combat(magicien, roi_sorcier)

        # Exécuter le tour
        executer_tour(attaquant, defenseur, numero_tour)

        # Pause entre les tours
        afficher_separateur()

        numero_tour += 1

        # Sécurité : limite à 100 tours pour éviter une boucle infinie
        if numero_tour > 100:
            print("⚠️  Combat trop long, match nul !")
            return

    # Annoncer le vainqueur
    if magicien.est_vivant:
        annoncer_vainqueur(magicien, roi_sorcier)
    else:
        annoncer_vainqueur(roi_sorcier, magicien)


if __name__ == "__main__":
    lancer_combat()
