#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
r = float(input('Quantos reais você tem: R$ '))
d = float(r / 5.75)
print('Com R$ {:.2f} você pode tem o equivalente a US$ {:.2f}'.format(r, d))