# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

n = randint(1,10)
palpite = int(0)
escolha = int(input('Escolha um numero entre 1 e 10: '))

while n != escolha:
    print('Numero errado!')
    palpite +=1
    escolha = int(input('Escolha outro numero entre 1 e 10: '))
    print('Carregando')
    sleep(2)
print(f'Você acertou!!!!!\nCom {palpite} tentativas')    
