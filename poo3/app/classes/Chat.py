from .Animal import Animal

class Chat(Animal):
    def __init__(self, name: str):
        super().__init__(name)
        
    def make_sound(self) -> str:
        return "Meow!"