from app.classes.Voiture import Voiture
from app.classes.Rectangle import Rectangle
from app.classes.Chien import Chien
from app.classes.Chat import Chat
from app.classes.Ingenieur import Ingenieur
from app.classes.IParle import IParle
from app.classes.FileRepo import FileRepo
from app.classes.InMemRepo import InMemRepo
from app.classes.UserRepository import UserRepository
from app.classes.PaymentMethod import PaymentMethod
from app.classes.Paypal import Paypal
from app.classes.CreditCard import CreditCard


if __name__ == "__main__":
    voiture1 = Voiture("Toyota", "Corolla")
    voiture2 = Voiture("Honda", "Civic")

    print(f"Voiture 1: {voiture1.marque} {voiture1.modele}")
    print(f"Voiture 2: {voiture2.marque} {voiture2.modele}")
    
    voiture1.marque = "Ford"
    voiture1.modele = "Mustang"
    voiture2.marque = "Chevrolet"
    voiture2.modele = "Camaro"

    print(f"Voiture 1 modifiée: {voiture1.marque} {voiture1.modele}")
    print(f"Voiture 2 modifiée: {voiture2.marque} {voiture2.modele}")
    
    rectangle1 = Rectangle(5, 10)
    print(f"Rectangle 1 - Longueur: {rectangle1.length}, Largeur: {rectangle1.width}, Aire: {rectangle1.area()}, Périmètre: {rectangle1.perimeter()}")
    print(rectangle1.salutation())
    
    chien = Chien("Rex")
    print(f"Chien: {chien.name}, Son: {chien.make_sound()}")
    print(chien.obeis("assis"))
    
    chat = Chat("Kitty")
    print(f"Chat: {chat.name}, Son: {chat.make_sound()}")
    
    ingenieur = Ingenieur(50000)
    print(f"Ingénieur Salaire: {ingenieur.salaire}")
    ingenieur.salaire = 60000
    print(f"Ingénieur Salaire modifié: {ingenieur.salaire}")
    
    from app.classes.Personne import Personne
    from app.classes.Canard import Canard
    
    def faire_parler(entite: object):
        entite.parler()
        
    personne = Personne()
    canard = Canard()
    faire_parler(personne)
    faire_parler(canard)
    
    def faire_parler_iparle(entite: IParle) -> None:
        entite.parler()
        
    faire_parler_iparle(personne)
    faire_parler_iparle(canard)
        
    def ajouter_des_users(repo: UserRepository) -> None:
        while True:
            response = input("Voulez-vous ajouter un utilisateur? (o/n): ")
            if response.lower() != 'o':
                break
            name = input("Entrez le nom de l'utilisateur: ")
            repo.save({"name": name})
    
    def afficher_users(repo: UserRepository) -> None:
        users = repo.find_all()
        print("Utilisateurs enregistrés:")
        for user in users:
            print(user)
            
            
    repo1 = FileRepo("users.json")
    repo2 = InMemRepo()
    # print("=== Utilisation de FileRepo ===")
    # ajouter_des_users(repo1)
    # afficher_users(repo1)
    
    # print("=== Utilisation de InMemRepo ===")
    # ajouter_des_users(repo2)
    # afficher_users(repo2)
    
    def process_payment(method: PaymentMethod, amount: float) -> None:
        method.pay(amount)
        
    process_payment(Paypal(), 50)
    process_payment(CreditCard(), 30)