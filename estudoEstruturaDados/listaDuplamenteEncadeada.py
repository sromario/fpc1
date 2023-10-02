class No:
    def __init__(self, dado):
        self._dado = dado
        self._anterior = None
        self._proximo = None

    def __str__(self):
        return "No com dado {}".format(self._dado)
    


class Lista: #duplamente encadeada
    def __init__(self):
        self._inicio = None
        self._fim = None

    
    #verificar se lista está vazia
    def isVazia(self):
        if self._inicio is None:
            return True
        return False
    
    #inserir elemento
    def inserirNoFim(self, dado=None):
        novono = No(dado)
        if self.isVazia():
            self._inicio = self._fim = novono
        else:
            novono._anterior = self._fim 
            self._fim._proximo = novono
            self._fim = novono

    #buscar elemento
    def buscar(self,x):
        i = self._inicio
        while i != None:
            if x == i._dado:
                return i
            else:
                i = i._proximo
        return i

    #remover elemento
    def remover(self, x):
        no_encontrado = self.buscar(x)
        if no_encontrado != None:
            if no_encontrado._anterior != None:
                no_encontrado._anterior._proximo = no_encontrado._proximo
            if no_encontrado._proximo != None:
                no_encontrado._proximo._anterior = no_encontrado._anterior
        return no_encontrado
    

    #transforma em objeto str
    def __str__(self):
        s = ""
        i = self._inicio
        while i != None:
            s += " | {}".format(str(i))
            i = i._proximo
        return s
    


#exemplo de uso 
if __name__ == "__main__" :
    entrada = [5, 4, 3, 5, 18]
    minhalista = Lista()

    for i in entrada:
        minhalista.inserirNoFim(i)

    print(minhalista)


       



    