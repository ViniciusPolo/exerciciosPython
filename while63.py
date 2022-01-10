# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

# 0 – 1 – 1 – 2 – 3 – 5 – 8

i = int(input('Quantos elementos da sequencia de Fibonacci deseja exibir: '))
j = 0
c = 0
p = 1
while c < i:
    print(f'{j}', end=', ')
    j = j + p
    p = j - p
    c+=1
    if j == 0:
        j+=1
print('Fim')
