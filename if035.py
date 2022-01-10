#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
a = float(input('Digite o tamanho do lado a: '))
b = float(input('Digite o tamanho do lado b: '))
c = float(input('Digite o tamanho do lado c: '))
if (a<b+c and b<a+c and c<a+b):
    print('Com essas medidas é possível formar um triângulo')
else:
    print('Não é possivel formar um triângulo com essas medidas.')