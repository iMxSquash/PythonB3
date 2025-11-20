from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name: str):
        self.__name = name
    
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name
    
    @abstractmethod
    def make_sound(self):
        """Produce the sound made by the animal. """
        pass
    
    