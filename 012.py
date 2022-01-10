#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Digite o valor do produto R$ '))
pdesc = p * 0.95
print('O valor do produto é R$ {:.2f} e com o desconto de 5% saíra por {:.2f}'.format (p, pdesc))