# routes.py
# Ajoutez conn pour la connexion à la base de données
#from app import conn
from app import app
import mysql.connector
from app import inter
from form import SignUpForm

from flask import render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/mini_factory__1_')
def mini_factory():
    return render_template('mini_factory_1.html')

@app.route('/mini_factory__1_/mini_factory__1_production')
def mini_factory_1_production():
   # Passez cette valeur à la page HTML
    return render_template('mini_factory_1_production.html', last_temperature=inter.getLAST("TEMP_AIR"),
                           last_co2=inter.getLAST("TAUX_CO2"),
                           last_humidite=inter.getLAST("TAUX_HUMIDITE"),
                           last_luminosite=inter.getLAST("LUMINOSITE"),
                           last_ath=inter.getLAST("PRESSION_ATH"),
                           nb_bleu=inter.getStock_Couleur(1),
                           nb_rouge=inter.getStock_Couleur(2),
                           nb_blanc=inter.getStock_Couleur(3),
                           date_of=inter.getDate_OF(),
                           couleur_of=inter.getCouleur_OF())

@app.route('/mini_factory__1_/mini_factory__1_production/info_capteur_env')
def info_capteur_env_1():
    return render_template('info_capteur_env.html',last_10_temperature=inter.getLAST10("TEMP_AIR"),
                           last_10_co2=inter.getLAST10("TAUX_CO2"),
                           last_10_humidite=inter.getLAST10("TAUX_HUMIDITE"),
                           last_10_luminosite=inter.getLAST10("LUMINOSITE"),
                           last_10_ath=inter.getLAST10("PRESSION_ATH"))

@app.route('/mini_factory__1_/mini_factory__1_production/Gestion_stock')
def gestion_stock_1():
    return render_template('gestion_stock.html',bdd_1_emplcement_1_couleur=inter.getStock("1"),
                           bdd_1_emplcement_2_couleur=inter.getStock("2"),
                           bdd_1_emplcement_3_couleur=inter.getStock("3"),
                           bdd_1_emplcement_4_couleur=inter.getStock("4"),
                           bdd_1_emplcement_5_couleur=inter.getStock("5"),
                           bdd_1_emplcement_6_couleur=inter.getStock("6"),
                           bdd_1_emplcement_7_couleur=inter.getStock("7"),
                           bdd_1_emplcement_8_couleur=inter.getStock("8"),
                           bdd_1_emplcement_9_couleur=inter.getStock("9"))
    
@app.route('/mini_factory__1_/mini_factory__1_production/OF')
def info_OF():
    return render_template('info_OF_.html',last_10_of_date=inter.getDate_OF_10(),
                           last_10_of_couleur=inter.getCouleur_OF_10())

@app.route('/list_table')
def list_table():
    return render_template('list_bdd.html')

@app.route('/mini_factory/Ilots')
def list_ilots():
    return render_template('ilots.html')


@app.route('/test')
def show_tables():
    # Vous devrez implémenter la logique pour récupérer les noms des tables depuis la base de données ici
    table_names = ['Couleur', 'GESTION_ERREUR', 'GESTION_STOCK', 'LUMINOSITE', 'Ordre_de_fabrication', 'PRESSION_ATH', 'PRODUIT', 'TAUX_CO2', 'TAUX_HUMIDITE', 'TEMP_AIR', 'ilo', 'information_erreur', 'suivit_production', 'unité_fab']

    return render_template('index.html', liste=table_names)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    error = None
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        hashed_password = generate_password_hash(password)

        error_user = inter.signup_requette(username, hashed_password)
        if error_user == 1:
            error = "Ce nom d'utilisateur est déjà pris."
        else:
            return redirect(url_for('home'))
            
    return render_template('signup.html', form=form, error=error)




@app.route('/login', methods=['GET', 'POST'])
def login():
    form = SignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        hashed_password = generate_password_hash(password)
        
        # Appel à la fonction de connexion
        if inter.login_requette(username, hashed_password,password):
            # Si l'authentification réussit, redirigez l'utilisateur vers la page d'accueil
            return redirect(url_for('home'))
        else:
            # Sinon, affichez un message d'erreur ou redirigez vers une page d'erreur
            flash("Nom d'utilisateur ou mot de passe incorrect.")
    return render_template('login.html', form=form)
