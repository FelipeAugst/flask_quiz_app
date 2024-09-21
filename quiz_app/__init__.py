from flask import Flask
from quiz_app.views import usuario,home


def create_app(debug=True):
    app = Flask(__name__)
    app.config['SECRET_KEY']= "MINHA CHAVE"
    app.config['DEBUG']=debug
    app.register_blueprint(usuario.user)
    app.register_blueprint(home.home)


    return app
