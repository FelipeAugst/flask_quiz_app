import jwt
from flask import request, redirect,abort,session
from functools import wraps
from quiz_app import config
import bcrypt





def gerar_token( chave=config.SECRET_KEY,dados=None):
    
    token= jwt.encode(dados,chave)
    return token


def autenticar(handler):
    @wraps(handler)
    def verifica_token(**kwargs):
        chave= config.SECRET_KEY 
        token = request.cookies.get("auth")
        dados = jwt.decode(token,chave,algorithms=['HS256'])
        if dados == None:
            redirect("/login")
        if dados['userid'] != kwargs['id']:
            abort(403,"Operacao nao permitida")

        return handler(**kwargs)
    return verifica_token

