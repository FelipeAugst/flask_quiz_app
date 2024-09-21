import jwt
from flask import request, redirect
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
        return handler(**kwargs)
    return verifica_token

