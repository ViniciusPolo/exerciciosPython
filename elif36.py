#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o valor da salário: R$ '))
tempo = int(input('Em quantos anos será realizado o pagamento: '))
prestacao = (casa/tempo)/12
if prestacao<=(salario*0.3):
    print('A prestação será de R${:.2f}. Seu financiamento foi aprovado!'.format(prestacao))
else:
    print('Infelizmente não conseguiremos aprovar seu financiamento, a prestação de R${:.2f} excede 30% do seu salário.'.format(prestacao))