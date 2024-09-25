from flask import Blueprint,abort,request

from flask import request,abort,jsonify,render_template,make_response,Blueprint
from markupsafe import escape
from .dados import db
from quiz_app import auth



user = Blueprint("user",__name__,url_prefix="/usuario")

@user.route("/criar",methods=['POST'])
def criar_usuario():
    try:
        usuario = request.json
        nome= usuario['nome']
        email= usuario['email']
        nick = usuario['nick']
        senha = usuario['senha']
        db.append(usuario)
        criado= {"criado":{"nome":nome,"email":email}}
        resp = make_response()
        return resp



    except:
        abort(400,"dados invalidos")

@user.get("/")
def mostrar_usuario():
    return jsonify(db)


@user.get("/<string:usuario>")
@auth.autenticar
def buscar_usuario(usuario):
    tamanho = len(db['usuarios'])
    for idx in range(tamanho):
        if db[idx]['nome']== usuario:
            return db['usuarios'][idx]
            
    return "<h1>Usuario nao encontrado</h1>"




@user.put("/alterar/<int:id>")
@auth.autenticar
def altera_usuario(id):
    json = request.json
    email= json['email']
    nome= json['nome']
    nick= json['nick']
    for usuario in db:
        if usuario['id']== id:
            usuario['email']= email
            usuario['nick']=nick
            usuario['nome']=nome
            return jsonify(db)
    return "<h1>Usuario nao encontrado</h1>"



    
@user.delete("/deletar/<int:id>")
@auth.autenticar
def deletar_usuario(id):
    tamanho = len(db)
    for idx in range(tamanho):
        if db[idx]['id']== id:
            db.pop(idx)
            return "Deletado"
            
    return "<h1>Usuario nao encontrado</h1>"

