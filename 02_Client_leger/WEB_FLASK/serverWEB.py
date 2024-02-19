from app import app
app.config['SECRET_KEY'] = 'une_cle_secret_oui'
if __name__ == "__main__":
    app.run(host='0.0.0.0')
