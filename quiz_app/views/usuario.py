from flask import Blueprint,abort,request

from flask import request,abort,jsonify,render_template,make_response,Blueprint
from markupsafe import escape
from .dados import db,buscar
from quiz_app import auth,seguranca
from .senha import senha
import bcrypt




user = Blueprint("user",__name__,url_prefix="/usuario")
user.register_blueprint(senha)


@user.route("/criar",methods=['POST'])
def criar_usuario():
    usuario = request.json
    nome= usuario['nome']
    email= usuario['email']
    nick = usuario['nick']
    usuario['id']= len(db)+1

    senha = usuario['senha']
    senha_criptografada= seguranca.criptografar_senha(senha)
    usuario['senha']= senha_criptografada

    db.append(usuario)
    criado= {"criado":{"nome":nome,"email":email}}
    resp = make_response(jsonify(criado))
    return resp


@user.get("/")
def mostrar_usuario():
    return jsonify(db)


@user.get("/<int:id>")
@auth.autenticar
def buscar_usuario(id):
    usuario = buscar(db,id)
    if usuario==None: 
        return abort(404,"usuario nao encontrado")
    return jsonify(db[usuario])




@user.put("/alterar/<int:id>")
@auth.autenticar
def alterar_usuario(id):
    json = request.json
    email= json['email']
    nome= json['nome']
    nick= json['nick']
    usuario= buscar(db,id)
    if usuario == None:
        return abort(404,"usuario nao encontrado")
    db[usuario]['id']== id
    db[usuario]['email']= email
    db[usuario]['nick']=nick
    db[usuario]['nome']=nome
    return jsonify(db)
   



    
@user.delete("/deletar/<int:id>")
@auth.autenticar
def deletar_usuario(id):
    usuario= buscar(db,id)
    if usuario == None:
        return abort(404,"usuario nao encontrado")

    db.pop(usuario)
    return "Deletado"
            

