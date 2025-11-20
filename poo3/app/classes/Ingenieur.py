from .Employe import Employe

class Ingenieur(Employe):
    def __init__(self, salaire: float):
        self._salaire = salaire

    @property
    def salaire(self) -> float:
        """Retourne le salaire de l'ingénieur."""
        return self._salaire
    
    @salaire.setter
    def salaire(self, value: float):
        """Définit le salaire de l'ingénieur."""
        if value < 0:
            raise ValueError("Le salaire ne peut pas être négatif.")
        self._salaire = value