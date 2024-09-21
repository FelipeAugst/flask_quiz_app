from flask import Blueprint,abort,request

from flask import request,abort,jsonify,render_template,make_response,Blueprint
from markupsafe import escape

#base de dados para testarmos as funções 
dados = {"usuarios":[{"nome":"felipe","email":"felipe@felipe","senha":"1234"}, 
           {"nome":"antonio","email":"antonio@antonio","senha":"1234"}, 
           {"nome":"carlos","email":"carlos@carlos","senha":"1234"}], }


user = Blueprint("user",__name__,url_prefix="/usuario")

@user.route("/criar",methods=['POST'])
def criar_usuario():
    try:
        usuario = request.json
        nome= usuario['nome']
        email= usuario['email']
        nick = usuario['nick']
        nick = usuario['senha']
        dados['usuarios'].append(usuario)
        criado= {"criado":{"nome":nome,"email":email}}
        resp = make_response()
        resp.set_cookie("dados",criado.__str__())
        return resp



    except:
        abort(400,"dados invalidos")

@user.get("/")
def mostrar_usuario():
    return jsonify(request.cookies.get("dados"))


@user.get("/<string:usuario>")
def buscar_usuario(usuario):
    tamanho = len(dados['usuarios'])
    for idx in range(tamanho):
        if dados['usuarios'][idx]['nome']== usuario:
            return dados['usuarios'][idx]
            
    return "<h1>Usuario nao encontrado</h1>"




@user.put("/alterar/<string:nome>")
def altera_usuario(nome):
    json = request.json
    email= json['email']
    for usuario in dados['usuarios']:
        if usuario['nome']== nome:
            usuario['email']= email
            return jsonify(dados)
    return "<h1>Usuario nao encontrado</h1>"



    
@user.delete("/deletar/<string:usuario>")
def deletar_usuario(usuario):
    tamanho = len(dados['usuarios'])