def maior_diferenca_cebola_azeitona(N, diferencas):
    max_diferenca = 0
    diferenca_atual = 0

    for i in range(2 * N):
        diferenca_atual += diferencas[i % N]
        if diferenca_atual < 0:
            diferenca_atual = 0
        if diferenca_atual > max_diferenca:
            max_diferenca = diferenca_atual

    return max_diferenca

# Leitura de entrada
N = int(input())
diferencas = list(map(int, input().split()))

# Encontre a maior diferença possível
resultado = maior_diferenca_cebola_azeitona(N, diferencas)

# Imprima o resultado
print(resultado)
