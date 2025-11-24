"""Module définissant la classe MagicienBlanc."""

import random
from .Personnage import Personnage
from .Frappe import Frappe


class MagicienBlanc(Personnage):
    """Représente un Magicien Blanc inspiré de Gandalf."""

    def __init__(self) -> None:
        """Initialise le Magicien Blanc avec ses frappes spécifiques."""
        frappes = [
            Frappe("⚡ Éclair lumineux", force=15, experience_gain=5),
            Frappe("🔥 Flamme de l'Anor", force=25, experience_gain=10),
            Frappe("✨ Sort de bannissement", force=30, experience_gain=15),
            Frappe("💫 Lumière purificatrice", force=20, experience_gain=8),
        ]
        super().__init__("✨ Magicien Blanc", frappes)

    def frappe(self, cible: Personnage, force_frappe: Frappe = None) -> None:
        """Effectue une frappe magique sur la cible.

        Args:
            cible: Le personnage cible de l'attaque
            force_frappe: La frappe utilisée (choisie aléatoirement si None)
        """
        if force_frappe is None:
            force_frappe = self._choisir_frappe_aleatoire()

        print(f"\n{self.nom} utilise {force_frappe.nom} !")

        if cible.esquive():
            print(f"💨 {cible.nom} esquive l'attaque avec agilité !")
        else:
            cible.recoit_degat(self, force_frappe.force)
            self._experience += force_frappe.experience_gain
            print(f"💥 Coup porté ! +{force_frappe.experience_gain} XP")

    def esquive(self) -> bool:
        """Tente d'esquiver une attaque avec 22% de chance.

        Returns:
            True si l'esquive réussit, False sinon
        """
        return random.random() < 0.22

    def recoit_degat(self, adversaire: Personnage, force_frappe: int) -> None:
        """Reçoit des dégâts d'un adversaire.

        Args:
            adversaire: Le personnage qui attaque
            force_frappe: La force de la frappe reçue
        """
        degats_totaux = force_frappe + adversaire.experience
        self._degats += degats_totaux
        print(f"🩸 {self.nom} subit {degats_totaux} points de dégâts !")
        print(f"❤️  Vie restante: {self.vie_restante}/{self.vie} | ⭐ XP: {self.experience}")
