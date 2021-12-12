# As funções pegam funcionalidades, recebem alguns parametros, e com base do que foram passados a elas, fazem algo internamente 

#Sintaxe
''' def nome_da_funcao (parametro)
  comando '''
#Usar poucos parametros - boas praticas

#-- Exemplos da aula
''' def dar_boas_vindas_personalizado(nome):
  print(f' Boas-vindas! {nome} ')

dar_boas_vindas_personalizado('Lucas')
 '''
''' 
# Desafios 1
def gerar_nome_completo (nome, sobrenome): # Criando um função e passando os parametros (informações que vou receber)
  print(f'Boas-Vindas!{nome} {sobrenome}') # comando que vai ser executado 

gerar_nome_completo ('Lucas', 'Farias')# Chamando a função 

# Desafios 2
def calcular_valores(preco, quantidade = 1):
  total = preco * quantidade
  print (total)

calcular_valores(12)
 '''
# Processar VS Retornar 
# Funções que retornam e que processam 
# Quando usar? Precisa dessa informação na lógica? ou só preciso processar esse dado?


''' # Exemplos da aula
# Argumentos posicionais - Valores devem está nas mesmas posições 
def exibir_preco(nome_produto, preco):
    print(f'{nome_produto} está no valor de: {preco}')
exibir_preco('iphone', preco=5000  )

# Argumentos nomeados - Valores são nomeados e passado no parametro 
def exibir_preco(nome_produto, preco):
    print(f'{nome_produto} está no valor de: {preco}')
exibir_preco (nome_produto = 'iphone', preco = 5000)


 '''
def gerar_objeto_personalizado(cor,*,altura,formato): print(cor,altura,formato)

gerar_objeto_personalizado ('azul',altura=1.7, formato='quadrado' )





















