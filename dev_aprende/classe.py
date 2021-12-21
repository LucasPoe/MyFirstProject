''' # Classe = É um tipo estruturado que pode conter (membros)
# Atributo (dados/campos) membro
# Métodos (funções/operações) membro

# Definir uma classe 

class Cubo: #cabeçalho da classe / Letra maiuscula PascalCase
   Docstring (recomendado)
  # dado de classe compartilhado (Atributo da classe)
  def __init__ (self, valor): #Método constutor da classe 
    self.x = valor
    print('Objeto criado! ')

  def calcula_cubo (self): #Método geral 
    cubo = self.x * self.x * self.x # dado de instancia ('self')
    return 'Cubo calculado: ' + str(cubo)
  
teste = Cubo(520)
c = teste.calcular_cubo()
print(c)
  '''
''' # Método construtor 
# Sintaxe - 
# def __init__(self,[parâmetros]) 
  # código do método construtor # Self - referencia ao objeto
class Gato:
  def __init__ (self, nome):
    self.nome = nome
    print('Um gato é um animal', self.nome )

nome_gato = input('Digite o nome de seu gato: ')
g1 ='''  
''' Gato(nome_gato)

class Cliente: # Nome da classe
  padrao = 'filme' #Variavel da classes fixa, Não precisa instancia para acessar ]
  # variaveis de classe
  def __init__(self, nome, email, plano): # Iniciando uma classe com atributos 
    self.nome = nome #Self significa ele mesmo(classe)
    self.email = email
    self.plano = plano

nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
plano = input("Digite seu Plano: ")


cliente1 = Cliente(nome, email, plano)
print(Cliente.nome)

print(nome, email, plano) '''

#Herança 
class Pessoa:
  def __init__(self,nome,idade):
    self.nome = nome
    self.idade = idade

  def mostrar_nome(self):
    print(self.nome)

  def mostrar_idade(self):
    print(self.idade)  

class Estudante (Pessoa): #Classe estudante herdando Pessoa atraves dos parenteses 
  def __init__ (self, nome, idade, mat):
    Pessoa.__init__ (self, nome, idade) # Chamando o constutor da super classe 
    self.mat = mat

  def mostrar_mat (self):
    print(self.mat)

p = Pessoa ('Marcos', 30) # instanciando 
p.mostrar_idade() # entrando em Pessoa na função mostrar 
s = Estudante ('pedro', 20, 1000) # Instanciando - criando 
s.mostrar_nome() # Mostando a função
s.mostrar_mat()
s.mostrar_idade()





















