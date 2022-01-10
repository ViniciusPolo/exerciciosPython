#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.
nome = input('Digite seu Nome completo: ')
print('Em maiusculas: ',nome.upper())
print('Em minusculas: ',nome.lower())
letras = len(nome)
espacos = nome.count(' ')
qsespacos = letras - espacos
print('O nome tem {} letras'.format(qsespacos))
fimprimeiro=nome.find(' ')
print('O primeiro nome {} tem {} letras'.format(nome[:fimprimeiro],fimprimeiro))