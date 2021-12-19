# Classe = É um tipo estruturado que pode conter (membros)
# Atributo (dados/campos) membro
# Métodos (funções/operações) membro

# Definir uma classe 

class Cubo: #cabeçalho da classe / Letra maiuscula PascalCase
  ''' Docstring (recomendado)'''
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
