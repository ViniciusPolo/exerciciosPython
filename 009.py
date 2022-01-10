#Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
n = int(input('Digite um número: '))
i = int(0)
print('Sua tabuada é: ')
while i <= 10:
    print(' {} x {} = {}'.format(n, i, (n*i)))
    i += 1