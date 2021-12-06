x = float(input("Digite o número: ")) # Entrada de número para que possa entrar na estrutura de repetição 

soma = 0 # Essa variavel que irá calcular a soma. Ela deve começar com o valor 0 pois é um número neutro e que vai ser somada com a variavel X
while (x != 0): # A estrutura vai se repetira enquanto a condição for verdadeira
    soma = soma + x  # X vai se acumulando na variavel Soma 
    x = float(input("Digite o número: ")) # O X irá receber um novo valor, que ira retorna para a condição while para verificar se a condição é falsa ou verdadeira 
print (soma)
  