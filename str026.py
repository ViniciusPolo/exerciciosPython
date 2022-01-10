#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input('Digite um frase: ').lower().strip()
a = frase.count('a')
p = frase.find('a')
u = frase.rfind('a')
print('A letra "A" aparece {} vezes pela primeira vez na posição {} e pela ultima na posição {}.'.format(a,p,u))