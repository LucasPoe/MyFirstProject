# idades do individuo - int
# soma as idades que entrarem(ate chegar no negativo), calcular a média dessas idades
# entrada negativa, encerrar o programa 
# calculo das idade, e a media 

idade = int(input ("Digite as idades: ")) #recebe idade 
numero_de_entrada = 0 # Número de quantas entrada, para calcular com a média
soma = 0 # variavel cumulativa de idade 
if(idade > 0):# condição 
  while (idade > 0): # condição para repetir
    soma = soma + idade # idade se acumulando na variavel soma 
    idade = int(input ("Digite as idades: ")) # idade sendo rescrita 
    numero_de_entrada = numero_de_entrada + 1 # numero de entrada sendo incrementado 
    media = float(soma/numero_de_entrada) # calculo da média 
  print(media)
else:
  print("Impossivel calcular")

  