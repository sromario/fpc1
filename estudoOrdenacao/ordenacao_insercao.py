#ordena uma lista por inserção
def ordenacao(lista):
    for i in range(1,len(lista)):
        elemento = lista[i]
        j = i - 1

        while j>= 0 and lista[j] > elemento:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = elemento

testeLista = [int(x) for x in input().split()]
ordenacao(testeLista)
print(testeLista)