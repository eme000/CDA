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
        
        conn.commit()

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
    
    def getStock(self,emplacement):
        requeteSQL = f"SELECT Couleur FROM GESTION_STOCK WHERE emplacement = '{emplacement}'"
        #   Exécutez la requête
        sortie_requet = self.connection_bdd(requeteSQL)
        couleur=[99]
        VALEUR_DE_SORTIE=99
        for couleur in sortie_requet:
            VALEUR_DE_SORTIE=couleur[0]
        return VALEUR_DE_SORTIE
    
    def getStock_Couleur(self,couleur):
        requeteSQL = f"SELECT Couleur FROM GESTION_STOCK WHERE emplacement <> '99' AND Couleur = '{couleur}'"
        sortie_requet = self.connection_bdd(requeteSQL)
        row =[0]
        nb_couleur=0
        I=0
        for row in sortie_requet:
            I=I+1
        nb_couleur=I
        return nb_couleur

    def getDate_OF(self):
        requeteSQL = "SELECT `DATE_OF` FROM `Ordre_de_fabrication` ORDER BY `ID_OF` DESC LIMIT 1"
        sortie_requet = self.connection_bdd(requeteSQL)
        for row in sortie_requet:
            date_of=row[0]
        return date_of

    def getCouleur_OF(self):
        requeteSQL = "SELECT `COULEUR_PRODUIT` FROM `Ordre_de_fabrication` ORDER BY `ID_OF` DESC LIMIT 1"
        sortie_requet = self.connection_bdd(requeteSQL)
        for row in sortie_requet:
            couleur=row[0]
        print(couleur)
        return couleur
    
    def getDate_OF_10(self):
        # ne fonctionne pas sans le F demander a ERIC 
        requeteSQL = f"SELECT `DATE_OF` FROM `Ordre_de_fabrication` ORDER BY `ID_OF` DESC LIMIT 10"
        #   Exécutez la requête
        sortie_requet = self.connection_bdd(requeteSQL)
        # Traitement des résultats
        list_sortie=[0,0,0,0,0,0,0,0,0,0,0]
        # Affichez les résultats
        I=0
        for row in sortie_requet:
            list_sortie[I]=row[0]
            I=I+1
        print(list_sortie)
        return list_sortie
    
    
    def getCouleur_OF_10(self):
        # ne fonctionne pas sans le F demander a ERIC 
        requeteSQL = f"SELECT `COULEUR_PRODUIT` FROM `Ordre_de_fabrication` ORDER BY `ID_OF` DESC LIMIT 10"
        #   Exécutez la requête
        sortie_requet = self.connection_bdd(requeteSQL)
        # Traitement des résultats
        list_sortie=[0,0,0,0,0,0,0,0,0,0,0]
        # Affichez les résultats
        I=0
        for row in sortie_requet:
            list_sortie[I]=row[0]
            I=I+1
        print(list_sortie)
        return list_sortie
    

    def signup_requette(self, username, hashed_password):
        try:
            test = 0
            query = f"INSERT INTO `users` (`username`, `password_hash`) VALUES ('{username}', '{hashed_password}');"
            print('ouig')
            self.connection_bdd(query)
            
        except Exception as e:
            if "1062" in str(e):
                print("Erreur : Ce nom d'utilisateur existe déjà.")
                test = 1
                return test
            else:
                print(f"Erreur : {e}")
                return False
        
        
