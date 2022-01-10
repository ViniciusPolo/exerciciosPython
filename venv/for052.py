# Faça um programa que leia um numero inteiro e defina se ele é primo ou não
num = int(input("Digite um número inteiro: "))
tot=0
for i in range(1,num+1):#expressões de multiplicação e divisão começe o for por um, zero não é divisivel nem multiplicavel
    if num % i == 0:
        print('\033[33m',end=' ')
        tot+=1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(i), end=' ')

if tot==2:
    print('\nÉ primo')
else:
    print("\nNão é primo")