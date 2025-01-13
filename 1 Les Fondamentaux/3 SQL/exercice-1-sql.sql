-- # Exercice 1 SQL

-- 1. Création des tables
CREATE TABLE Auteurs (
   AuteurID INT PRIMARY KEY,
   Nom VARCHAR,
   Prénom VARCHAR,
   Pays VARCHAR
);

CREATE TABLE Genres (
   GenreID INT PRIMARY KEY,
   NomGenre VARCHAR
);

CREATE TABLE Livres (
   LivreID INT PRIMARY KEY,
   Titre VARCHAR,
   AuteurID INT,
   GenreID INT,
   DatePublication DATE,
   Disponible BOOLEAN,
   FOREIGN KEY (AuteurID) REFERENCES Auteurs(AuteurID),
   FOREIGN KEY (GenreID) REFERENCES Genres(GenreID)
);

CREATE TABLE Emprunteurs (
   EmprunteurID INT PRIMARY KEY,
   Nom VARCHAR,
   Prénom VARCHAR,
   Email VARCHAR,
   Téléphone VARCHAR
);

CREATE TABLE Emprunts (
   EmpruntID INT PRIMARY KEY,
   LivreID INT,
   EmprunteurID INT,
   DateEmprunt DATE,
   DateRetourPrévue DATE,
   DateRetourEffective DATE,
   FOREIGN KEY (LivreID) REFERENCES Livres(LivreID),
   FOREIGN KEY (EmprunteurID) REFERENCES Emprunteurs (EmprunteurID)
);



-- 2. Insertion des données
INSERT INTO Auteurs (AuteurID, Nom, Prénom, Pays) VALUES
(1, 'Hugo', 'Victor', 'France'),
(2, 'Orwell', 'George', 'Royaume-Uni'),
(3, 'Asimov', 'Isaac', 'Russie'),
(4, 'Tolkien', 'J.R.R.', 'Royaume-Uni'),
(5, 'Austen', 'Jane', 'Royaume-Uni'),
(6, 'Dumas', 'Alexandre', 'France'),
(7, 'Bradbury', 'Ray', 'États-Unis'),
(8, 'Camus', 'Albert', 'France'),
(9, 'Verne', 'Jules', 'France'),
(10, 'Hemingway', 'Ernest', 'États-Unis');

INSERT INTO Genres (GenreID, NomGenre) VALUES
(1, 'Roman'),
(2, 'Science-fiction'),
(3, 'Fantasy'),
(4, 'Classique'),
(5, 'Philosophie'),
(6, 'Aventure'),
(7, 'Horreur'),
(8, 'Biographie');

INSERT INTO Livres (LivreID, Titre, AuteurID, GenreID, DatePublication, Disponible) VALUES
(1, 'Les Misérables', 1, 1, '1862-01-01', TRUE),
(2, '1984', 2, 2, '1949-06-08', FALSE),
(3, 'Fondation', 3, 2, '1951-01-01', TRUE),
(4, 'Le Seigneur des Anneaux', 4, 3, '1954-07-29', TRUE),
(5, 'Orgueil et Préjugés', 5, 4, '1813-01-28', TRUE),
(6, 'Le Comte de Monte-Cristo', 6, 6, '1844-08-28', TRUE),
(7, 'Fahrenheit 451', 7, 2, '1953-10-19', TRUE),
(8, 'L’Étranger', 8, 5, '1942-01-01', FALSE),
(9, 'Vingt mille lieues sous les mers', 9, 6, '1870-06-20', TRUE),
(10, 'Le Vieil Homme et la Mer', 10, 4, '1952-09-01', FALSE),
(11, 'Les Trois Mousquetaires', 6, 6, '1844-03-14', TRUE),
(12, 'Le Château', NULL, 4, '1926-01-01', TRUE);

