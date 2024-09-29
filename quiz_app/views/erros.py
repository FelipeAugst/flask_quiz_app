from flask import render_template, request

def erro_404(ex):
    url = request.url
    return render_template("404.html",endereco=url)