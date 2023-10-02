class PilhaCaracteres:
    def __init__(self):
        self.items = []

    def esta_vazia(self):
        return len(self.items) == 0

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.items.pop()
        else:
            return None

# Função para inverter uma string usando uma pilha
def inverter_string(string):
    pilha = PilhaCaracteres()
    
    for caractere in string:
        pilha.empilhar(caractere)
    
    string_invertida = ''
    while not pilha.esta_vazia():
        string_invertida += pilha.desempilhar()
    
    return string_invertida

# Ler uma string do teclado
entrada = input("Digite uma string: ")

# Inverter a string usando a função inverter_string
string_invertida = inverter_string(entrada)

# Imprimir a string invertida
print("String invertida:", string_invertida)