INSERT INTO Emprunteurs (EmprunteurID, Nom, Prénom, Email, Téléphone) VALUES
(1, 'Dupont', 'Jean', 'jean.dupont@mail.com', '0601020304'),
(2, 'Martin', 'Lucie', 'lucie.martin@mail.com', '0602030405'),
(3, 'Bernard', 'Paul', 'paul.bernard@mail.com', '0603040506'),
(4, 'Durand', 'Sophie', 'sophie.durand@mail.com', '0604050607'),
(5, 'Lefevre', 'Antoine', NULL, '0605060708'),
(6, 'Roux', 'Marie', 'marie.roux@mail.com', '0606070809'),
(7, 'Moreau', 'Julie', 'julie.moreau@mail.com', '0607080910'),
(8, 'Petit', 'Nicolas', 'nicolas.petit@mail.com', '0608091011'),
(9, 'Girard', 'Laure', 'laure.girard@mail.com', '0609101112'),
(10, 'Andre', 'Thomas', 'thomas.andre@mail.com', NULL),
(11, 'Lam', 'Marc', 'marc.lam@mail.com', '0609101113');

INSERT INTO Emprunts (EmpruntID, LivreID, EmprunteurID, DateEmprunt, DateRetourPrévue, DateRetourEffective) VALUES
(1, 1, 1, '2024-10-10', '2024-10-17', NULL),
(2, 2, 2, '2024-10-11', '2024-10-18', '2024-10-13'),
(3, 3, 3, '2024-10-12', '2024-10-19', NULL),
(4, 4, 4, '2024-10-13', '2024-10-20', '2024-10-17'),
(5, 5, 5, '2024-10-14', '2024-10-21', NULL),
(6, 6, 6, '2024-10-15', '2024-10-22', '2024-10-20'),
(7, 7, 7, '2024-10-16', '2024-10-23', NULL),
(8, 8, 8, '2024-10-17', '2024-10-24', '2024-10-28'),
(9, 9, 9, '2024-10-18', '2024-10-25', NULL),
(10, 5, 10, '2024-10-19', '2024-10-26', NULL),
(11, 11, 1, '2024-10-20', '2024-10-27', '2024-10-25'),
(12, 7, 2, '2024-10-21', '2024-10-28', NULL),
(13, 8, 3, '2024-10-22', '2024-10-29', NULL),
(15, 1, 5, '2024-10-24', '2024-10-31', NULL),
(16, 4, 6, '2024-10-25', '2024-11-01', NULL),
(17, 9, 7, '2024-10-26', '2024-11-02', NULL);



-- 3. Sélectionner les livres disponibles
-- Écrivez une requête pour récupérer tous les livres disponibles.
SELECT * FROM Livres WHERE Disponible = 1;



-- 4. Trier les livres par date de publication
-- Écrivez une requête pour récupérer les livres et les trier par date de
-- publication, du plus ancien au plus récent.
SELECT * FROM Livres ORDER BY DatePublication;



-- 5. Filtrer les emprunts en cours
-- Écrivez une requête pour récupérer les emprunts dont DateRetourEffective est
-- encore NULL, ce qui signifie que le livre n'a pas encore été rendu.
SELECT * FROM Emprunts WHERE DateRetourEffective IS NULL;



-- 6. Calculer la durée d'un emprunt
-- Écrivez une requête pour calculer la durée (en jours) entre la date d'emprunt
-- et la date de retour effective pour chaque emprunt, et nommez cette nouvelle
-- colonne DuréeEmprunt.
SELECT
    DateEmprunt,
    DateRetourPrévue,
    (JULIANDAY(DateRetourEffective) - JULIANDAY(DateEmprunt)) AS DuréeEmprunt
FROM Emprunts;



-- 7. Jointure sur les livres et les auteurs
-- Écrivez une requête SQL pour afficher le titre des livres ainsi que le nom
-- complet (nom et prénom) de leur auteur. Affichez un livre même s'il n'a pas
-- d'auteur connu, par contre n'affichez pas les auteurs qui n'ont pas de livre
-- dans la base.
SELECT L.Titre, A.Nom, A.Prénom
FROM Livres L
LEFT JOIN Auteurs A
ON L.AuteurID = A.AuteurID;



