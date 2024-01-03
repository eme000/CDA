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
cursor = conn.cursor()

# Exemple: Sélectionnez toutes les lignes de la table 'Couleur'
query = "SELECT * FROM Couleur"

# Exécutez la requête
cursor.execute(query)

# Récupérez les résultats
results = cursor.fetchall()

# Affichez les résultats
for row in results:
    print(row)

# Fermez le curseur et la connexion
cursor.close()
conn.close()
