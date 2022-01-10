#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Entre com o salário do Funcionário: R$ '))
if (sal>1250):
    print('Seu salário que era de R$ {} terá um aumento de 10% e passará a ser R$ {}'.format(sal, sal*1.1))
else:
    print('Seu salário que era de R$ {} terá um aumento de 15% e passará a ser R$ {}'.format(sal, sal*1.15))