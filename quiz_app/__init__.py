from flask import Flask
from quiz_app.views import usuario,home,erros


def create_app(debug=True):
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app.config['DEBUG']=debug
    app.register_blueprint(usuario.user)
    app.register_blueprint(home.home)
    app.register_error_handler(404,erros.erro_404)
  



    return app
