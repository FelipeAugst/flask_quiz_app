from flask import Blueprint,request,abort
from quiz_app.auth import autenticar
import quiz_app.seguranca as seguranca
from .dados import db,buscar


senha = Blueprint("senha",__name__,url_prefix="/senha")


@senha.post("/<int:id>/alterar")
@autenticar
def alterar_senha(id):
    dados = request.json
    senha_antiga= dados['antiga']
    nova_senha= dados['nova']
    confirmacao = dados['confirmacao']

    if confirmacao != nova_senha:
        abort(400,"confirmacao diferente da nova senha")
    nova_senha= seguranca.criptografar_senha(nova_senha)
    usuario = buscar(db,id)
    if not seguranca.senha_correta(senha_antiga,db[usuario]['senha']):
        return abort(403,"Senha incorreta")
    db[usuario]['senha']= nova_senha
    return "Senha alterada"
    