-- 8. Filtrer les emprunteurs qui n'ont pas encore rendu de livres
-- Utilisez une jointure pour afficher les informations des emprunteurs (nom,
-- prénom, email) qui n'ont pas encore rendu leurs livres (c'est-à-dire les
-- emprunts où la date de retour effective est NULL).
SELECT DISTINCT E1.Nom, E1.Prénom, E1.Email
FROM Emprunteurs E1
JOIN Emprunts E2
ON E1.EmprunteurID = E2.EmprunteurID
WHERE E2.DateRetourEffective IS NULL;



-- 9. Nombre de livres par genre
-- Écrivez une requête qui utilise une jointure pour afficher le nombre de 
-- livres par genre. Le résultat doit montrer le nom du genre et le nombre de
-- livres associés.
SELECT G.NomGenre, COUNT(*) AS NombreLivres
FROM Livres L
JOIN Genres G
ON L.GenreID = G.GenreID
GROUP BY L.GenreID;



-- 10. Durée moyenne d'emprunt par emprunteur
-- Calculez la durée moyenne des emprunts pour chaque emprunteur, et affichez
-- leur nom et prénom ainsi que la durée moyenne en jours.
SELECT
    E1.Nom,
    E1.Prénom,
    AVG(JULIANDAY(E2.DateRetourEffective) - JULIANDAY(E2.DateEmprunt))
        AS DuréeMoyenneEmprunt
FROM Emprunteurs E1
JOIN Emprunts E2
ON E1.EmprunteurID = E2.EmprunteurID
GROUP BY E1.EmprunteurID;



-- 11. Jointure avec emprunteurs, livres, et genres
-- Affichez le nom et le prénom de chaque emprunteur, le titre du livre emprunté
-- et le genre de ce livre. Affichez tous les livres, même ceux qui n'ont pas
-- été empruntés, ainsi que tous les emprunteurs, même s'ils n'ont pas encore
-- emprunté de livre et tous les genres, même s'il n'existe pas de livre pour
-- ces genres.
SELECT E1.Nom, E1.Prénom, L.Titre, G.NomGenre
FROM Emprunteurs E1
FULL OUTER JOIN Emprunts E2
ON E1.EmprunteurID = E2.EmprunteurID
FULL OUTER JOIN Livres L
ON E2.LivreID = L.LivreID
FULL OUTER JOIN Genres G
ON L.GenreID = G.GenreID;



-- 12. Livres les plus empruntés
-- Écrivez une requête SQL pour trouver les trois livres les plus empruntés.
-- Affichez leur titre et le nombre d'emprunts.
SELECT L.Titre, COUNT(*) AS NombreEmprunts
FROM Livres L
JOIN Emprunts E
ON L.LivreID = E.LivreID
GROUP BY L.LivreID
ORDER BY NombreEmprunts DESC
LIMIT 3;



-- 13. Nombre de livres empruntés par emprunteur
-- Écrivez une requête SQL pour afficher le nombre total de livres empruntés par
-- chaque emprunteur. Le résultat doit inclure les emprunteurs qui n'ont jamais
-- emprunté de livre.
SELECT E1.Nom, E1.Prénom, COUNT(LivreID) AS NombreLivresEmpruntes
FROM Emprunteurs E1
LEFT JOIN Emprunts E2
ON E1.EmprunteurID = E2.EmprunteurID
GROUP BY E1.EmprunteurID;



-- 14. Livres jamais empruntés
-- Écrivez une requête SQL pour afficher la liste des livres qui n'ont jamais
-- été empruntés.
SELECT L.Titre
FROM Livres L
WHERE LivreID NOT IN (
    SELECT E.LivreID
    FROM Emprunts E
);



-- 15. Nombre d'emprunteurs par auteur
-- Écrivez une requête SQL pour afficher le nombre total d'emprunteurs pour
-- chaque auteur. Le résultat doit inclure les auteurs dont aucun livre n'a été
-- emprunté.
SELECT A.Nom, A.Prenom, COUNT(DISTINCT E.EmprunteurID) AS NombreEmprunteurs
FROM Emprunts E
JOIN Livres L
ON E.LivreID = L.LivreID
RIGHT JOIN Auteurs A
ON L.AuteurID = A.AuteurID
GROUP BY A.AuteurID 
