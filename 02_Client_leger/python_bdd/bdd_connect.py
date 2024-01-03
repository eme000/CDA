import mysql.connector

# Paramètres de connexion à la base de données
host = '0.0.0.0'
user = 'root'
password = 'uimm'
database = 'db_test'

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
