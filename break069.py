#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:

#A) quantas pessoas tem mais de 18 anos.

#B) quantos homens foram cadastrados.

#C) quantas mulheres tem menos de 20 anos.
cont_idade = int(0)
cont_homem = 0
cont_mulher = 0
while True:
    idade = int(input('Informe a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo da pessoa: ')).strip().upper()[0]
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar: (S/N)')).strip().upper()[0]
    if continuar == 'N':
        print('Programa encerrado!')
        break
    if idade > 18:
        cont_idade += 1
    if sexo == 'M':
        cont_homem += 1
    if sexo == 'F' and idade < 20:
        cont_mulher += 1
print (f'Foram cadastradas {cont_idade} pessoas com mais de 18 anos\n{cont_homem} são do sexo masculino\nE há {cont_mulher} mulheres com menos de 20 anos')
    
