# Exercício Python 46:
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, in de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
print('Contagem Regressiva: ')
for c in range(10, -1, -1):
    print('{}!'.format(c))
    sleep(1)
print('Lançar!')
