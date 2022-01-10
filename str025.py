#Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = input('Digite o nome da pessoa: ')
maisc = nome.upper()
fnome = int(maisc.find('SILVA'))
nome = nome.strip()
espaco = nome.find(' ')
if fnome == -1:
    print('{} não tem Silva no nome'.format(nome[:espaco].capitalize()))
else:
    print('{} tem Silva no nome'.format(nome[:espaco].capitalize()))

print ('Silva?' in nome)
#outro modo sem usar o if