"""Lista Encadeada Simples: A inserção e a remoção de elementos em uma lista encadeada são mais simples, pois você pode simplesmente ajustar as referências dos nós para inserir ou remover elementos em qualquer posição sem a necessidade de deslocamento de dados.
"""
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeadaSimples:
    def __init__(self):
        self.inicio = None

    def inserir(self, valor):
        novo_no = No(valor)
        if self.inicio is None:
            self.inicio = novo_no
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no

    def remover(self, valor):
        if self.inicio is None:
            print("A lista está vazia.")
            return

        if self.inicio.valor == valor:
            self.inicio = self.inicio.proximo
            return

        atual = self.inicio
        anterior = None

        while atual is not None:
            if atual.valor == valor:
                anterior.proximo = atual.proximo
                return
            anterior = atual
            atual = atual.proximo

        print(f"Elemento {valor} não encontrado na lista.")

    def pesquisar(self, valor):
        atual = self.inicio
        posicao = 0

        while atual is not None:
            if atual.valor == valor:
                print(f"Elemento {valor} encontrado na posição {posicao}.")
                return
            atual = atual.proximo
            posicao += 1

        print(f"Elemento {valor} não encontrado na lista.")

    def alterar(self, valor_antigo, valor_novo):
        atual = self.inicio

        while atual is not None:
            if atual.valor == valor_antigo:
                atual.valor = valor_novo
                print(f"Elemento {valor_antigo} alterado para {valor_novo} com sucesso.")
                return
            atual = atual.proximo

        print(f"Elemento {valor_antigo} não encontrado na lista.")

    def listar(self):
        atual = self.inicio
        print("Elementos na lista:")
        while atual is not None:
            print(atual.valor, end=" ")
            atual = atual.proximo
        print()


# Exemplo de uso:
lista = ListaEncadeadaSimples()

while True:
    print("\nOpções:")
    print("1. Inserir")
    print("2. Remover")
    print("3. Pesquisar")
    print("4. Alterar")
    print("5. Listar")
    print("6. Sair")
    
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        valor = int(input("Digite o valor a ser inserido: "))
        lista.inserir(valor)
    elif opcao == 2:
        valor = int(input("Digite o valor a ser removido: "))
        lista.remover(valor)
    elif opcao == 3:
        valor = int(input("Digite o valor a ser pesquisado: "))
        lista.pesquisar(valor)
    elif opcao == 4:
        valor_antigo = int(input("Digite o valor antigo: "))
        valor_novo = int(input("Digite o novo valor: "))
        lista.alterar(valor_antigo, valor_novo)
    elif opcao == 5:
        lista.listar()
    elif opcao == 6:
        break
    else:
        print("Opção inválida. Tente novamente.")
