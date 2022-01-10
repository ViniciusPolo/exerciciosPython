#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = input('Digite o nome da pessoa: ').lower().title().strip()
p = nome.find(' ')
u = nome.rfind(' ')
print('O nome da pessoa mais curso é {}{}.'.format(nome[:p],nome[u:]))
#poderia usar o split, ai cada palavra seria uma posição