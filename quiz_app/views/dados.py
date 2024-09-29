#base de dados para testarmos as funções 
db = []

id=len(db)+1

def buscar(db,busca):
    for idx in range(len(db)):
        if db[idx]['nick']== busca or db[idx]['email']==busca or db[idx]['id']==busca:
            return idx
        

    return None