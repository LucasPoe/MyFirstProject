num1 = int(input ("Digite o número 1: "))
num2 = int(input ("Digite o número 2: "))
num3 = int(input ("Digite o número 3: "))

if (num1 < num2 and num1 < num3 and num2 < num3): # Unico erro foi o "Anan num2 < num3" ou seja, a verificacão do num2 para o num3 
  print(num1,num2,num3)
else: 
    print("não está crescente")

  