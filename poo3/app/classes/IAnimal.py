from abc import ABC, abstractmethod

class IAnimal(ABC):
    @abstractmethod
    def parler(self) -> str:
        """Fait parler l'animal."""
        pass
    
    @abstractmethod
    def se_deplacer(self) -> str:
        """Décrit le déplacement de l'animal."""
        pass