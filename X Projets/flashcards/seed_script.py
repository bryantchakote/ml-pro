# %%
# Ce script permet de créer des données de test pour la base de données
from flashcards import *
import json
import sqlite3
import random
from datetime import datetime, timedelta


# %%
# Suppression des données
# empty_tables()


# %%
# Initialisation de la base de données (+ insertion des thèmes)
init_db()


# %%
# Création des flashcards
with open("seed_data.json", "r") as f:
    seed_data = json.load(f)

for theme in seed_data["contenu"]:
    id_theme = theme["id_theme"]
    cards = theme["cartes"]
    for card in cards:
        question = card["question"]
        reponse = card["reponse"]
        probabilite = card["probabilite"]
        create_card(question, reponse, probabilite, id_theme)


# %%
# Création des statistiques
with sqlite3.connect("flashcards.db") as conn:
    c = conn.cursor()

    today = datetime.now()

    for i in range(14, -1, -1):
        bonnes_reponses = random.randint(0, 10)
        mauvaises_reponses = random.randint(0, 10)

        # Ajouter les données pour les 15 derniers jours
        date = (today - timedelta(days=i)).strftime("%Y-%m-%d")

        c.execute(
            """
        INSERT INTO stats (bonnes_reponses, mauvaises_reponses, date) VALUES
        (?, ?, ?)""",
            (bonnes_reponses, mauvaises_reponses, date),
        )

        print("Statstique créée")
