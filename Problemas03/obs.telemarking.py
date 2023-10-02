def distribuir_ligacoes(N, L, tempos):
    vendedores = [(i, 0) for i in range(1, N + 1)]
    resultado = [0] * N

    for i, tempo in enumerate(tempos):
        vendedor = min(vendedores, key=lambda x: (x[1], x[0]))
        resultado[vendedor[0] - 1] += 1
        vendedores.remove(vendedor)
        vendedores.append((vendedor[0], vendedor[1] + tempo))

    return resultado

# Leitura de entrada
N, L = map(int, input().split())
tempos = [int(input()) for _ in range(L)]

# Distribuir ligações entre os vendedores
ligacoes_por_vendedor = distribuir_ligacoes(N, L, tempos)

# Imprimir resultado
for i, ligacoes in enumerate(ligacoes_por_vendedor):
    print(i + 1, ligacoes)
