import tkinter, crud_functions, main

class crud():
    def __init__(self):
        self.janela = tkinter.Tk()
        self.janela.title("CRUD")
        self.janela.geometry("250x250")
    
        self.labels()
        self.janela.mainloop()

    def labels(self):
        self.botaoC = tkinter.Button(text='Criar', width= '15', height='3')
        self.botaoR = tkinter.Button(text='Ler', width= '15', height='3')    
        self.botaoU = tkinter.Button(text='Atualizar', width= '15', height='3')
        self.botaoD = tkinter.Button(text='Apagar', width= '15', height='3')
        self.empacotamento_labels()
    
    def empacotamento_labels(self):
        self.botaoC.pack()
        self.botaoR.pack()
        self.botaoU.pack()
        self.botaoD.pack()

    def Banco(self):
        pass

if __name__ == '__main__':
    crud()