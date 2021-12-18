''' 
 # Tratar erros 
 # Deixa a vida do usuario mais facil
try:
  valor = int(input('digite: '))
  print(valor * 5.25)
except:
  print('Favor digitar apenas números')
 '''
# Como reagir a um erro 
# Não deixar a exeção para o usúario - mensagem amigavel

''' # Podemos tratar varios erros usando o except
# Ultilização do Finally
try:
  meses = [1,2,3,4,5,6,7,8,9,10,11,12]
  print(meses[15])
except IndentationError as erro:
  print('Favor acessar valido')
  print(erro)
except NameError as erro:
  print('Sintaxe errada') 
finally:
  print('A operação foi encerrad')
 '''
# Ultilixando logging - Historico da aplicação 
# NIveis de logging - Gravidade do problema
# Guardar informações, criar um arquivo de problemas 
# Manter historico de erros - logging
import logging
logging.basic
logging.critical('Logging nível critical')

