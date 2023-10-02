def colheita(L,C,M,N, campo):
    max_flores = 0
    
    for i in range(L - M + 1): #itera sobre as linhas da matriz
        for j in range(C - N + 1 ): #itera sobre as colunas da matriz
            
            total_flores = 0
            for x in range(i , i + M):  #itera sobre as linhas da submatriz
                for y in range(j , j + N): #itera sobre as colunas da submatriz
                    total_flores += campo[x][y]

            max_flores = max(max_flores,total_flores)
    
    return max_flores



#entradas
L,C, M,N = map(int, input().split()) #linhas/coluna/ linha lote/coluna lote
campo = []

for i in range(L):
    flores = list(map(int, input().split()))
    campo.append(flores)

#chama def e encontra max
resultado = colheita(L,C,M,N, campo)

#impressão
print(resultado)