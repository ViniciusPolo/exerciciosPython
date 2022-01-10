#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

#[ 1 ] somar

#[ 2 ] multiplicar

#[ 3 ] maior

#[ 4 ] novos números

#[ 5 ] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite um numero: '))
n2 = int(input('Agora outro: '))
opcao = 0
while not opcao == 5:
    opcao = int(input('[ 1 ] somar - [ 2 ] multiplicar - [ 3 ] maior - [ 4 ] novos números - [ 5 ] sair do programa\n'))
    if opcao == 1:
        soma = n1 + n2
        print(f'Você escolheu [1] - somar\nA soma entre {n1} e {n2} = {soma}')
    elif opcao == 2:
        mult = n1 * n2
        print(f'Você escolheu [2] - multiplicar\nA multiplicação entre {n1} e {n2} = {mult}')
    elif opcao == 3:
        if n1 < n2:
            print(f'Você escolheu [3] - maior\nO maior entre entre {n1} e {n2} = {n2}')
        elif n1 > n2:
            print(f'Você escolheu [3] - maior\nO maior entre entre {n1} e {n2} = {n1}')
        else:
            print(f'Você escolheu [4] - maior\nContudo {n1} e {n2} são iguais')
    elif opcao == 4:
        n1 = int(input('Digite um outro numero: '))
        n2 = int(input('Agora digite outro: '))
    elif opcao > 5:
        print('Opção incorreta, escolha outra')
    print('=-=' * 10)
print('Você escolheu [5] = Progama Encerrado')





