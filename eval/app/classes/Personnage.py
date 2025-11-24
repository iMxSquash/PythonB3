"""Module définissant la classe abstraite Personnage."""

from abc import ABC, abstractmethod
from typing import List
import random
from .Frappe import Frappe


class Personnage(ABC):
    """Classe abstraite représentant un personnage de combat."""

    tour: str = "joueur1"

    def __init__(self, nom: str, frappes: List[Frappe]) -> None:
        """Initialise un personnage.

        Args:
            nom: Le nom du personnage
            frappes: Liste des frappes disponibles pour le personnage
        """
        self._nom = nom
        self._vie = 100
        self._frappes = frappes
        self._experience = 0
        self._degats = 0

    # Getters et setters avec validation
    @property
    def nom(self) -> str:
        """Retourne le nom du personnage."""
        return self._nom

    @nom.setter
    def nom(self, value: str) -> None:
        """Définit le nom du personnage."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Le nom doit être une chaîne non vide")
        self._nom = value

    @property
    def vie(self) -> int:
        """Retourne les points de vie du personnage."""
        return self._vie

    @vie.setter
    def vie(self, value: int) -> None:
        """Définit les points de vie du personnage."""
        if not isinstance(value, int) or value < 0:
            raise ValueError("La vie doit être un entier positif")
        self._vie = value

    @property
    def frappes(self) -> List[Frappe]:
        """Retourne la liste des frappes disponibles."""
        return self._frappes

    @frappes.setter
    def frappes(self, value: List[Frappe]) -> None:
        """Définit la liste des frappes."""
        if not isinstance(value, list) or not all(isinstance(f, Frappe) for f in value):
            raise ValueError("Les frappes doivent être une liste d'objets Frappe")
        self._frappes = value

    @property
    def experience(self) -> int:
        """Retourne l'expérience du personnage."""
        return self._experience

    @experience.setter
    def experience(self, value: int) -> None:
        """Définit l'expérience du personnage."""
        if not isinstance(value, int) or value < 0:
            raise ValueError("L'expérience doit être un entier positif")
        self._experience = value

    @property
    def degats(self) -> int:
        """Retourne les dégâts subis par le personnage."""
        return self._degats

    @degats.setter
    def degats(self, value: int) -> None:
        """Définit les dégâts subis."""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Les dégâts doivent être un entier positif")
        self._degats = value

    @property
    def vie_restante(self) -> int:
        """Calcule et retourne la vie restante du personnage."""
        return max(0, self._vie - self._degats)

    @property
    def est_vivant(self) -> bool:
        """Vérifie si le personnage est encore en vie."""
        return self.vie_restante > 0

    @abstractmethod
    def frappe(self, cible: "Personnage", force_frappe: Frappe) -> None:
        """Effectue une frappe sur la cible.

        Args:
            cible: Le personnage cible de l'attaque
            force_frappe: La frappe utilisée
        """
        pass

    @abstractmethod
    def esquive(self) -> bool:
        """Tente d'esquiver une attaque.

        Returns:
            True si l'esquive réussit, False sinon
        """
        pass

    @abstractmethod
    def recoit_degat(self, adversaire: "Personnage", force_frappe: int) -> None:
        """Reçoit des dégâts d'un adversaire.

        Args:
            adversaire: Le personnage qui attaque
            force_frappe: La force de la frappe reçue
        """
        pass

    def _choisir_frappe_aleatoire(self) -> Frappe:
        """Choisit une frappe aléatoire parmi celles disponibles.

        Returns:
            Une frappe choisie aléatoirement
        """
        return random.choice(self._frappes)
