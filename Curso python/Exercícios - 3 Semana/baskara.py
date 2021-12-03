# 3 dados a, b, c 
# calcular o delta, e apos isso calcula o baskara 
#  Se o delta for igual a 0 = 1 raiz, se for 0 não tera raizer reais. O programa deve rodar só raizes reais 
# calcular a raiz
# 1- entrada  2- calcular delta 3- calcular baskara 4- inserir as condicionante para averiguar qual o tipo da raiz

import math

a = float(input("Valor de A: "))
b = float(input("Valor de B: "))
c = float(input("Valor de C: "))

# Formula delta 
delta = b**2 - 4 * a * c 
print ("Valor de delta: ", delta)

if a == 0:
  print("O valor de A deve ser diferente de 0")
elif  delta < 0:
    print ("Sem raizes reais ")
else: 
# bhaskara
  x1 = (-b + math.sqrt(delta)) / (2 * a)
  x2 = (-b - math.sqrt(delta)) / (2 * a)

print("Valor de X1: ", x1)
print("Valor de X2: ", x2)

