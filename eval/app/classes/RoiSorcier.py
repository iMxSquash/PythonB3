"""Module définissant la classe RoiSorcier."""

import random
from .Personnage import Personnage
from .Frappe import Frappe


class RoiSorcier(Personnage):
    """Représente le Roi Sorcier d'Angmar, seigneur des Nazgûl."""

    def __init__(self) -> None:
        """Initialise le Roi Sorcier avec ses frappes sombres."""
        frappes = [
            Frappe("⚔️  Lame maudite", force=19, experience_gain=6),
            Frappe("🌑 Souffle de terreur", force=23, experience_gain=9),
            Frappe("💀 Cri spectral", force=30, experience_gain=13),
            Frappe("🗡️  Frappe des ténèbres", force=21, experience_gain=7),
        ]
        super().__init__("👑 Roi Sorcier", frappes)

    def frappe(self, cible: Personnage, force_frappe: Frappe = None) -> None:
        """Effectue une frappe ténébreuse sur la cible.

        Args:
            cible: Le personnage cible de l'attaque
            force_frappe: La frappe utilisée (choisie aléatoirement si None)
        """
        if force_frappe is None:
            force_frappe = self._choisir_frappe_aleatoire()

        print(f"\n{self.nom} déchaîne {force_frappe.nom} !")

        if cible.esquive():
            print(f"💨 {cible.nom} évite l'attaque de justesse !")
        else:
            cible.recoit_degat(self, force_frappe.force)
            self._experience += force_frappe.experience_gain
            print(f"💥 Attaque réussie ! +{force_frappe.experience_gain} XP")

    def esquive(self) -> bool:
        """Tente d'esquiver une attaque avec 20% de chance.

        Returns:
            True si l'esquive réussit, False sinon
        """
        return random.random() < 0.20

    def recoit_degat(self, adversaire: Personnage, force_frappe: int) -> None:
        """Reçoit des dégâts d'un adversaire.

        Args:
            adversaire: Le personnage qui attaque
            force_frappe: La force de la frappe reçue
        """
        degats_totaux = force_frappe + adversaire.experience
        self._degats += degats_totaux
        print(f"🩸 {self.nom} encaisse {degats_totaux} points de dégâts !")
        print(f"❤️  Vie restante: {self.vie_restante}/{self.vie} | ⭐ XP: {self.experience}")
