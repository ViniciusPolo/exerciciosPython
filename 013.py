#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
sal = float(input('Digite o salário do funcionario: R$'))
aum = float(sal * 1.15)
print('O salário anterior de R$ {:.2f}, com o reajuste será de R$ {:.2f}'.format(sal, aum))