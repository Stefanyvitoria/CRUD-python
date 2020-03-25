import dbm

def Create(): #Função que adiciona um novo registro.
    db = dbm.open('Banco.db', 'c')
    user = input('Adicionar usuário: ').lower().strip()
    if user in db: print(f'Usuário já existe nos registros!')
    else:
        email = input('E-mail: ')
        db[user] = email
        print(f'\tUsuário criado com sucesso!')

def Read(): #Função que consulta um registro.
    db = dbm.open('Banco.db', 'r')
    user = input('Consultar usuário: ').lower().strip()
    if user in db: print(f'E-mail: {db[user].decode()}')
    else:
        print('Usuário não encontrado nos registros!')

def Delete(): #Função que apaga um registro.
    db = dbm.open('Banco.db', 'c')
    user = input('Apagar usuário: ').lower().strip()
    if user in db:
        del db[user]
        print('Usuário Deletado!')
    else:
        print('Usuário não encontrado nos registros!')
    
def Update(): #Função que atualiza um registro.
    db = dbm.open('Banco.db', 'c')
    user = input('Atualizar usuário: ').lower().strip()
    if user in db:
        db[user] = input('E-mail: ')
        print('Usuário Atualizado!')
    else:
        print('Usuário não encontrado nos registros!')
