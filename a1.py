import random

valor_aleatorio = random.randint(1,10)
chute = int(input ('Chute um valor de 1 a 10: '))
acertou = False
while acertou == False:
  chute = int(input ('Chute um valor de 1 a 10: '))
  if chute > valor_aleatorio:
    print('Chute foi maior que o valor gerado')
  elif chute < valor_aleatorio:
    print('chute menor que o valor gerado')
  elif chute == valor_aleatorio:
    acertou = True
    print('você acertou!')