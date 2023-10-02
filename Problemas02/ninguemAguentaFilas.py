class No():
  def __init__(self,dado=None):
    self.dado = dado
    self.prox = None
    self.ant = None

  def __str__(self):
    return str(self.dado)

class list():
  def __init__(self):
    self.inicio = None
    self.fim = None

  #Gerar a string
  def __str__(self):
    f = ""
    c = self.inicio
    while not c is None:
      if c.prox == None:
        f += "{}".format(str(c))

      else:
        f += "{} ".format(str(c))
      c = c.prox
    return f

  
  #coloca um novo elemento no final da lista
  def inserir(self, data=None):
    novo_no = No(data)
    if self.isVazia():
        self.inicio = self.fim = novo_no
    else:
        novo_no.ant = self.fim
        self.fim.prox = novo_no
        self.fim = novo_no

  #verifica se lista está vazia
  def isVazia(self):
    return self.inicio is None and self.fim is None
  
  #verifica se existe um elemento na fila
  def procurar(self, x):
    y = self.inicio
    while not y is None:
      if x == y.dado:
        break
      else:
        y = y.prox
    return y
    
  #remover um elemento da lista
  def remove(self, x):
    no_achado = self.procurar(x)
    if no_achado is not None:
      if no_achado.prox is not None:
         no_achado.prox.ant = no_achado.ant
      else:
        self.fim = no_achado.ant

      if no_achado.ant is not None:
        no_achado.ant.prox = no_achado.prox
      else:
        self.inicio = no_achado.prox
    return no_achado


# PROBLEMA #
qnt_pessoas = [int(n) for n in input().split()]
ident_pessoa = input().split()
qnt_pessoas2 = [int(m) for m in input().split()]
ident_pessoas2 = input().split()
lista_pessoas = list()
for i in ident_pessoa:
    lista_pessoas.inserir(i)
for i in ident_pessoas2:
    lista_pessoas.remove(i)
print(lista_pessoas)