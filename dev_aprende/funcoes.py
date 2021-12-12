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
''' def gerar_objeto_personalizado(cor,*,altura,formato): print(cor,altura,formato)

gerar_objeto_personalizado ('azul',altura=1.7, formato='quadrado' )
 '''
# Args - argumentos cuja valores, são varios, isto é caso precisa passar varios valores, ultilizar o '*' - Quantidade ilimitada de argumentos posicionais 
''' def somar (*valores, b):
    print(valores)
    for valor in valores:
      b = b + valor
    print(b)
somar (10,20,5, b=5) '''

# Kwargs são os arguemtos ilimiatados, para os nomeados "**"
# Quando não sabe a quantidade de argumentos que estará recebendo - nomeados ou posicionais 

''' def fazer_calculo(nome,*args,**kwargs):
  print(nome)
  print(args)
  print(kwargs)
  for arg in args:
    print(args)
  for kwarg in kwargs.values():
    print(kwarg)
fazer_calculo('Jeff',4,6,3,7,a=1,b=2,c=3)

 '''
# 1- De nomes sigficativo - nome da função, intenção 
# 2- Funções pequenas que fazem apenas uma coisa
# 3- Quanto menor a quantidade de argumentos, melhor - Max 3 Argumentos 
# 4- Use funções para organizar seu código e economizar linha de código(DRY) Não se repita - Rotina 

















