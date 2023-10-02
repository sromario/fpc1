class No:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tam = 0
    
    
    def inserir(self, dado):
        novono = No(dado)
        if self.tam == 0:
            self.primeiro = novono
            self.ultimo = novono
        else:
            self.ultimo.prox = novono
            self.ultimo = novono
        self.tam += 1
    
    def remover(self):
        if self.tam == 0:
            return None
        else:
            dado = self.primeiro.dado
            self.primeiro = self.primeiro.prox
            self.tam -= 1
            return dado

    def buscar_primeiro(self):
        # Verificar se está vazia
        if self.tam == 0:
            return 0
        return self.primeiro.dado

    def isVazio(self):
        return self.tam == 0




#problema
t = int(input())
for i in range(t):
    regular = Fila()
    preferencial = Fila()
    
    
    comandos = int(input())
    caso = 0
    for i in range(comandos):
        entrada = input().split()

        if entrada[0] == 'f':
            regular.inserir(entrada[1])

        elif entrada[0] == 'p':
            preferencial.inserir(entrada[1])

        elif entrada[0] == 'A':
            #se a fila regular está vazia
            if regular.isVazio():
                preferencial.remover()
            regular.remover()

        elif entrada[0] == 'B':
            #se a fila preferencial está vazia
            if preferencial.isVazio():
                regular.remover()
            preferencial.remover()

        elif entrada[0] == 'I':
            caso += 1 
            print(f"caso: {caso}")
            print(regular.buscar_primeiro(), end="  ")
            print(preferencial.buscar_primeiro())

        else:
            break
 
    