def obter_plano(plano):
    if plano == 'premium':
        return 5
    elif plano == 'diamante':
        return 4
    elif plano == 'ouro':
        return 3
    elif plano == 'prata':
        return 2
    elif plano == 'bronze':
      return 1
    elif plano == 'resto':
        return 0

def heappify(a,N,i):
    maior = i
    l = 2*i + 1 #filho esquerdo
    r = 2*i + 2 #filho direito


    if l < N:
        if a[l][1] < a[maior][1]:
            maior = l
        elif a[l][1] == a[maior][1]:
            if a[l][2] < a[maior][2]:
                maior = l
            elif a[l][2] == a[maior][2]:
                if a[l][0] > a[maior][0]:
                    maior = l

    if r < N:
        if a[r][1] < a[maior][1]:
            maior = r
        elif a[r][1] == a[maior][1]:
            if a[r][2] < a[maior][2]:
                maior = r
            elif a[r][2] == a[maior][2]:
                if a[r][0] > a[maior][0]:
                    maior = r

 
 
    if  maior != i:
        a[i], a[maior] = a[maior], a[i] 
        heappify(a,N, maior)
    
def heapsort(a):
    n = len(a)

    for i in range(n // 2 - 1, -1, -1):
        heappify(a, n, i)

    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heappify(a, i, 0)


quantidade = int(input())
lista = []
for _ in range(quantidade):
    paciente, plano, gravidade = input().split()
    gravidade = int(gravidade)
    lista.append((paciente, obter_plano(plano), gravidade))


heapsort(lista)
for paciente in lista:
    print(paciente[0])