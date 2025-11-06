# Classe représentant une bataille entre deux joueurs
from app.models.player import Player

class Battle:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def start_battle(self) -> None:
        tours = 10
        
        while tours > 0:
            score1 = self.player1.tirage()
            score2 = self.player2.tirage()
            
            if score1 > score2:
                self.player1.update_score(1)
            elif score2 > score1:
                self.player2.update_score(1)
                
            print(f"Tour {11 - tours}: {self.player1.name} a tiré {score1}, {self.player2.name} a tiré {score2}")
            print(self.player1)
            print(self.player2)
                
            tours -= 1
            
        p1_score = self.player1.get_score()
        p2_score = self.player2.get_score()
        
        print(f"Scores: {self.player1.name} {p1_score} - {self.player2.name} {p2_score}")
        
        if p1_score > p2_score:
            print(f"{self.player1.name} gagne la bataille!")
        elif p2_score > p1_score:
            print(f"{self.player2.name} gagne la bataille!")
        else:
            print("La bataille se termine par une égalité!")

    def __str__(self) -> str:
        return f"Battle entre {self.player1.name} et {self.player2.name}"