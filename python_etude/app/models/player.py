# Classe représentant un joueur

from random import randint

class Player:
    def __init__(self, name: str, score: int = 0):
        self.name = name
        self.score = score

    def update_score(self, points: int) -> None:
        self.score += points

    def get_score(self) -> int:
        return self.score
    
    def tirage(self) -> int:
        return randint(2, 12)

    def __str__(self) -> str:
        return f"Player(name={self.name}, score={self.score})"