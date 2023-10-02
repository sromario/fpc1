"""Lista Estática: Em uma lista estática, os elementos são armazenados em um espaço de memória contíguo e pré-alocado com um tamanho fixo. Isso significa que a lista tem um tamanho máximo definido no momento da criação e não pode crescer além desse limite. Se a lista estiver cheia, não é possível adicionar mais elementos a menos que alguns sejam removidos."""


class ListaEstatica:
    def __init__(self):
        self.lista = [None] * 10  # Inicializa uma lista com 10 elementos vazios

    def inserir(self, valor):
        for i in range(len(self.lista)):
            if self.lista[i] is None:
                self.lista[i] = valor
                return
        print("A lista está cheia. Não é possível inserir mais elementos.")

    def remover(self, valor):
        if valor in self.lista:
            self.lista.remove(valor)
            self.lista.append(None)
            print(f"Elemento {valor} removido com sucesso.")
        else:
            print(f"Elemento {valor} não encontrado na lista.")

    def pesquisar(self, valor):
        if valor in self.lista:
            print(f"Elemento {valor} encontrado na posição {self.lista.index(valor)}.")
        else:
            print(f"Elemento {valor} não encontrado na lista.")

    def alterar(self, valor_antigo, valor_novo):
        if valor_antigo in self.lista:
            index = self.lista.index(valor_antigo)
            self.lista[index] = valor_novo
            print(f"Elemento {valor_antigo} alterado para {valor_novo} com sucesso.")
        else:
            print(f"Elemento {valor_antigo} não encontrado na lista.")

    def listar(self):
        print("Elementos na lista:")
        for item in self.lista:
            if item is not None:
                print(item, end=" ")
        print()


# Exemplo de uso com entrada do usuário:
lista = ListaEstatica()

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
