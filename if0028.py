#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
n = randint(1,10)
escolha = int(input('Escolha um número: '))
print('Loading...')
sleep(3)
if(escolha == n):
    print('Parabéns você acertou')
else:
    print('Você errou, o numero sorteado foi {}'.format(n))
