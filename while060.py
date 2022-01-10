#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.5 Exemplo:

#5! = 5 x 4 x 3 x 2 x 1 = 120
from math import factorial
n = int(input('Informe um numero: '))
i = factorial(n)
fat = n
while n > 1:
    print(f'{n}! = {fat}')
    fat = fat * (n-1)
    n = n-1
print(f'1! = {fat}\nO fatorial é : {fat}')


print(f'O fatorial9 calculado através da biblioteca: {i}')
