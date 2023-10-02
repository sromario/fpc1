# Função para encontrar o número máximo estimado de cajus colhidos
def max_cajus_colhidos(L, C, M, N, fazenda):
    max_cajus = 0

    # Calcula a matriz de soma acumulada
    sum_matrix = [[0] * (C + 1) for _ in range(L + 1)]

    for i in range(1, L + 1):
        for j in range(1, C + 1):
            sum_matrix[i][j] = fazenda[i - 1][j - 1] + sum_matrix[i - 1][j] + sum_matrix[i][j - 1] - sum_matrix[i - 1][j - 1]

    for i in range(L - M + 1):
        for j in range(C - N + 1):
            total_cajus = 0
            for x in range(i, i + M):
                for y in range(j, j + N):
                    total_cajus += fazenda[x][y]

            max_cajus = max(max_cajus, total_cajus)

    return max_cajus

# Leitura de entrada
L, C, M, N = map(int, input().split())
fazenda = []

for _ in range(L):
    linha = list(map(int, input().split()))
    fazenda.append(linha)

# Encontre o número máximo estimado de cajus colhidos
resultado = max_cajus_colhidos(L, C, M, N, fazenda)

# Imprima o resultado
print(resultado)
