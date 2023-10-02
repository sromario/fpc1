# Função para calcular o número mínimo de pastas
def min_pastas(N, B, tamanhos):
    pastas = 0  # Inicialmente, nenhum arquivo está em uma pasta
    atual_pasta = 0  # Tamanho atual da pasta
    
    # Percorrer os arquivos
    for tamanho in tamanhos:
        # Se o tamanho do arquivo for maior que o limite B, retorne -1 (impossível)
        if tamanho > B:
            return -1
        
        # Se o arquivo não couber na pasta atual, crie uma nova pasta
        if atual_pasta + tamanho > B:
            pastas += 1
            atual_pasta = 0
        
        # Adicione o arquivo à pasta atual
        atual_pasta += tamanho

    # Certifique-se de contar a última pasta, se necessário
    if atual_pasta > 0:
        pastas += 1

    return pastas

# Ler entrada
N, B = map(int, input().split())
tamanhos = list(map(int, input().split()))

# Calcular e imprimir a quantidade mínima de pastas
resultado = min_pastas(N, B, tamanhos)
print(resultado)
