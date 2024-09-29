import bcrypt

def criptografar_senha(senha):
    senha = bytes(senha,encoding='utf-8')
    salt= bcrypt.gensalt()
    senha_criptografada= bcrypt.hashpw(senha,salt)
    return str(senha_criptografada,encoding='utf-8')



def senha_correta(senha,senha_salva):
    senha= bytes(senha,encoding='utf-8')
    senha_salva= bytes(senha_salva,encoding='utf-8')
    return bcrypt.checkpw(senha,senha_salva)

