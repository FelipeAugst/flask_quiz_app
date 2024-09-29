from flask import request,Blueprint
from quiz_app.auth import autenticar


quiz = Blueprint("quiz",__name__,url_prefix="/quiz")


@quiz.post("/<int:id>/criar")
@autenticar
def criar_quiz(id):
    return "Publicando quiz"

@quiz.get("/")
def listar_quiz():
    return "quizes:"


@quiz.get("/<string:pesquisa>")
def buscar_quiz(pesquisa):
    return "quizes:"



@quiz.put("/<int:id>/alterar/<int:quizid>")
@autenticar
def editar_quiz(id,quizid):
    return "alterando quiz"


@quiz.delete("/<int:id>/deletar/<int:quizid>")
@autenticar
def deletar_quiz(id,quizid):
    return "deletando quiz"