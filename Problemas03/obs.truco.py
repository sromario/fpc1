# Valores das cartas
def calcular_pontuacao(carta):
    valor_pontuacao = [4, 5, 6, 7, 12, 11, 13, 1, 2, 3]
    return valor_pontuacao[carta]

# Função para determinar o vencedor de uma rodada
def vencedor_rodada(carta_adalberto, carta_bernardete):
    if carta_adalberto > carta_bernardete:
        return 'A'
    elif carta_bernardete > carta_adalberto:
        return 'B'
    else:
        return 'A'

# Número de partidas
N = int(input())

# Contadores de vitória
vitorias_adalberto = 0
vitorias_bernardete = 0

# Processar cada partida
for _ in range(N):
    cartas = [int(x) for x in input().split()]

    # Determinar o vencedor de cada rodada
    vencedor_rodada1 = vencedor_rodada(cartas[0], cartas[3])
    vencedor_rodada2 = vencedor_rodada(cartas[1], cartas[4])
    vencedor_rodada3 = vencedor_rodada(cartas[2], cartas[5])

    # Contar vitórias de Adalberto e Bernardete
    if vencedor_rodada1 == 'A' or vencedor_rodada2 == 'A' or vencedor_rodada3 == 'A':
        vitorias_adalberto += 1
    else:
        vitorias_bernardete += 1

# Imprimir resultados
print(vitorias_adalberto, vitorias_bernardete)
