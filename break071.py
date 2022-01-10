#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. 
# OBS:considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

sacado = c = v = d = u = 0
saque = int(input('Quanto deseja sacar? '))
while True:
    sacado = saque
    while saque >= 50:
        c += 1
        saque -= 50
        if saque == 0:
            break
    while saque >= 20:
        v += 1
        saque -= 20 
        if saque == 0:
            break 
    while saque >= 10:
        d += 1
        saque -= 10
        if saque == 0:
            break  
    while saque >= 1:
        u += 1
        saque -= 1 
        if saque == 0:
            break

    print(f'Saque no valor de {sacado} foi entregue \n{c} notas de $50\n{v} notas de $20,\n{d} notas de $10 e\n{u} notas de $1')
    break



