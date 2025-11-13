from app.classes.Personne import Personne
from app.classes.CompteBancaire import CompteBancaire

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