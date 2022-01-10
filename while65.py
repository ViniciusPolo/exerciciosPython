#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. 
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
cont = 0
tot = 0
s = 'S'
num = 0
while s == 'S':
    num = int(input('Digite um numero : '))
    s = input('Deseja acrescentar mais valores? (S/N): ').upper().strip()[0]
    tot = num + tot
    if cont <= 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    cont+=1
media = tot / cont
print(f'Foram inseridos {cont} numeros e sua media é {media}, o menor é {menor} e o maior é: {maior}')