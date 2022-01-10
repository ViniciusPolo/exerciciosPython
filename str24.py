#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
city = input('Digite o nome de uma cidade: ')
maisc = city.capitalize()
fcity = int(maisc.find('Santo'))
if fcity == -1:
    print('A cidade não tem Santo no nome')
else:
    print('A cidade tem Santo no nome')