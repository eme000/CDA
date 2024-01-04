from app import app
from flask import render_template


@app.route('/') # decorators
def home():
    return render_template ('home.html')
    return strResult


@app.route('/list')
def list():
    return render_template ('list_bdd.html',)
    return strResult


@app.route('/test')
def show_tables():
    # Vous devrez implémenter la logique pour récupérer les noms des tables depuis la base de données ici
    table_names = ['Couleur', 'GESTION_ERREUR', 'GESTION_STOCK', 'LUMINOSITE', 'Ordre_de_fabrication', 'PRESSION_ATH', 'PRODUIT', 'TAUX_CO2', 'TAUX_HUMIDITE', 'TEMP_AIR', 'ilo', 'information_erreur', 'suivit_production', 'unité_fab']

    return render_template('index.html', liste=table_names)

