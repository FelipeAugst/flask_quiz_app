from flask import Blueprint,request,abort,redirect,make_response,session
from .dados import db
from quiz_app import auth
import bcrypt


home = Blueprint("home",__name__)


@home.get("/")
def home_page():return f"<h1>Pagina Principal</h1>"


@home.route("/login",methods=['POST','GET'])
def login():
    if request.method== "GET":
        return "<h1>Tela de login</h1>"
    try:
        dados = request.json
        nick= dados['nick']
        senha = bcrypt.hashpw(dados['senha'])
        for usuario in db:
            if usuario['nick']== nick:
                if usuario['senha']==senha:
                    resp = make_response("logado",200)
                    chave= session.get("SECRET_KEY")
                    token = auth.gerar_token(chave,{"userid":usuario['id']})
                    resp.set_cookie("auth",token)
                    return resp
                else:
                    return abort(403,"senha incorreta")
        return abort(403,"usuario nao encontrado")
        
    except Exception as ex:
        print(ex)
        return abort(404)

    