"""Module contenant les fonctions utilitaires pour le combat."""

import time
from typing import Tuple
from app.classes.Personnage import Personnage


def afficher_titre() -> None:
    """Affiche le titre du jeu avec un style épique."""
    print("\n" + "=" * 60)
    print("⚔️  " + " " * 10 + "COMBAT ÉPIQUE EN TERRE DU MILIEU" + " " * 10 + "⚔️")
    print("=" * 60)
    print()


def afficher_intro(joueur1: Personnage, joueur2: Personnage) -> None:
    """Affiche l'introduction du combat.

    Args:
        joueur1: Le premier combattant
        joueur2: Le second combattant
    """
    print(f"🎭 {joueur1.nom} VS {joueur2.nom}")
    print(f"\n{'─' * 60}\n")
    time.sleep(1)


def afficher_separateur() -> None:
    """Affiche un séparateur visuel."""
    print(f"\n{'─' * 60}\n")
    time.sleep(0.5)


def annoncer_vainqueur(vainqueur: Personnage, perdant: Personnage) -> None:
    """Annonce le vainqueur du combat.

    Args:
        vainqueur: Le personnage victorieux
        perdant: Le personnage vaincu
    """
    print("\n" + "=" * 60)
    print("🏆" + " " * 20 + "FIN DU COMBAT" + " " * 20 + "🏆")
    print("=" * 60)
    print(f"\n💀 {perdant.nom} est tombé au combat...")
    print(f"🎉 {vainqueur.nom} remporte la victoire !")
    print(f"⭐ XP finale du vainqueur: {vainqueur.experience}")
    print(f"❤️  Vie restante: {vainqueur.vie_restante}/{vainqueur.vie}")
    print("\n" + "=" * 60 + "\n")
