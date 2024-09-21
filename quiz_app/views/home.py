from flask import Blueprint,request,abort,redirect,make_response
from .dados import db
from quiz_app import auth


home = Blueprint("home",__name__)


@home.get("/")
def home_page():return f"<h1>Pagina Principal</h1>"


@home.route("/login",mwthods=['POST','GET'])
def login():
    if request.method== "GET":
        return "<h1>Tela de login</h1>"
    try:
        dados = request.json
        nick= dados['nick']
        senha = dados['senha']
        for usuario in db:
            if usuario['nick']== nick:
                if usuario['senha']==senha:
                    resp = make_response(redirect("/"))
                    token = auth.gerar_token("1234",{"nick":nick,"senha":senha})
                    resp.set_cookie("auth",token)

                    return resp
                else:
                    return abort(403,"senha incorreta")
        return abort(403,"usuario nao encontrado")
        
    except Exception as ex:
        return abort(403,ex)

    