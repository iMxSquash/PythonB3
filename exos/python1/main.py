"""
Programme principal de gestion de boutique - Exercice Python 1

Ce programme simule la gestion simple d'une boutique en utilisant
une architecture propre et modulaire.
"""

from app.models import Boutique
from app.services import BoutiqueService
from app.utils import afficher_titre, formater_prix, afficher_variable_avec_type


def main() -> None:
    """
    Fonction principale du programme.
    """
    # Affichage du titre
    afficher_titre("GESTION DE BOUTIQUE - EXERCICE 1")
    
    # I. Créer et typer correctement les variables
    print("I. Création des variables\n")
    
    nom_boutique: str = "ChossettZ"
    produit: str = "chaussettes"
    prix_unitaire: float = 5.99
    quantite_stock: int = 20
    tva: float = 0.20
    compte_client: float = 100.0
    compte_boutique: float = 0.0
    
    # Affichage des variables créées
    print(f"✓ nom_boutique: {nom_boutique} (type: {type(nom_boutique).__name__})")
    print(f"✓ produit: {produit} (type: {type(produit).__name__})")
    print(f"✓ prix_unitaire: {formater_prix(prix_unitaire)} (type: {type(prix_unitaire).__name__})")
    print(f"✓ quantite_stock: {quantite_stock} (type: {type(quantite_stock).__name__})")
    print(f"✓ tva: {tva} (type: {type(tva).__name__})")
    print(f"✓ compte_client: {formater_prix(compte_client)} (type: {type(compte_client).__name__})")
    print(f"✓ compte_boutique: {formater_prix(compte_boutique)} (type: {type(compte_boutique).__name__})")
    
    # II. Afficher une phrase complète utilisant TOUTES les variables
    print("\n" + "="*50)
    print("II. Phrase complète avec toutes les variables")
    print("="*50 + "\n")
    
    # Création de l'instance de boutique
    boutique = Boutique(
        nom_boutique=nom_boutique,
        produit=produit,
        prix_unitaire=prix_unitaire,
        quantite_stock=quantite_stock,
        tva=tva,
        compte_client=compte_client,
        compte_boutique=compte_boutique
    )
    
    # Affichage via print()
    print(boutique)
    
    # Création du service pour gérer la logique métier
    service = BoutiqueService(boutique)
    
    # III. Effectuer les opérations arithmétiques
    print("\n" + "="*50)
    print("III. Opérations arithmétiques")
    print("="*50 + "\n")
    
    # a. Calculer le prix hors taxe 
    prix_ht: float = boutique.prix_unitaire
    
    # b. Calculer le prix TTC
    prix_ttc: float = service.calculer_prix_ttc()
    
    # c. Afficher les deux résultats arrondis à 2 décimales
    print(f"a. Prix Hors Taxe (HT): {formater_prix(prix_ht)}")
    print(f"b. Prix TTC (TVA {boutique.tva * 100}%): {formater_prix(prix_ttc)}")
    print(f"\nCalcul détaillé:")
    print(f"   Prix TTC = Prix HT × (1 + TVA)")
    print(f"   Prix TTC = {formater_prix(prix_ht)} × (1 + {boutique.tva})")
    print(f"   Prix TTC = {formater_prix(prix_ht)} × {1 + boutique.tva}")
    print(f"   Prix TTC = {formater_prix(prix_ttc)}")
    
    # IV & V. Demander et valider la quantité d'achat
    print("\n" + "="*50)
    print("IV. Achat de chaussettes")
    print("="*50 + "\n")
    
    # Demander la quantité avec la fonction input
    quantite_achat_str: str = input(
        f"Combien de paires de {boutique.produit} voulez-vous acheter ? "
    )
    
    # V. Validation complète via le service
    est_valide, quantite_achat, message_erreur = service.valider_quantite_achat(
        quantite_achat_str
    )
    
    if not est_valide:
        # Afficher l'erreur et terminer le programme
        print(f"\n❌ ERREUR: {message_erreur}")
        print("Le programme se termine.")
        return
    
    # Si la validation réussit
    print(f"\n✓ Validation réussie!")
    print(f"✓ Quantité commandée: {quantite_achat} paire(s) de {boutique.produit}")
    
    # VI. Calculer et stocker toutes les informations de l'achat
    print("\n" + "="*50)
    print("VI. Traitement de la transaction")
    print("="*50 + "\n")
    
    print("⏳ Traitement en cours...")
    
    # Effectuer l'achat complet (calculs + mise à jour)
    transaction = service.effectuer_achat(quantite_achat)
    
    # Afficher le récapitulatif détaillé
    service.afficher_recapitulatif_achat(transaction)
    
    # VII. Vérifier si le stock est inférieur à 10
    print("="*50)
    print("VII. Vérification du stock")
    print("="*50 + "\n")
    
    service.verifier_stock_faible(seuil=10)
    
    # IX. Convertir le prix TTC de la vente en chaîne et ajouter le symbole €
    print("="*50)
    print("IX. Conversion du prix TTC en chaîne")
    print("="*50 + "\n")
    
    # Récupérer le montant TTC de la transaction
    montant_ttc_vente: float = transaction['montant_ttc']
    
    # Convertir en chaîne avec symbole € (utilise formater_prix de utils)
    montant_ttc_str: str = formater_prix(montant_ttc_vente, devise="€")
    
    # Afficher le résultat
    print(f"Montant TTC de la vente (float): {montant_ttc_vente}")
    print(f"Type: {type(montant_ttc_vente).__name__}")
    print(f"\nMontant TTC de la vente (string): {montant_ttc_str}")
    print(f"Type: {type(montant_ttc_str).__name__}")
    print(f"\n✓ Le symbole '€' a été ajouté dynamiquement via la fonction formater_prix().")
    
    # X. Afficher la facture
    print("\n" + "="*50)
    print("X. Facture de la transaction")
    print("="*50)
    
    service.afficher_facture(quantite_achat)
    
    # XI. Afficher le type de chaque variable
    print("\n" + "="*50)
    print("XI. Type de toutes les variables")
    print("="*50 + "\n")
    
    print("Variables initiales:")
    afficher_variable_avec_type("nom_boutique", nom_boutique)
    afficher_variable_avec_type("produit", produit)
    afficher_variable_avec_type("prix_unitaire", prix_unitaire)
    afficher_variable_avec_type("quantite_stock", quantite_stock)
    afficher_variable_avec_type("tva", tva)
    afficher_variable_avec_type("compte_client", compte_client)
    afficher_variable_avec_type("compte_boutique", compte_boutique)
    
    print("\nVariables calculées:")
    afficher_variable_avec_type("prix_ht", prix_ht)
    afficher_variable_avec_type("prix_ttc", prix_ttc)
    
    print("\nVariables de saisie:")
    afficher_variable_avec_type("quantite_achat_str", quantite_achat_str)
    afficher_variable_avec_type("quantite_achat", quantite_achat)
    
    print("\nVariables de transaction:")
    afficher_variable_avec_type("transaction", transaction)
    
    print("\nVariables de conversion:")
    afficher_variable_avec_type("montant_ttc_vente", montant_ttc_vente)
    afficher_variable_avec_type("montant_ttc_str", montant_ttc_str)
    
    print("\nObjets:")
    afficher_variable_avec_type("boutique", boutique)
    afficher_variable_avec_type("service", service)


if __name__ == "__main__":
    main()
