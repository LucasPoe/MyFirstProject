from datetime import datetime
import random 

print('------Bem-vindo--------')
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
data_de_registro = datetime.now()
cartoes = ['R$50,00','R$250,00','R$120,00' ]
cartao_funcionario = (random.choice(cartoes))

data_de_nascimento = datetime.strptime(input("Data de nascimento no formato dd/mm/aaaa: "),'%d/%m/%Y')

#Mensagem de boas vindas

print(F'Olá" {nome}, seu registro foi concluído com sucesso no dia {data_de_registro.day}/{data_de_registro.month}/{data_de_registro.year}. \n Parabéns, houve um sorteio e você ganhou um cartão no valor de {cartao_funcionario}')

#obs - Atentar-se a strings dinamicas, datetime.now separado









