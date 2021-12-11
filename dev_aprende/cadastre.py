from datetime import datetime # importando biblioteca
import random # # importando biblioteca

print('------Bem-vindo--------')
nome = input("Digite seu nome: ") # criando variavel 
idade = int(input("Digite sua idade: ")) # criando variavel 
data_de_registro = datetime.now() # # criando variavel que recebe data 
cartoes = ['R$50,00','R$250,00','R$120,00' ] # criando lista/coleção 
cartao_funcionario = (random.choice(cartoes)) # atribuindo um valor aleatorio a um funcionario

data_de_nascimento = datetime.strptime(input("Data de nascimento no formato dd/mm/aaaa: "),'%d/%m/%Y') # pedindo data de aniversario para o funcionario ultilizando datetime e guardando  

#Mensagem de boas vindas

print(F'Olá {nome}, seu registro foi concluído com sucesso no dia {data_de_registro.day}/{data_de_registro.month}/{data_de_registro.year}. \n Parabéns, houve um sorteio e você ganhou um cartão no valor de {cartao_funcionario}') # ultilizando string dinamica

#obs - Atentar-se a strings dinamicas, datetime.now separado









print(F'Ola {nome}')