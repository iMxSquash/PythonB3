from .Animal import Animal

class Chien(Animal):
    """
    Classe représentant un chien.
    Args:
        Animal (Animal): Classe de base Animal.
    """
    def parler(self) -> str:
        return "Woof Woof!"