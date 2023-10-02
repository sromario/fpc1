class PilhaCartas:
    def __init__(self):
        self.cartas = []

    def esta_vazia(self):
        return len(self.cartas) == 0

    def empilhar(self, carta):
        self.cartas.append(carta)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.cartas.pop()
        else:
            print("A pilha de cartas está vazia. Não é possível desempilhar.")

    def topo(self):
        if not self.esta_vazia():
            return self.cartas[-1]
        else:
            print("A pilha de cartas está vazia. Não há topo.")

    def tamanho(self):
        return len(self.cartas)

# Função para exibir o menu de opções
def exibir_menu():
    print("Escolha uma opção:")
    print("1. Empilhar carta")
    print("2. Desempilhar carta")
    print("3. Exibir carta no topo")
    print("4. Tamanho da pilha")
    print("5. Sair")

# Exemplo de uso da PilhaCartas com entrada do usuário
pilha = PilhaCartas()

while True:
    exibir_menu()
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        carta = input("Digite a carta que deseja empilhar: ")
        pilha.empilhar(carta)
        print(f"{carta} foi empilhada.")
    elif opcao == "2":
        carta_desempilhada = pilha.desempilhar()
        if carta_desempilhada:
            print(f"{carta_desempilhada} foi desempilhada.")
    elif opcao == "3":
        carta_topo = pilha.topo()
        if carta_topo:
            print(f"Carta no topo da pilha: {carta_topo}")
    elif opcao == "4":
        tamanho_pilha = pilha.tamanho()
        print(f"Tamanho da pilha: {tamanho_pilha}")
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")
