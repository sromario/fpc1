def numero_de_rodadas(N, cartas):
    rodadas = 0
    proxima_carta = 1  # Próxima carta a ser encontrada

    while proxima_carta <= N:
        encontrou = False

        for i in range(len(cartas)):
            if cartas[i] == proxima_carta:
                encontrou = True
                proxima_carta += 1
                break

        if not encontrou:
            return rodadas  # Se não encontrou a próxima carta, encerra

        if proxima_carta > N:
            break

        rodadas += 1

    return rodadas

# Leitura de entrada
N = int(input())
cartas = list(map(int, input().split()))

# Encontre o número de rodadas do jogo
resultado = numero_de_rodadas(N, cartas)

# Imprima o resultado
print(resultado)
