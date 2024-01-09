import os
import mysql.connector
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer les informations de connexion depuis les variables d'environnement
host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_DATABASE')

# Connexion à la base de données
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Création d'un curseur
curseur_temp = conn.cursor()

requette = "SELECT Couleur FROM GESTION_STOCK WHERE emplacement = '1';"

# Exécutez la requête
curseur_temp.execute(requette)


# Affichez les résultats
I=0
row =[99]
for row in curseur_temp:
    print(row[0])

    I=I+1
print(" ")
print(row[0])
print(" ")


# Fermez le curseur et la connexion
curseur_temp.close()
conn.close()
