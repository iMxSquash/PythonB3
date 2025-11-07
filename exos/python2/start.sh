#!/bin/bash
# Script pour démarrer rapidement le projet avec l'environnement virtuel

echo "🚀 Démarrage du projet Python 2 - Pierre Feuille Ciseaux"
echo ""

# Vérifier si .venv existe
if [ ! -d ".venv" ]; then
    echo "⚠️  L'environnement virtuel n'existe pas."
    echo "📦 Création de l'environnement virtuel..."
    python3 -m venv .venv
    echo "✅ Environnement virtuel créé !"
fi

# Activer l'environnement virtuel
echo "🔧 Activation de l'environnement virtuel..."
source .venv/bin/activate

echo "✅ Environnement virtuel activé !"
echo ""
echo "📝 Commandes disponibles :"
echo "   • python3 main.py          : Lancer le programme"
echo "   • deactivate               : Quitter l'environnement virtuel"
echo ""
