"""
O Tio de Juvenal, Roberval, quer financiar um carro. Juvenal está dizendo para ele que
financiamentos colocam a corda no pescoço de todos e que ele deveria economizar para comprar o
carro à vista. Então, como Roberval é uma pessoa pragmática, ele pediu para seu sobrinho mostrar
os cálculos de quanto ele vai ter que pagar, de fato, pelo futuro carro. No entanto, Juvenal está com
um problema: ele não tem calculadora e seu computador está com o processador quebrado. Mais
especificamente, a Unidade Lógico Aritmética (ULA) do processador está executando apenas a
operação “+1”, também conhecida como sucessor. Juvenal está desesperado, pois precisa realizar
operações mais elaboradas para calcular os juros e não permitir que seu tio faça uma grande besteira
financiando aquele carro. Juvenal então decidiu pedir sua ajudar para elaborar um programa de
computador que realize as operações de sucessor, soma, multiplicação e exponenciação que seja
executado em seu computador defeituoso.
Tarefa
Implemente um programa que implemente as operações de soma, multiplicação e exponenciação
usando apenas a operação de sucessor.
Entrada
A entrada deverá ser lida do teclado e consiste de várias operações. Cada linha representa uma
operação. Cada operação pode ser escrita em uma das seguintes maneiras.
Sucessor, onde A é um número inteiro >= 0:
Suc A
Soma, onde A, B são números inteiros >= 0:
Soma A B
Multiplicação, onde A, B são números inteiros >= 0
Mult A B
Exponenciação, onde A, B são números inteiros >= 0
Exp A B
Saída
Escreva em cada linha da saída o resultado da operação correspondente"""

def sucessor(x):
    return x + 1

def soma(a, b):
    for _ in range(b):
        a = sucessor(a)
    return a

def multiplicacao(a, b):
    result = 0
    for _ in range(b):
        result = soma(result, a)
    return result

def exponenciacao(a, b):
    if b == 0:
        return 1
    result = 1
    for _ in range(b):
        result = multiplicacao(result, a)
    return result

while True:
  try:  
    entrada = input().split()
   
    if entrada[0] == "Suc":
        a = int(entrada[1])
        resultado = sucessor(a)
    elif entrada[0] == "Soma":
        a = int(entrada[1])
        b = int(entrada[2])
        resultado = soma(a, b)
    elif entrada[0] == "Mult":
        a = int(entrada[1])
        b = int(entrada[2])
        resultado = multiplicacao(a, b)
    elif entrada[0] == "Exp":
        a = int(entrada[1])
        b = int(entrada[2])
        resultado = exponenciacao(a, b)
    else:
        break
    print(resultado)

  except EOFError:
    break    
    
