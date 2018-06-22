import csv
import pymysql

# On ouvre un fichier de log, afin d'y afficher les éventuelles erreurs
logf = open("log.txt", "w")

# On tente de se connecter à la base de données
try:
    
    conn = pymysql.connect(host="localhost", user='AP', passwd="ap", db='bdd_python')
    cursor = conn.cursor()
    
except Exception as e:
    logf.write('Echec de la connexion à la base de données %s \n' % str(e).encode(encoding='UTF-8', errors='strict'))
    

# On ouvre le fichier csv et on concatène les colonnes C et D puis on stocke le tout dans un nouveau fichier
try:
    
    with open("file.csv", "r") as source, open("result.csv", "w") as result:
        rdr = csv.reader(source, delimiter=';')
        wtr = csv.writer(result, delimiter=';')
        for r in rdr:
            wtr.writerow([r[2] + ' ' + r[3]] + r[0:])
            
except Exception as e:
    logf.write('Echec de l\'ouverture du fichier %s \n' % str(e).encode(encoding='UTF-8', errors='strict'))
    

# On ouvre le fichier créé précédemment afin de l'écrire dans la bdd
with open('result.csv', 'rt') as f:
    csv_data = csv.reader(f, delimiter=';')
    try:

        # On initialise la valeur de l'AI a 1000000 par défaut
        cursor.execute('ALTER TABLE tablename AUTO_INCREMENT = 1000000')
        
    except Exception as e:
        logf.write('Erreur de la modification de l\'auto incrément %s \n' % str(e).encode(encoding='UTF-8',errors='strict'))
        
    for row in csv_data:
        row = [i for i in row if i != '']
        if len(row)==9 and ' DESIGNATION  SIZE \nML' not in row:
            try:

                # On insère les données correspondantes dans la base de données
                cursor.execute("""INSERT INTO `produit`(pr_refour, pr_desi, pr_pack, pr_codebarre, pr_prac, pr_prix) VALUES ('%s', '%s', %s, %s, %s, %s)""" % (row[1], row[0], row[5], row[8], row[6].replace(',', '.'), row[7].replace(',', '.')))

            except Exception as e:
                logf.write('Echec de l\'ajout dans la base de données %s \n' % str(e).encode(encoding='UTF-8', errors='strict'))

    # Enfin on ferme la connection
    try:

        conn.commit()
        conn.close()

    except Exception as e:
        logf.write('Echec de la fermeture de la base de données %s \n' % str(e).encode(encoding='UTF-8', errors='strict'))
