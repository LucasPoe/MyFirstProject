# 2 valores inteiros - X e Y 
# Comparar se X e Y são crescentes ou descrescentes e se forem iguais, encerrar 
# Numeros precisam ser int 
# mostrar a ordem descrescente crescente
# x = input
# y = input 
# while (x > y and x != y )
#   print (descrescente )
#  
#
#
#

x = int(input("Digite o número x:" )) # Entrada de valores 
y = int(input("Digite o número y:" )) # Entrada de valores 

while (x != y): # Aqui basta os números serem diferentes para que a condição seja atendida -
  if (x < y): # Testando a condição
    print("crescente") # Aprensenta o resultado 
  else: 
    print("decrescente") 
  x = int(input("Digite o número x:" )) # Importante adicionar novamente a variavel, para que não se entre em um loop 
  y = int(input("Digite o número y:" )) #







