#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input("Digite o ano, digite 0 para o ano atual: "))
if ano==0:
    ano = date.today().year
bi = 'é bissexto' if ano%4==0 and ano%100!=0 or ano%400==0 else 'não é bissexto'
print('O ano {}'.format(bi))

