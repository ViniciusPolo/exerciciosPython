#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
n = int(input('Digite um numero entre 0 e 9999: '))
m=n//1000%10
c=n//100%10
d=n//10%10
u=n//1%10
#print('O milhar é {}, a centena é {}, a dezena é o número {} e a unidade é representada por {}.'.format(n[0],n[1],n[2],n[3]))
print('O milhar é {}, a centena é {}, a dezena é o número {} e a unidade é representada por {}.'.format(m,c,d,u))