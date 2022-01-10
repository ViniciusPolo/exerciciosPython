#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO
nota1 = float(input('Digite a 1ºnota do aluno: '))
nota2 = float(input('Digite a 2º nota do aluno: '))
nota=(nota1+nota2)/2
if nota>=7:
    print('A média é de {} e o aluno está APROVADO!'.format(nota))
elif nota>=5 and nota<7:
    print('A média é de {} e o aluno está em RECUPERAÇÃO!'.format(nota))
else:
    print('A média é de {} e o aluno está REPROVADO!'.format(nota))

