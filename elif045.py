# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep
print('Vamos jogar Jokenpo!')
player1 = input('''[ pedra ]
[ papel ]
[ tesoura ]\n''').lower()
jokenpo = ['pedra', 'papel', 'tesoura']
escolha = random.choice(jokenpo)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if player1 == escolha:
    print('Computador: {} x Player 1: {}.\nEMPATOU'.format(escolha, str(player1)))
elif player1=='pedra' and escolha=='tesoura':
    print('Computador: {} x Player 1: {}.\n=-=-=-=-=-=-=\nVOCÊ VENCEU!\n=-=-=-=-=-=-=\n'.format(escolha, str(player1)))
elif player1=='papel' and escolha=='pedra':
    print('Computador: {} x Player 1: {}.\n=-=-=-=-=-=-=\nVOCÊ VENCEU!\n=-=-=-=-=-=-=\n'.format(escolha, str(player1)))
elif player1=='tesoura' and escolha=='papel':
    print('Computador: {} x Player 1: {}.\n=-=-=-=-=-=-=\nVOCÊ VENCEU!\n=-=-=-=-=-=-=\n'.format(escolha, str(player1)))
else:
    print('Computador: {} x Player 1: {}.\n=-=-=-=-=-=-=\nVOCÊ VENCEU!\n=-=-=-=-=-=-=\n'.format(escolha, str(player1)))



