from abc import ABC, abstractmethod

class FormGeom(ABC):
    @abstractmethod
    def area(self):
        """Calculate the area of the geometric form."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the geometric form."""
        pass
    
    def salutation(self) -> str:
        return "Bonjour, merci d'utiliser notre application de géométrie."