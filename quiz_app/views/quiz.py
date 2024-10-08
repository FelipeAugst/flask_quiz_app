from flask import request,Blueprint, abort, jsonify
from quiz_app.db_connector.db_con import querySQL, fechResultToDict
from quiz_app.auth import autenticar


quiz = Blueprint("quiz",__name__,url_prefix="/quiz")


@quiz.post("/<int:id>/criar")
@autenticar
def criar_quiz(id):
    quiz = request.json
    tema = quiz["tema"]
    titulo = quiz["titulo"]
    qresult = querySQL(query='''INSERT INTO QUIZ(TEMA, TITULO) VALUES (?,?)''', args=(tema, titulo))
    if qresult == None:
        abort(500)
    else:
        return jsonify(qresult)

@quiz.get("/<int:id>/")
@autenticar
def listar_quiz(id):

    qresult = querySQL(query='''SELECT * FROM QUIZ;''', args=())
    if qresult == None:
        abort(500)
    else:
        return jsonify(fechResultToDict(qresult, ("id", "tema", "titulo")))


@quiz.get("/<int:id>/search")
def buscar_quiz(id):

    req_data = request.json
    tema = ""
    titulo = ""
    argq = ""
    argF = ()

    if "tema" in req_data:
        tema = req_data["tema"]
        argq = "TEMA = (?)"
        argF = (tema, )
    
    if "titulo" in req_data:
        titulo = req_data ["titulo"]
        if argq != "":
            argq = argq + "AND TITULO = (?)"
            argF = (tema, titulo,)
        else:
            argq = "TITULO = (?)"
            argF = (titulo,)
    
    if not ("tema" in req_data) and not ("titulo" in req_data):
        return abort(400)

    qresult = querySQL(query=f'''SELECT TEMA, TITULO FROM QUIZ WHERE {argq};''', args=argF)
    if qresult == None:
        abort(500)
    else:
        return jsonify(fechResultToDict(qresult, ("tema", "titulo")))



@quiz.put("/<int:id>/alterar/<int:quizid>")
@autenticar
def editar_quiz(id,quizid):

    #try:
        req_data = request.json
        tema = req_data['tema']
        titulo = req_data['titulo']

        qresult = querySQL(query='''UPDATE QUIZ SET TITULO = ?, TEMA = ? WHERE ID = ?;''', args=(titulo, tema, quizid,))
        if qresult == None:
            abort(500)
        else:
            return jsonify(qresult)
    #except:
        #return abort(400)


@quiz.delete("/<int:id>/deletar/<int:quizid>")
@autenticar
def deletar_quiz(id,quizid):
    qresult = querySQL(query= f''' DELETE FROM QUIZ WHERE ID = ?''', args=(quizid,))
    if qresult == None:
        abort(500)
    else:
        return jsonify(qresult)