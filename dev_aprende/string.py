''' # Aula 6 - método de strings
a = 'é'
b = 'MELHOR'
c = 'QUE'
d = 'feito'
e = 'perfeito'

print( f'{a.upper()} {b.lower()} {d.upper()} {c.lower()} {e.upper()}')

# Aula 7 - Slice - Extraindo partes de uma string 
teclado = 'Teclado'
print(teclado[2]) #referenciando cada string
print(teclado[-1]) #vai direto para a ultima string
print(teclado.index('l')) #Qual caractere voce quer buscar 
print(teclado[0:5]) # Onde começar, onde termina 
biblioteca = 'biblioteca'
print(biblioteca.index('0'))
print()
 '''
  # Aula 8 - Slit e Join 
#print(frase.split())
#- Slit = Encontra os espaços e colocar em uma lista 

# aula 10 - Números e operações matemáticas

# aula 11 - DateTime e Tempo
''' from datetime import datetime
data_aniversario = datetime.strptime(input('Data do niver'),'%d/%m/%Y')

data_atual = datetime.now() 

dias_restantes = data_aniversario - data_atual

print(dias_restantes.days) '''






#print(datetime.now()) #day , month , year 

# criar del
#data = datetime.strptime(input('Quando? '),'%d/%m/%Y') # convertendo string para data

  #aula 12 
# Valores aleatórios com random
# import random

#print (random.random()) # Gera valor aleatorio
#print (random.uniform(4,10)) # decimal
#print (random.randit(4,10)) #inteiro 

''' cores = ['verde','vermelho', 'azul']
print(random.choice(cores)) # "K=X" especifica mais de uma valor  '''
''' 
moeda = ['cara', 'coroa']
print(random.choices(moeda)) '''

''' nomes = ['lucas','carlos','jean','igor','rafael','andre']
print(random.choices(nomes, k = 1)) '''

# print(random.randint(10, 100))

#aula 13 - Atalhos 























