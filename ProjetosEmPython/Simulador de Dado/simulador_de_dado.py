# Simulador de dado
# Simular o uso de um dado, gerando um valor de 1 até 6

import random  # Importando uma modulo que gera valores aléatorios 
import PySimpleGUI

class simuladorDeDado: # Declarando a class
    def __init__(self):     #Comportamento inicial da class
      self.valor_minimo = 1 
      self.valor_maximo = 6
      self.mensagem = 'Você gostaria de gerar um novo valor?'
      # Layout 
      layout = [
        [sg.Text('Jogar o dado?')],
        [sg.Button('sim'), sg.Button('Não')] #Mensagem - sim ou não 
      ]

    def iniciar(self): 
        # Criar uma janela 
      self.janela = sg.Window('Simulador de Dado', Layout=layout) #Janela 
        # Ler os valores da tela 
      self.eventos, self.valores = janela.Read()
        # Fazer alguma coisa com esses valores
        
      while True:
            try: #Tratamento de exeção 
              self.eventos == 'sim':
              if resposta == 'sim' or resposta == 's'
                  self.GerarValorDoDado()
              elif resposta == 'não' or resposta == 'n'
                  print('Obrigado')
              else: 
                  print('Favor digitar sim ou não')
            exception:
                print('Ocorreu um erro')

  
  def GerarValorDoDado(self): 
    print(random.randit(self.valor_minimo, self. valor_maximo))



simulador = SimuladorDeDado() #Instanciando a class
simulador.iniciar()           #Chamando método
