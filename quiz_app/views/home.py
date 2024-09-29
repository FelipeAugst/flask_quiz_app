from flask import Blueprint,request,abort,redirect,make_response,session
from .dados import db,buscar
from quiz_app import auth
import bcrypt
from quiz_app.seguranca import senha_correta


home = Blueprint("home",__name__,url_prefix="/")


@home.get("/")
@auth.autenticar
def home_page():return f"<h1>Pagina Principal</h1>"


@home.post("/login/")
def login():
        dados = request.json
        nick= dados['nick']
        senha = dados['senha']
        usuario= buscar(db,nick)
        if usuario== None:
            return abort(400,"usuario nao encontrado")
        senha_salva =db[usuario]['senha']
        senha =senha
        if senha_correta(senha,senha_salva):
            resp = make_response("logado",200)
            token = auth.gerar_token(dados={"userid":db[usuario]['id']})
            resp.set_cookie("auth",token)
            return resp
        else:
            return abort(403,"senha incorreta")
        
        

    