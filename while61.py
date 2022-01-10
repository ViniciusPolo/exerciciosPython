#Exercício Python 61: 
# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

p = int(input('Qual é o primeiro termo da PA: '))
r = int(input('Qual será a razão: '))
n = 0
while n < 10:
    print(f'{p}', end = ', 4')
    p = p + r
    n+=1
