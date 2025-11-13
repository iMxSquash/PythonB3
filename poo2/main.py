from app.classes.Voiture import Voiture
from app.utils import utils
from app.classes.Chien import Chien
from app.classes.Chat import Chat


if __name__ == "__main__":
    voiture = Voiture("fiat", "MULTIPLA", 2020, 1000)
    
    voiture.accelerer(1000)
    
    utils.show(voiture, "ma_voiture")
    print(voiture.afficher_details())
    
    chien = Chien()
    chat = Chat()
    print()
    utils.faire_parler(chien)
    utils.faire_parler(chat)
    