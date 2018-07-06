# CsvToDbPython

CESI - AP17

Projet de rattrapage Python

Par Augustin Julien

L'objectif de ce programme est d'exporter un fichier CSV vers une base de données.

Avant d'utiliser ce programme, plusieurs manipulations sont nécessaires :

  - Créer une base de données MySQL locale et importer dedans le fichier "bdd_python.sql"
  - Ajouter les identifiants de connexion à cette base dans le programme Python "csvToDb.py"
  - Le fichier de départ en ".XSV" doit être converti via le logiciel Excel en fichier ".csv", séparé par des virgules, afin que celui-ci puisse être interprété par le programme.
  
Lorsque ces quelques manipulations sont faites, le programme est prêt à être utilisé.

Description de fonctionnement du programme :

  - Etape 1 - Création d'un fichier de log "logFile.log" afin d'y écrire les éventuels messages d'erreur.
  - Etape 2 - Le programme se connecte à la base de données paramétrée au préalable.
  - Etape 3 - Ouverture du fichier CSV et concaténation de 2 colonnes devant être exportées vers la même colonne dans la base de données.
  - Etape 4 - Ouverture du nouveau fichier généré et début de la phase d'export.
  - Etape 5 - Initialisation de l'auto-incrément avec comme valeur de départ 1 000 000.
  - Etape 6 - Copie des valeurs dans la table produit, les marques étant copiées dans une table différente des autres valeurs, la table "modele_marque".
  - Etape 7 - Fermeture de la connexion à la base de données et fin du programme.
