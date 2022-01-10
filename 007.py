#Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = float(input('Digite a nota do 1° Aluno: '))
n2 = float(input('Digite a nota do 2º Aluno: '))
m = (n1 + n2)/2
print('A média entre as notas( {:.1f} e {:.1f} ) do aluno é igual a {:.1f}'.format(n1, n2, m))
#{:.1f} - 1 casa float depois da virgula