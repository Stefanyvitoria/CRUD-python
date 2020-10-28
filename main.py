"""
Sistema de CRUD simples em python.
Autor: Stefany Izidio.
Github: https://github.com/Stefanyvitoria
Email: Stefanyvitoria9307@gmail.com
"""
#Importação dos módulos
import dbm
import crud_functions

def Entrada(): #Função que Recebe o comando de entrada e verifica se a entrada entá correta.
    ent = input("Insira (c/create) para adicionar, (r/read) para consultar, (u/update) para atualizar ou (d/delete) para excluir um registro.\nEntrada: ").strip().lower() 
    opcoes = ['c','create', 'r','read', 'u', 'update','d','delete']

    while (ent not in opcoes) and (ent.strip() != ''):
        print('\nEntrada Inválida!\n')
        ent = input("Insira (c/create) para adicionar, (r/read) para consultar, (u/update) para atualizar ou (d/delete) para excluir um registro.\nEntrada: ").strip().lower()
    if not ent:
        raise "Fim"
    return ent

def root(): #Função que cria o banco de dados e inicia as execuções. 
    db = dbm.open('Banco.db', 'c')
    db.close()
    entrada = Entrada()
    if entrada.startswith('c'):
        user = input('Adicionar usuário: ').lower().strip()
        email = input('E-mail: ')
        print(crud_functions.Create(user, email))

    elif entrada.startswith('r'): 
        user = input('Consultar usuário: ').lower().strip()
        print(crud_functions.Read(user))

    elif entrada.startswith('u'):
        user = input('Atualizar usuário: ').lower().strip()
        print(crud_functions.Update(user))
    
    elif entrada.startswith('d'):  
        user = input('Apagar usuário: ').lower().strip()
        print(crud_functions.Delete(user))

if __name__ == "__main__": #Inicia a função principal.
    try:   
        while True:
            root()
    except: pass