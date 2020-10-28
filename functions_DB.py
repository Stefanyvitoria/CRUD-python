import dbm

def Create(user, email): #Função que adiciona um novo registro.
    db = dbm.open('Base.db', 'c')
    if user in db:
        return f'Usuário já existe nos registros!'
    else:
        db[user] = email
        return f'Usuário criado com sucesso!'

def Read(user): #Função que consulta um registro.
    db = dbm.open('Base.db', 'r')
    if user in db: 
        return f'E-mail: {db[user].decode()}'
    else:
        return 'Usuário não encontrado nos registros!'
    
def Update(user): #Função que atualiza um registro.
    db = dbm.open('Base.db', 'c')
    if user in db:
        db[user] = input('E-mail: ')
        return 'Usuário Atualizado!'
    else:
        return 'Usuário não encontrado nos registros!'

def Delete(user): #Função que apaga um registro.
    db = dbm.open('Base.db', 'c')
    if user in db:
        del db[user]
        return 'Usuário Deletado!'
    else:
        return 'Usuário não encontrado nos registros!'