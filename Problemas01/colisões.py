def colisao(entrada1,entrada2):
     #analisando eixo X e eixo y
    if entrada2[0] > entrada1[2] or entrada2[2] < entrada1[0] or entrada2[1] > entrada1[3] or entrada2[3] < entrada1[1]:
        return 0

    else:
        return 1



if __name__== "__main__":
    entrada1 = [int(x) for x in input().split()]
    entrada2 = [int(x) for x in input().split()]

    print(colisao(entrada1,entrada2))