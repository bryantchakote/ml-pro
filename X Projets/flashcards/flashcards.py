import json
import sqlite3
from datetime import datetime


# Initialisation de la base de données
def init_db():
    """Cette fonction initialise la base de données en créant les tables cards,
    thèmes et stats si elles n'existent pas déjà. Elle insère également des
    thèmes prédéfinis dans la table themes.
    """
    try:
        with sqlite3.connect("flashcards.db") as conn:
            c = conn.cursor()
            c.execute("PRAGMA foreign_keys = ON")

            # Création des tables
            c.execute(
                """
            CREATE TABLE IF NOT EXISTS cards (
                id INTEGER PRIMARY KEY,
                question TEXT,
                reponse TEXT,
                probabilite REAL,
                id_theme INTEGER,
                FOREIGN KEY (id_theme) REFERENCES themes(id) ON DELETE RESTRICT
            )
            """
            )

            c.execute(
                """
            CREATE TABLE IF NOT EXISTS themes (
                id INTEGER PRIMARY KEY,
                theme TEXT
            )
            """
            )

            c.execute(
                """
            CREATE TABLE IF NOT EXISTS stats (
                id INTEGER PRIMARY KEY,
                bonnes_reponses INTEGER,
                mauvaises_reponses INTEGER,
                date DATE
            )
            """
            )

            # Insertion des thèmes (depuis un fichier JSON)
            with open("seed_data.json", "r") as f:
                seed_data = json.load(f)

            for theme in seed_data["contenu"]:
                nom_theme = theme["theme"]
                c.execute("INSERT INTO themes (theme) VALUES (?)", (nom_theme,))

            conn.commit()

            print("Base de données initialisée")

    except sqlite3.Error as e:
        print("Erreur lors de l'initialisation de la base de données :", e)


# Fonctions CRUD pour flashcards
def create_card(question, reponse, probabilite, id_theme):
    """Crée une carte."""
    try:
        with sqlite3.connect("flashcards.db") as conn:
            c = conn.cursor()
            c.execute("PRAGMA foreign_keys = ON")

            c.execute(
                """
            INSERT INTO cards (question, reponse, probabilite, id_theme) VALUES
            (?, ?, ?, ?)
            """,
                (question, reponse, probabilite, id_theme),
            )

            conn.commit()

            print("Carte créée")

    except sqlite3.Error as e:
        print("Erreur lors de la création de la carte :", e)


def get_card(id):
    """Récupère une carte."""
    try:
        with sqlite3.connect("flashcards.db") as conn:
            c = conn.cursor()
            c.execute("PRAGMA foreign_keys = ON")

            c.execute("SELECT * FROM cards WHERE id = ?", (id,))
            card = c.fetchone()

            if card is None:
                print(f"Aucune carte avec l'id {id}")

    except sqlite3.Error as e:
        print("Erreur lors de la récupération de la carte :", e)
        card = None

    return card


def update_card(id, question, reponse, probabilite, id_theme):
    """Met à jour une carte."""
    try:
        with sqlite3.connect("flashcards.db") as conn:
            c = conn.cursor()
            c.execute("PRAGMA foreign_keys = ON")

            c.execute(
                """
            UPDATE cards
            SET question = ?, reponse = ?, probabilite = ?, id_theme = ?
            WHERE id = ?""",
                (question, reponse, probabilite, id_theme, id),
            )

            conn.commit()

            print("Carte mise à jour")

    except sqlite3.Error as e:
        print("Erreur lors de la mise à jour de la carte :", e)


def delete_card(id):
    """Supprime une carte."""
    try:
        with sqlite3.connect("flashcards.db") as conn:
            c = conn.cursor()
            c.execute("PRAGMA foreign_keys = ON")

            c.execute("DELETE FROM cards WHERE id = ?", (id,))

            conn.commit()

            print("Carte supprimée")

    except sqlite3.Error as e:
        print("Erreur lors de la suppression de la carte :", e)


def get_all_cards():
    """Récupère toutes les cartes."""
    try:
        with sqlite3.connect("flashcards.db") as conn:
            c = conn.cursor()
            c.execute("PRAGMA foreign_keys = ON")

            c.execute("SELECT * FROM cards")
            cards = c.fetchall()

            if not cards:
                print("Aucune carte trouvée dans la base de données")
                cards = []

    except sqlite3.Error as e:
        print("Erreur lors de la récupération des cartes :", e)
        cards = None

    return cards


def get_number_of_cards():
    """Retourne le nombre total de cartes."""
    try:
        with sqlite3.connect("flashcards.db") as conn:
            c = conn.cursor()
            c.execute("PRAGMA foreign_keys = ON")

            c.execute("SELECT COUNT(*) AS Count FROM cards")
            n_cards = c.fetchone()[0]

    except sqlite3.Error as e:
        print("Erreur lors du comptage des cartes :", e)
        n_cards = None

    return n_cards


def get_cards_by_theme(id_theme):
    """Récupère les cartes appartenant à un thème particulier."""
    try:
        with sqlite3.connect("flashcards.db") as conn:
            c = conn.cursor()
            c.execute("PRAGMA foreign_keys = ON")

            c.execute("SELECT * FROM cards WHERE id_theme = ?", (id_theme,))
            cards = c.fetchall()

            if not cards:
                print(f"Aucune carte trouvée pour le thème {id_theme}")
                cards = []

    except sqlite3.Error as e:
        print("Erreur lors de la récupération des cartes par thème :", e)
        cards = None

    conn.close()

    return cards


