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
    if not ent:
        raise "Fim"

    while ent not in opcoes:
        print('\tEntrada Inválida!')
        ent = input("Insira (c/create) para adicionar, (r/read) para consultar, (u/update) para atualizar ou (d/delete) para excluir um registro.\nEntrada: ").strip().lower()
    return ent

def root(): #Função que cria o banco de dados e inicia as execuções. 
    db = dbm.open('Banco.db', 'c')
    db.close()
    entrada = Entrada()
    if entrada.startswith('c'): crud_functions.Create()
    elif entrada.startswith('r'): crud_functions.Read()
    elif entrada.startswith('u'): crud_functions.Update()
    elif entrada.startswith('d'): crud_functions.Delete()

if __name__ == "__main__": #Inicia a função principal.
    try:   
        while True:
            root()
    except: pass