#entradas
n = int(input())
tamanhos = list(map(int, input().split()))
estoque = 0

#itera n vezes
for i in range(n):
    estoque += tamanhos[i] - 1

#impressão
print(estoque)


