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
    
    def connection_bdd(self,requete_sql):
        # Connexion à la base de données
        conn = mysql.connector.connect(
        host=self.host,
        user=self.user,
        password=self.password,
        database=self.database)

        curseur = conn.cursor()

        curseur.execute(requete_sql)
        
        #demander a ERIC J'AI PAS COMPRIS
        # Récupération des résultats
        results = curseur.fetchall()

        # Fermeture du curseur et de la connexion
        curseur.close()
        conn.close()
        

        return results


    
    def getLAST(self,nom_table):
        # ne fonctionne pas sans le F demander a ERIC 
        requeteSQL = f"SELECT `VALEUR_RELEVE` FROM `{nom_table}` ORDER BY `ID_RELEVE` DESC LIMIT 1"
        #   Exécutez la requête
        sortie_requet = self.connection_bdd(requeteSQL)
        # Traitement des résultats
        VALEUR_DE_SORTIE = 0.0
        for resultat in sortie_requet:
            VALEUR_DE_SORTIE = resultat[0]
        return VALEUR_DE_SORTIE
    
    def getLAST10(self,nom_table):
        # ne fonctionne pas sans le F demander a ERIC 
        requeteSQL = f"SELECT `VALEUR_RELEVE` FROM `{nom_table}` ORDER BY `ID_RELEVE` DESC LIMIT 10"
        #   Exécutez la requête
        sortie_requet = self.connection_bdd(requeteSQL)
        # Traitement des résultats
        list_sortie=[0,0,0,0,0,0,0,0,0,0,0]
        # Affichez les résultats
        I=0
        for row in sortie_requet:
            list_sortie[I]=row[0]
            I=I+1
        return list_sortie