# Fonctions CRUD pour themes
def create_theme(theme):
    """Crée un thème."""
    try:
        with sqlite3.connect("flashcards.db") as conn:
            c = conn.cursor()
            c.execute("PRAGMA foreign_keys = ON")

            c.execute("INSERT INTO themes (theme) VALUES (?)", (theme,))

            conn.commit()

            print("Thème créé")

    except sqlite3.Error as e:
        print("Erreur lors de la création du thème :", e)


def get_theme(id):
    """Récupère un thème."""
    try:
        with sqlite3.connect("flashcards.db") as conn:
            c = conn.cursor()
            c.execute("PRAGMA foreign_keys = ON")

            c.execute("SELECT * FROM themes WHERE id = ?", (id,))
            theme = c.fetchone()

            if theme is None:
                print(f"Aucun theme avec l'id {id}")

    except sqlite3.Error as e:
        print("Erreur lors de la récupération du thème :", e)
        theme = None

    return theme


def update_theme(id, theme):
    """Met à jour un thème."""
    try:
        with sqlite3.connect("flashcards.db") as conn:
            c = conn.cursor()
            c.execute("PRAGMA foreign_keys = ON")

            c.execute("UPDATE themes SET theme = ? WHERE id = ?", (theme, id))

            conn.commit()

        print("Thème mis à jour")
    except sqlite3.Error as e:
        print("Erreur lors de la mise à jour du thème :", e)


def delete_theme(id_theme):
    """Supprime un thème."""
    try:
        with sqlite3.connect("flashcards.db") as conn:
            c = conn.cursor()
            c.execute("PRAGMA foreign_keys = ON")

            c.execute("DELETE FROM themes WHERE id = ?", (id_theme,))

            conn.commit()

            print("Thème supprimé")
    except sqlite3.Error as e:
        print("Erreur lors de la suppression du thème :", e)


def get_all_themes():
    """Récupère tous les thèmes."""
    try:
        with sqlite3.connect("flashcards.db") as conn:
            c = conn.cursor()
            c.execute("PRAGMA foreign_keys = ON")

            c.execute("SELECT * FROM themes")
            themes = c.fetchall()

            if not themes:
                print("Aucun theme trouvé dans la base de données")
                themes = []

    except sqlite3.Error as e:
        print("Erreur lors de la récupération des themes :", e)
        themes = None

    return themes


# Fonctions CRUD pour stats
def update_stats(is_correct):
    """Incrémente les bonnes et mauvaises réponses par jour dans les stats."""
    try:
        with sqlite3.connect("flashcards.db") as conn:
            c = conn.cursor()
            c.execute("PRAGMA foreign_keys = ON")

            # Vérification de l'existence d'une entrée pour la date actuelle
            aujd = datetime.now().strftime("%Y-%m-%d")
            c.execute("SELECT * FROM stats WHERE date = ?", (aujd,))
            stats = c.fetchone()

            # Mise à jour des statistiques existantes
            if stats is not None:
                _, bonnes_reponses, mauvaises_reponses, _ = stats

                if is_correct:
                    bonnes_reponses += 1
                else:
                    mauvaises_reponses += 1

                c.execute(
                    """
                UPDATE stats
                SET bonnes_reponses = ?, mauvaises_reponses = ?
                WHERE date = ?""",
                    (bonnes_reponses, mauvaises_reponses, aujd),
                )

            # Création d'une nouvelle entrée pour la date actuelle
            else:
                bonnes_reponses = 1 if is_correct else 0
                mauvaises_reponses = 0 if is_correct else 1

                c.execute(
                    """
                INSERT INTO stats (bonnes_reponses, mauvaises_reponses, date)
                VALUES (?, ?, ?)""",
                    (bonnes_reponses, mauvaises_reponses, aujd),
                )

            conn.commit()

            print("Statistiques mises à jour")

    except sqlite3.Error as e:
        print("Erreur lors de la mise à jour des statistiques :", e)


def update_card_probability(card_id, is_correct):
    """Met à jour la probabilité d'apparition d'une carte."""
    try:
        with sqlite3.connect("flashcards.db") as conn:
            c = conn.cursor()
            c.execute("PRAGMA foreign_keys = ON")

            # Récupération de la probabilité actuelle
            c.execute("SELECT probabilite FROM cards WHERE id = ?", (card_id,))

            probabilite = c.fetchone()[0]

            # Calcul de la nouvelle probabilité
            if is_correct:
                probabilite *= 0.9
            else:
                probabilite *= 1.1

            # Limitation de la probabilité entre 0.1 et 1
            probabilite = max(0.1, min(probabilite, 1))

            # Mise à jour de la bade de données
            c.execute(
                "UPDATE cards SET probabilite = ? WHERE id = ?", (probabilite, card_id)
            )

            conn.commit()

            print("Probabilité mise à jour")
    except sqlite3.Error as e:
        print("Erreur lors de la mise à jour de la probabilité :", e)


def get_all_stats():
    """Récupère toutes les statistiques."""
    try:
        with sqlite3.connect("flashcards.db") as conn:
            c = conn.cursor()
            c.execute("PRAGMA foreign_keys = ON")

            c.execute("SELECT * FROM stats")
            stats = c.fetchall()

            if not stats:
                print("Aucune stat trouvée dans la base de données")
                stats = []

    except sqlite3.Error as e:
        print("Erreur lors de la récupération des stats :", e)
        stats = None

    return stats


# Suppression des données
def empty_tables():
    """Vide les tables cards, themes et stats."""
    try:
        with sqlite3.connect("flashcards.db") as conn:
            c = conn.cursor()
            c.execute("PRAGMA foreign_keys = ON")

            c.execute("DELETE FROM cards")
            c.execute("DELETE FROM themes")
            c.execute("DELETE FROM stats")

            conn.commit()

            print("Tables vidées")

    except sqlite3.Error as e:
        print("Erreur lors de la suppression des tables :", e)
