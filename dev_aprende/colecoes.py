''' #Lista
precos = [10,20,30,100]
        #  0 1  2
print(precos[2]) #acessando por indice

#Encontrando os valores sem precisar do indice
print(precos[precos.index(100)])

# Lista aceita qualquer dado
itens = [1,2,3,'ola',True,1.0]

#Maneiras diferentes de gerar uma lista 
#Multiplicação de valores(repetição)

lista_de_noves = [9] * 10

#Usando gerador range(sequencia)
faixa = list(range(30))
print(faixa)

#Gerar a partir de String
print(list('Olá'))

#lista de lista (matriz)
matriz_de_nome = [['Carol',30],['Marcus',50]]
print(matriz_de_nome[0])
print(matriz_de_nome[0][0])
 '''

#desafio 1
''' itens = ['pc','livros','café' ]
print(f'{itens}')

#desafio 2
lista = list(range(1, 132))
print(lista)

#desafio 3 
print(lista, itens)

#desafio 4
matriz = [['pc',500],['livro', 30],['cafe', 10] ]
print(matriz)
 '''

''' # Adicionando valores ao final 
valores = [1,2,3,4,5]
anos = [2020,2030,2040]
valores.append(11) #Adicionado (append)
print(valores) 

#Unir lista
valores.extend(anos) #extend - pega lista e coloca em outra
print(valores)

# Adiciomar lista
nova_lista = valores + anos 
print(nova_lista)

# inserir um novo com base no indice
anos.insert(2, 2031 ) # indice/novo valor 
print(anos )

#Extrai com base no indice - pop - retorna um valor
anos_2020 = anos.pop(0)
''' 
''' print(anos_2020)

# Remover item da lista com base no valor, e não no indice
anos.remove(2040)
# Remover item da lista com base no indice, e não no valor
del anos [2] #[2:6] excluir uma faixa de valor

# contando a ocorrencia de uma valor 
(valores.count(2)) # Quantas vezes esse valor aparece

#Resetar - excluir as listas 
valores.clear()
 '''

# Ordenar listas 

''' valores = [2,34,82,46,84,843,816,81,8,32,8,48]
valores.sort() # Ordena os valores de forma crescente
valores.sort(reverse = True) # Ordena os valores de forma descrecente
valores.reverse() # Ordena os valores do final para o começo 
print(valores )

 '''

''' 
# Processando múltiplas listas c/ função ZIP
a_lista = ['A','B','C','D','E']
b_lista = [1,2,3,4,5]

for a_lista,b_lista in zip(a_lista,b_lista): # pegando listas diferentes e unir essas informações 
  print(a_lista)
  print(b_lista)

from itertools import zip_longest 
#Zip_longest faz o for passar por todos os valores e aprensenta mesmo que sem valor 
titulo = ['t1','t2','t3','t4','t5']
descricao = [1,2,3]
for titulo,descricao in zip_longest(titulo, descricao):
  print(F'{titulo } {descricao}')


 '''
''' from itertools import zip_longest

produtos = ['P1', 'P2','P3','P4','P5']
precos = ['500', '1500','2700','5000']
for produtos, precos in zip_longest(produtos,precos):
  print(F'Produto {produtos} encontrados {precos}')



 '''
''' 
# Dicionários 
# Criação, há duas maneiras 
# chaves {chave,valor}
pessoa = {'nome':'Carol','idade':18, 'altura':1.80}
# outra maneira 
pessoa1 = dict(nome='Carol', idade=18, altura=1.80)
print(pessoa1)
# Acessar uma propriedade
pessoa1 ['idade']
pessoa.keys() # Todas as chaves disponiveis para o dicioario
pessoa.values() # Acessa os valores que estão no dicionario
pessoa.items() # Contenta tanto a chave quanto o valor 
# iterar sobre um dicionario
for item in pessoa.items():
  print(item[1]) '''

''' # Tuplas 
#Criação 
sites = ('facebool')
valores =(20,50)
# Acessando por indice
print(sites[1])
# União de tupla
dados = sites + valores 
# Tipo dinamico
 '''

''' # Arrays
from array import array 
numeros = array('i',[1,2,3,4,5])
numeros.appende(10)
numeros.insert(5,200)
numeros.pop(1)
numeros.remove(5)
del numeros[1]
 '''
''' 
# Range (geradores )
for numero in range (10, 30 ,2):
  print(numero)
# Criar listas rapidamente 
resultado = list(range(0,201, 10))
print(resultado)
 '''

''' frutas = ['Maça','Laranja','Morango','Limão']

for indice, frutas in enumerate(frutas, 0):
  print(indice, frutas)
  if indice == 3:
    print(F'Número {indice} fruta {frutas} em promoção'  )

 '''

''' # Ordenando coleçoes (dicionario) atraves de propriedade
#Desafio 1
produtos = [
  {'nome': 'Celular',
    'preco': 1500
  },
  {'nome': 'Monitor',
    'preco': 500
  },
  {'nome': 'Microfone',
    'preco': 300
  }
] 

produtos.sort(key=itemgetter('preco'))
print(produtos) '''
''' 
#Desafio 2
from operator import itemgetter
equipamento = [('Tripé',300),('Câmera',1700), ('Iluminação',200)]

equipamento.sort(key=itemgetter(1), reverse=True)
print(equipamento)

#Desafio 3 
cotacao = [['usd',5.25],['brl', 1.56], ['eur',6.47]]

cotacao.sort(key=itemgetter(1)) 
print(cotacao)
 '''

# Filter 
# Desafio
vagas = [
  ['vaga 1', 1200],
  ['vaga 2', 2550],
  ['vaga 3', 5000]
]

def vagas_2500 (salario):
  if vagas[1] > 2500:
    return True
  else:
    return False

print(list(filter(vagas_2500,vagas)))
print(list(map(vagas_2500,vagas)))







































































