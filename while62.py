# Exercício Python 62:
# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

p = int(input('Qual é o primeiro termo da PA: '))
r = int(input('Qual será a razão: '))
n = 0
j = 1
i = 10
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while n < total:
        print(f'{p}', end=', ')
        p += r
        n += 1
    print('Pausa')
    mais = int(input('Deseja aumentar os valores? '))