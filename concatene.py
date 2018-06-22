import csv
import pymysql

logf = open("log.txt", "w")

try:
    conn = pymysql.connect(host="localhost", user='AP', passwd="ap", db='bdd_python')
    cursor = conn.cursor()
except Exception as e:
    logf.write('Echec de la connexion à la base de données %s \n' % str(e).encode(encoding='UTF-8', errors='strict'))

with open("fileTest.csv","r") as source, open("result.csv","w") as result:
    rdr = csv.reader(source, delimiter=';')
    wtr = csv.writer(result, delimiter=';')
    for r in rdr:
        print (r)
        wtr.writerow([r[2] + ' ' + r[3]] + r[0:])

with open('result.csv', 'rt') as f:
    csv_data = csv.reader(f, delimiter=';')
    try:
        cursor.execute('ALTER TABLE tablename AUTO_INCREMENT = 1000000')
    except Exception as e:
        logf.write('Erreur de la modification de l\'auto incrément %s \n' % str(e).encode(encoding='UTF-8',errors='strict'))
    for row in csv_data:
        #print (row)
        row = [i for i in row if i != '']
        #print (row)
        if len(row)==9 and ' DESIGNATION  SIZE \nML' not in row:
            print (row)
            try:
                print (row[1])
                print (row[0])
                print (row[5])
                print (row[8])
                print (row[6])
                print (row[7])
                cursor.execute("""INSERT INTO `produit`(pr_refour, pr_desi, pr_pack, pr_codebarre, pr_prac, pr_prix) VALUES ('%s', '%s', %s, %s, %s, %s)""" % (row[1], row[0], row[5], row[8], row[6].replace(',','.'), row[7].replace(',','.')))
            except Exception as e:
                logf.write('Echec de l\'ajout dans la base de données %s \n' % str(e).encode(encoding='UTF-8',errors='strict'))
    #close the connection to the database.
    conn.commit()
    conn.close()
