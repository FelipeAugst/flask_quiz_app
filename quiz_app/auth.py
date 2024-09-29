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
        if token == None:
            return redirect("/login")
        try:
            dados = jwt.decode(token,chave,algorithms=['HS256'])
            if dados['userid'] != kwargs['id']:
                return abort(403,"Operacao nao permitida")
            return handler(**kwargs)
        except:
            return abort(403,"falha ao extrair token")
    return verifica_token

