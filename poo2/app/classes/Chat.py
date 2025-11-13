from .Animal import Animal

class Chat(Animal):
    """Classe représentant un chat.

    Args:
        Animal (Animal): Classe de base Animal.
    """
    def parler(self) -> str:
        """Fait parler le chat.

        Returns:
            str: Le son émis par le chat.
        """
        return "Meow Meow!"