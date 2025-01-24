# Application de Flashcards

Le but de ce projet est de construire une application de flashcards. Ce type d'application permet à l'utilisateur de créer des cartes mentales, avec une information ou question par carte, et d'essayer de répondre à la question ou d'expliquer le concept. La subtilité est que, l'apparition des cartes dépend de si vous arrivez à avoir la bonne réponse. Plus serez à l'aise avec un concept, moins la carte apparaitra, et au contraire, plus vous avez du mal avec un concept, et plus la carte apparaitra fréquemment.

## Schéma de la base de données

Notre base de données comprendra trois tables principales :

- `cards` : Contient les flashcards.
- `themes` : Contient les thèmes des flashcards.
- `stats` : Contient les statistiques des réponses des utilisateurs.

Détail des tables :

- `cards`
  - `id` : INTEGER PRIMARY KEY
  - `question` : TEXT
  - `reponse` : TEXT
  - `probabilite` : REAL
  - `id_theme` : INTEGER, FOREIGN KEY REFERENCES themes(id) ON DELETE RESTRICT
- `themes`
  - `id` : INTEGER PRIMARY KEY
  - `theme` : TEXT
- `stats`
  - `id` : INTEGER PRIMARY KEY
  - `bonnes_reponses` : INTEGER
  - `mauvaises_reponses` : INTEGER
  - `date` : DATE

Le champ probabilite est un réel entre 0.1 et 1.

## Fonctions implémentées

- Initialisation de la base de données
  - `init_db` : Cette fonction initialise la base de données en créant les tables cards, thèmes et stats si elles n'existent pas déjà. Elle insère également des thèmes prédéfinis dans la table themes.
- Fonctions CRUD pour `flashcards`
  - `create_card(question, reponse, probabilite, id_theme)` : Crée une carte.
  - `get_card(id)` : Récupère une carte.
  - `update_card(id, question, reponse, probabilite, id_theme)` : Met à jour une carte.
  - `delete_card(id)` : Supprime une carte.
  - `get_all_cards()` : Récupère toutes les cartes.
  - `get_number_of_cards()` : Retourne le nombre total de cartes.
  - `get_cards_by_theme(id_theme)` : Récupère les cartes appartenant à un thème particulier.
- Fonctions CRUD pour `themes`
  - `create_theme(theme)` : Crée un thème.
  - `get_theme(id_theme)` : Récupère un thème.
  - `update_theme(id_theme, theme)` : Met à jour un thème.
  - `delete_theme(id_theme)` : Supprime un thème.
  - `get_all_themes()` : Récupère tous les thèmes.
- Fonctions CRUD pour `stats`
  - `update_stats(is_correct)` : Incrémente les bonnes et mauvaises réponses par jour dans les stats.
  - `update_card_probability(card_id, is_correct)` : Met à jour la probabilité d'apparition d'une carte.
  - `get_all_stats()` : Récupère les statistiques.
- Suppression des données dans les tables
  - `empty_tables()` : Vide les tables `cards`, `themes` et `stats`.
