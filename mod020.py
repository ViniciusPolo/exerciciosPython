#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
n1 = str(input('Escreva o nome de um aluno: '))
#str é padrão, não precisa colocar, os outros precisa declarar
n2 = input('Escreva o nome de outro aluno: ')
n3 = input('Escreva o nome de mais um aluno: ')
n4 = input('Escreva mais um nome: ')
lista = [n1, n2, n3, n4]
#A lista precisa estar entre colchetes
shuffle(lista)
print('A ordem de apresentação será: ', lista)
