def ordenar(lista):
  
  #Ordena a lista de forma crescente 


  for i in range(len(lista) - 1):
    for j in range(i + 1, len(lista)):
      if lista[i] > lista[j]:
        lista[i], lista[j] = lista[j], lista[i]

  return lista[1]




lista = []
entrada01 = int(input())
lista.append(entrada01)

entrada02 = int(input())
lista.append(entrada02)

entrada03 = int(input())
lista.append(entrada03)

print(ordenar(lista))