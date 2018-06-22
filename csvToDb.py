import csv
import pymysql

# On ouvre un fichier de log, afin d'y afficher les éventuelles erreurs
logf = open("log.txt", "w")

# On tente de se connecter à la base de données
try:

    print('-----Connexion à la base de données-----')
    conn = pymysql.connect(host="localhost", user='AP', passwd="ap", db='bdd_python')
    cursor = conn.cursor()
    print('Connecté à la bdd')

except Exception as e:
    print('Echec de la connexion')
    logf.write('Echec de la connexion à la base de données %s \n' % str(e).encode(encoding='UTF-8', errors='strict'))

# On ouvre le fichier csv et on concatène les colonnes C et D puis on stocke le tout dans un nouveau fichier
try:

    print('-----Ouverture et écriture dans le fichier-----')
    with open("file.csv", "r") as source, open("result.csv", "w") as result:
        rdr = csv.reader(source, delimiter=';')
        wtr = csv.writer(result, delimiter=';')
        for r in rdr:
            wtr.writerow([r[2] + ' ' + r[3]] + r[0:])
        print('Ecriture terminée')

except Exception as e:
    print('Echec de l\'ouverture du fichier')
    logf.write('Echec de l\'ouverture du fichier %s \n' % str(e).encode(encoding='UTF-8', errors='strict'))

# On ouvre le fichier créé précédemment afin de l'écrire dans la bdd
print('-----Ouverture du nouveau fichier-----')
try:

    with open('result.csv', 'rt') as f:
        csv_data = csv.reader(f, delimiter=';')
        try:

            # On initialise la valeur de l'AI a 1000000 par défaut
            cursor.execute('ALTER TABLE `produit` AUTO_INCREMENT = 1000000')
            print('Auto Increment initialisé à 1 000 000')

        except Exception as e:
            print('Erreur lors de l\'initialisation de l\'auto incrément')
            logf.write('Erreur de la modification de l\'auto incrément %s \n' % str(e).encode(encoding='UTF-8', errors='strict'))

        print('Copie des valeurs dans la base de données')
        for row in csv_data:
            row = [i for i in row if i != '']
            if len(row) == 9 and ' DESIGNATION  SIZE \nML' not in row:
                try:

                    # On insère les données correspondantes dans la base de données
                    cursor.execute(
                        """INSERT INTO `produit`(pr_refour, pr_desi, pr_pack, pr_codebarre, pr_prac, pr_prix) VALUES ('%s', '%s', %s, %s, %s, %s)""" % (
                        row[1], row[0], row[5], row[8], row[6].replace(',', '.'), row[7].replace(',', '.')))

                except Exception as e:
                    print('Erreur lors de la copie dans la base de données')
                    logf.write('Echec de l\'ajout dans la base de données %s \n' % str(e).encode(encoding='UTF-8',
                                                                                                 errors='strict'))

        # Enfin on ferme la connection
        try:

            print('----Fermeture de la connexion-----')
            conn.commit()
            conn.close()
            print('Connexion fermée')

        except Exception as e:
            print('Erreur lors de la fermeture de la connexion')
            logf.write('Echec de la fermeture de la base de données %s \n' % str(e).encode(encoding='UTF-8', errors='strict'))

except Exception as e:
    print('Echec de l\'ouverture du fichier')
    logf.write('Echec de l\'ouverture du fichier %s \n' % str(e).encode(encoding='UTF-8', errors='strict'))