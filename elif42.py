#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes
a = float(input('Digite o tamanho do lado a: '))
b = float(input('Digite o tamanho do lado b: '))
c = float(input('Digite o tamanho do lado c: '))
if (a<b+c and b<a+c and c<a+b):
    print('Com essas medidas é possível formar um triângulo')
    if a==b and b==c:
        print('As medidas são iguais, portanto é um triângulo EQUILATERO.')
    elif (a!=b and b==c) or (b!=c and b==a) or (c!=a and c==b):
        print('As medidas são {}, {}, {}, ou seja um dos lados é diferente, portanto é um triângulo ISÓCELES.'.format(a,b,c))
    else:
        print('As medidas são {}, {}, {}, ou seja todos os lados são diferentes, portanto é um triângulo ESCALENO.'.format(a,b,c))
else:
    print('Não é possivel formar um triângulo com essas medidas.')