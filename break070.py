#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. 
#  programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.

valor = float(0.00)
produto_1000 = cont = 0
mais_barato = ' '
while True:
    produto = input('Digite o nome do produto: ')
    preco = float(input('Informe o valor do item: '))
    continuar = ' '
    cont +=1
    if cont ==1 or preco < barato:
        mais_barato = produto
        barato = preco
    if preco >= 1000:
        produto_1000 += 1
    while continuar not in 'SN':
        continuar = input('Deseja continuar (S/N): ').strip().upper()[0]
    valor += preco
    if continuar == 'N':
        print('Programa encerrado!')
        break
print(f'A compra ficou em {valor}\n{produto_1000} produto(s) custam mais de $1000\nE o item mais barato foi {mais_barato} custando {barato}')