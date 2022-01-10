#Exercício Python 37:
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
n = int(input('Digite um número decimal: '))
print('''Ecolha um das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADEXIMAL''')
opcao = int(input('Sua Opção: '))
if opcao == 1:
    print('{} convertido para BINÀRIO é: {}'.format(n,bin(n)[2:]))
#sempre vai aparecer o tipo do numero 0b para binario, 0o para Octal e 0x para hexadecial, se usa o [2:](digito dois até o fim) para oculta-los, ver aula tratamento de textos.
elif opcao == 2:
    print('{} convertido para BINÀRIO é: {}'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('{} convertido para BINÀRIO é: {}'.format(n, hex(n)[2:]))
else:
    print('Digite uma opção correta:')


