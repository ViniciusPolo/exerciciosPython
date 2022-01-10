#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de descent
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros
produto = float(input('Qual é o valor do produto: '))
pag = int(input('''Entre com a condição de pagamento
[ 1 ] À vista dinheiro/cheque: 10% de desconto
[ 2 ] À vista no cartão: 5% de desconto
[ 3 ] em até 2x no cartão: preço formal 
[ 4 ] 3x ou mais no cartão: 20% de juros\n'''))
if pag==1:
    print('O valor do produto será R$ {:.2f}'.format(produto*0.9))
elif pag==2:
    print('O valor do produto será R$ {:.2f}'.format(produto*0.95))
elif pag==3:
    print('O valor do produto será em duas vezes de R$ {}'.format(produto/2))
else:
    print('O valor do produto será R$ {:.2f}'.format(produto * 1.2))