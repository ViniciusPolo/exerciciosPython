#Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
n1 = str(input('Escreva o nome de um aluno: '))
n2 = input('Escreva o nome de outro aluno: ')
n3 = input('Escreva o nome de mais um aluno: ')
n4 = input('Escreva mais um nome: ')
aluno = (n1, n2, n3, n4)
print('{} por gentileza apague o quadro'.format(choice(aluno)))