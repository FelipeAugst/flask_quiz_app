#base de dados para testarmos as funções 
db = [{"nome":"felipe","email":"felipe@felipe","nick":"felipao","senha":"1234","id":1}, 
           {"nome":"antonio","email":"antonio@antonio","senha":"1234","nick":"tonhao","id":2}, 
           {"nome":"carlos","email":"carlos@carlos","senha":"1234","nick":"carlao","id":3}]

id=len(db)+1

def buscar(db,busca):
    for idx in range(len(db)):
        if db[idx]['nick']== busca or db[idx]['email']==busca or db[idx]['id']==busca:
            return idx
        

    return None