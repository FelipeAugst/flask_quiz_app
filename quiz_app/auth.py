import jwt
from flask import request, redirect,abort
from functools import wraps




def gerar_token(secret,data=None):
    token= jwt.encode(data,secret)
    return token


def autenticar(handler):
    @wraps(handler)
    def verifica_token(**kwargs):
        chave="1234"
        token = request.cookies.get("auth")
        dados = jwt.decode(token,chave,algorithms=['HS256'])
        if dados == None:
            redirect("/login")
        if dados['userid'] != kwargs['id']:
            abort(403,"Operacao nao permitida")

        return handler(**kwargs)
    return verifica_token

