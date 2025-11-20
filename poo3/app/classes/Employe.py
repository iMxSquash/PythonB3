from abc import ABC, abstractmethod

class Employe(ABC):
    @property
    @abstractmethod
    def salaire(self) -> float:
        """Retourne le salaire de l'employé."""
        pass
    
    @salaire.setter
    @abstractmethod
    def salaire(self, value: float):
        """Définit le salaire de l'employé."""
        pass