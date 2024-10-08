from quiz_app.config import DATABASE_CONECTION
from functools import wraps
from flask import g
import sqlite3

def connect_database(func):

    @wraps(func)
    def make_conetion(**kargs):

        try:
            db = getattr(g, '_database', None)
            if db is None:
                db = g._database = sqlite3.connect(DATABASE_CONECTION['PATH'])
            dat = func(query=kargs['query'], args=kargs['args'], db=db)
            db.close()
            return dat
        except:
            raise(sqlite3.DatabaseError)
        
    return make_conetion

@connect_database
def querySQL(**kargs):

    query = kargs['query']
    db = kargs['db']

    cursor = db.cursor()
    cursor.execute(query, kargs['args'])
    db.commit()
    dados = cursor.fetchall()
    print(dados)

    return dados

def fechResultToDict(fetchData: list = [], keys: tuple = ()):
    data = {}
    tempdados = []
    j = 0

    for row in fetchData:
        for i in range(0, keys.__len__()):
            tempdados.append((str(keys[i]), str(row[i])))
        data[j] = {}
        data[j].update(tempdados)
        j = j + 1
    
    return data

# [(1, 'Flask', 'Integrando sqlite com Flask')]
# (id, tema, titulo)
# (id, 1), (tema, 'flask'), (titulo, 'Integrando sqlite com Flask')
# dict.upt(tupla) ->  {"id": 1, "tema": "flask"}
