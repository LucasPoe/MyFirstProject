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
# Método construtor 
# Sintaxe - 
# def __init__(self,[parâmetros]) 
  # código do método construtor # Self - referencia ao objeto
class Gato:
  def __init__ (self, nome):
    self.nome = nome
    print('Um gato é um animal', self.nome )

nome_gato = input('Digite o nome de seu gato: ')
g1 = Gato(nome_gato)