import os
import mysql.connector
from dotenv import load_dotenv


class interface:
    def __init__(self): # constructeur
        # Charger les variables d'environnement depuis le fichier .env
        load_dotenv()

        # Récupérer les informations de connexion depuis les variables d'environnement
        self.host = os.getenv('DB_HOST')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        
        self.database = os.getenv('DB_DATABASE')

    def __del__(self): # destructeur
        pass
        # close fonction
        
    def getTemp(self):
        # Connexion à la base de données
        conn = mysql.connector.connect(
        host=self.host,
        user=self.user,
        password=self.password,
        database=self.database)
        curseur_temp = conn.cursor()

        requeteSQL = "SELECT `VALEUR_RELEVE` FROM `TEMP_AIR` ORDER BY `ID_RELEVE` DESC LIMIT 1"

        #   Exécutez la requête
        liste_resultat=curseur_temp.execute(requeteSQL)
        temp = 0.0
        print(type(curseur_temp))
        print(curseur_temp)
        for result in curseur_temp:
            print(type(result))
            print(result)
            temp = result[0]
            

        # Fermez le curseur et la connexion
        curseur_temp.close()
        conn.close()
        
        return temp