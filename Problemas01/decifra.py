lista = input()
lista_2 = input()
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
resposta = ''

for letra in lista_2:
  try:
    indice = lista.index(letra)
    resposta = resposta + alfabeto[indice]
    

  except ValueError:
    resposta = resposta + letra

print(resposta)