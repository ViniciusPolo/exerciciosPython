# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Digite o sexo: ').strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input('Sexo incorreto, digite novamente: ').strip().upper()[0]


nome = input('Digite o Nome: ')
print(f'Seu nome é: {nome} do sexo {sexo}')
