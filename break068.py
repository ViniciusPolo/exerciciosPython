#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
from random import paretovariate, randint
cont = 0
while True:
    aposta = str(input('Par ou Impar (P/I): ')).strip().upper()[0]
    if aposta in 'PI': 
        pc = randint(0, 5)
        user = int(input('Digite sua jogada: '))
        print (f'Computador {pc}, você {user}')
        res = pc + user
        if res%2 == 0:
            vit = 'P'
        else:
            vit = 'I'
        cont +=1

        if aposta != vit:
            print(f'Você perdeu! Foram {cont} jogadas')
            break
        else:
            print(f'Você Venceu')

            
    else:
        print('Escolha par ou impar: (P/I')
