N =int(input())
matriz = [[0] * N for _ in range(N)]

for i in range(N):
    valor = input()
    valor = valor.split()
    for j in range(N):
        matriz[i][j] = int(valor[j]) 
    
M = sum(matriz[0])
linha_errada = coluna_errada = 0

for i in range(N):
    soma_linha = sum(matriz[i])
    soma_coluna = sum(matriz[j][i] for j in range(N))
    
    if soma_linha != M:
        linha_errada = i
    
    if soma_coluna != M:
        coluna_errada = i

valor_original = matriz[linha_errada][coluna_errada]
valor_alterado = M - (sum(matriz[linha_errada]) - valor_original)


print(valor_alterado, valor_original)
    