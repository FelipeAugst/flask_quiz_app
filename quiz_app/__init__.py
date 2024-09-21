from flask import Flask
from views import usuario

def create_app(debug=True):
    app = Flask()
    app.config['SECRET_KEY']= "MINHA CHAVE"
    app.config['DEBUG']=debug
    app.register_blueprint(usuario)


    return app
