# routes.py
# Ajoutez conn pour la connexion à la base de données
#from app import conn
from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/mini_factory__1_')
def mini_factory():
    return render_template('mini_factory_1.html')

@app.route('/mini_factory__1_/mini_factory__1_production')
def mini_factory_1_production():
    # Importez conn ici pour éviter l'importation circulaire
    from app import conn

    # Utilisez votre logique pour récupérer la dernière valeur de température depuis la base de données
    last_temperature = get_last_temperature(conn)

    # Passez cette valeur à la page HTML
    return render_template('mini_factory_1_production.html', last_temperature=last_temperature)

# Ajoutez cette fonction pour récupérer la dernière valeur de température
def get_last_temperature(conn):
    # Utilisez votre logique pour récupérer la dernière valeur de température depuis la base de données
    query = "SELECT VALEUR_RELEVE FROM LUMINOSITE ORDER BY DATE_RELEVE DESC LIMIT 1"
    
    # Exécutez la requête et récupérez la valeur de température
    result = conn.execute(query).fetchone()

    # Vérifiez si la valeur existe
    if result:
        last_temperature = result[0]
    else:
        last_temperature = None

    return last_temperature

@app.route('/list_table')
def list_table():
    return render_template('list_bdd.html')

@app.route('/test')
def show_tables():
    # Vous devrez implémenter la logique pour récupérer les noms des tables depuis la base de données ici
    table_names = ['Couleur', 'GESTION_ERREUR', 'GESTION_STOCK', 'LUMINOSITE', 'Ordre_de_fabrication', 'PRESSION_ATH', 'PRODUIT', 'TAUX_CO2', 'TAUX_HUMIDITE', 'TEMP_AIR', 'ilo', 'information_erreur', 'suivit_production', 'unité_fab']

    return render_template('index.html', liste=table_names)
