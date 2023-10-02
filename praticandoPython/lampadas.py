"""Você está de volta em seu hotel na Tailândia depois de um dia de mergulhos. O seu quarto tem
duas lâmpadas. Vamos chamá-las de A e B. No hotel há dois interruptores, que chamaremos de I1
e I2. Ao apertar I1, a lâmpada A troca de estado, ou seja, acende se estiver apagada e apaga se
estiver acesa. Se apertar I2, ambas as lâmpadas A e B trocam de estado.
As lâmpadas inicialmente estão ambas apagadas. Seu amigo resolveu bolar um desafio para você.
Ele irá apertar os interruptores em uma certa sequência, e gostaria que você respondesse o estado
final das lâmpadas A e B.
Entrada
A primeira linha contém um número N que representa quantas vezes seu amigo irá apertar algum
interruptor. Na linha seguinte seguirão N números, que pode ser 1, se o interruptor I1 foi apertado,
ou 2, se o interruptor I2 foi apertado.
Saída
Seu programa deve imprimir dois valores, em linhas separadas.
Na primeira linha, imprima 1 se a lâmpada A estiver acesa no final das operações e 0 caso contrário.
Na segunda linha, imprima 1 se a lâmpada B estiver acesa no final das operações e 0 caso contrário."""

def estado(vezes,n1):
    #lampadas A e B
    a = 0 
    b = 0
    for i in range(vezes):
        if n1[i] == 1:
            a = not a
              
        if n1[i] == 2:
            a = not a
            b = not b

    return int(a), int(b)

    

#entradas
if __name__ == "__main__":
    vezes = int(input())
    n1 = list(map(int,input().split()))
    a, b= estado(vezes,n1)
    print(a)
    print(b)
    