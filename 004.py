#Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
l = input('Digite algo no teclado: ')
#print('O tipo primeito digitado é ',type(leia))
print('O valor digitado é número:', l.isnumeric())
print('O valor digitado é Maiuscula:' , l.isupper())
print('O valor digitado é minuscula: ', l.islower())
print('o valor digitado é alfanumérico: ', l.isalnum())