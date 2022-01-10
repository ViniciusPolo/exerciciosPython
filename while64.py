# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
cont = 0
tot = 0
s = 0
while s != 999:
    s = int(input('Digite um numero ou 999 para parar: '))
    if s != 999:
        tot=tot + s
        cont += 1
print(f'Foram inseridos {cont} numeros e sua soma é {tot}')
