def cruzamento(n, n2):
    total_cruzamento = 0
    for i in range(n):
        for j in range(i+1, n):
            if n2[i] > n2[j]:
                total_cruzamento += 1
    return total_cruzamento


n = int(input())
n2 = [int(x) for x in input().split()]

resultado = cruzamento(n, n2)
print(resultado)