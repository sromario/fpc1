class No:

    def __init__(self, dado):
        self.dado = dado
        self.prox = None


class Pilha:

    def __init__(self):
        self.inicio = None

    def is_vazia(self):
        return self.inicio is None

    def push(self, dado):
        novo_no = No(dado)
        if self.is_vazia():
            self.inicio = novo_no
        else:
            novo_no.prox = self.inicio
            self.inicio = novo_no

    def pop(self):
        if self.is_vazia():
            return None
        r = self.inicio
        self.inicio = self.inicio.prox
        return r.dado


n_expressoes = int(input())
caracteres = {")":"(", "]":"[", "}":"{"}
for _ in range(n_expressoes):
    pilha = Pilha()
    exp = input()
    for token in exp:
        if token in caracteres.values():
            pilha.push(token)
        else:
            token_pilha = pilha.pop()
            if caracteres[token] != token_pilha:
                print("N")
                break
    if pilha.is_vazia():
        print("S")
