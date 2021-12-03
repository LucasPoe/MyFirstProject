#1- numero inteiro 
#2- identificar se o numero é impar ou par
#3- numeros float
#4- imprimir o numero - par ou impar
#5- 
#	receber numero 

numero = int(input("Digite o número: "))

num = numero % 2 

if (num == 0):
  print("Número par")
else:
  print("Número impar")