from flask import Blueprint,request,abort,redirect,make_response,session
from .dados import db
from quiz_app import auth
import bcrypt
from quiz_app.senhas import senha_correta


home = Blueprint("home",__name__,url_prefix="/")


@home.get("/")
def home_page():return f"<h1>Pagina Principal</h1>"


@home.post("/login/")
def login():
        dados = request.json
        nick= dados['nick']
        senha = dados['senha']
        for usuario in db:
            if usuario['nick']== nick:
                senha_salva =usuario['senha']
                senha =senha
                if senha_correta(senha,senha_salva):
                    resp = make_response("logado",200)
                    token = auth.gerar_token(dados={"userid":usuario['id']})
                    resp.set_cookie("auth",token)
                    return resp
                else:
                    return abort(403,"senha incorreta")
        return abort(403,"usuario nao encontrado")
        

    