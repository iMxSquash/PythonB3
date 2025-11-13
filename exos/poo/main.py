from app.classes.Personne import Personne

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