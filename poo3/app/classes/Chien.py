from .Animal import Animal

class Chien(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        
    def make_sound(self) -> str:
        return "Woof!"
        
    def obeis(self, ordre: str) -> str:
        return f"{self.name} fait {ordre}."