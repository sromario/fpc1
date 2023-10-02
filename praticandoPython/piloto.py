"""Uma grande fábrica de carros elétricos está realizando melhorias no sistema de piloto automático e
precisa da sua ajuda para implementar um programa que decida se um carro B, que está trafegando
no meio de dois carros A e C, precisa acelerar, desacelerar ou manter a velocidade atual. Os carros
são iguais e os sensores do piloto automático vão fornecer, como entrada, a posição atual da traseira
dos três carros. Veja um exemplo na figura.

A B C

O carro B precisa ser acelerado se a distância da sua traseira para a traseira do carro A for menor do
que a distância da sua traseira para a traseira do carro C. Se for maior, ele precisa ser desacelerado.
Se for igual, precisa manter a velocidade atual. Quer dizer, o carro B precisa ser acelerado se
(B − A) < (C − B), desacelerado se (B − A) > (C − B) e manter a velocidade se (B − A) for igual
a (C − B).
Entrada
A primeira linha da entrada contém um inteiro A. A segunda linha da entrada contém um inteiro
B. A terceira linha da entrada contém um inteiro C. Os três inteiros representam as posições atuais
das traseiras dos carros A, B e C, respectivamente.
Saída
Seu programa deve imprimir uma linha contendo um inteiro: 1 se o carro B precisa acelerar; −1 se
precisa desacelerar; ou 0 se precisa manter a velocidade atual."""

def piloto(a,b,c):
    if (b-a) < (c-b):
        return 1
    elif (b-a) > (c-b):
        return -1
    elif (b-a) == (c-b):
        return 0
    
if __name__ == "__main__":
   a = int(input())
   b = int(input())
   c = int(input())
   print(piloto(a,b,c))