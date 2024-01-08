from flask import Flask
app = Flask(__name__)

from app import inter_bdd
inter = inter_bdd.interface()
from app import routes



if __name__ == '__main__':
    app.run(debug=True)