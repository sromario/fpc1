#observação


def transporte(a, b, c):
  #ordenar caixas
  caixas = [a, b, c]
  caixas.sort()
  
  #caso base
  if not caixas:
    return 0

  # Caso recursivo: se a caixa mais pequena caber na caixa maior, então o drone pode fazer uma viagem para transportar a caixa maior.
  if a <= b:
    return 1 + transporte(b, c, caixas[1:])

  # Caso recursivo: se a caixa mais pequena não caber na caixa maior, então o número mínimo de viagens é o número mínimo de viagens para transportar as duas caixas restantes.
  else:
    return 1 + transporte(a, b, caixas[1:])


if __name__ == "__main__":
  a = int(input())
  b = int(input())
  c = int(input())
  print(transporte(a, b, c))
