from app.classes.Personne import Personne
from app.classes.CompteBancaire import CompteBancaire
from app.classes.Rectangle import Rectangle

if __name__ == "__main__":
    personne = Personne("Alice Dupont", 28)
    
    print(f"Nom: {personne.nom}")
    print(f"Âge: {personne.age}")
    print(f"Numéro: {personne.numero_securite}")
    
    print(f"Numéro name mangling: {personne._Personne__numero_securite}")
    
    personne.nom = "Bob Martin"
    personne.age = 35
    personne.numero_securite = "555-12-3456"
    
    personne.afficher_info()
    
    compte = CompteBancaire(personne, 500)
    
    compte.deposer(100)
    
    compte.afficher_solde()
    compte._afficher_solde()
    
    compte._CompteBancaire__enregistrer_transaction("Transaction via name mangling")
    
    compte.afficher_solde()
    
    rectangle = Rectangle(5, 3)
    
    print(f"Largeur: {rectangle.largeur}")
    print(f"Hauteur: {rectangle.hauteur}")
    print(f"Aire: {rectangle.aire}")
    
    rectangle.largeur = 10
    rectangle.hauteur = 7
    
    print(f"Nouvelle largeur: {rectangle.largeur}")
    print(f"Nouvelle hauteur: {rectangle.hauteur}")
    print(f"Nouvelle aire: {rectangle.aire}")
    
    print("\n3. Tentative d'affecter -3 à la largeur")
    try:
        rectangle.largeur = -3
    except ValueError as e:
        print(f"❌ Erreur: {e}")
    
    print("\n" + "=" * 60)
