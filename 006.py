#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
i=int(input('Digite um numero: '))
d=i*2
t=i*3
rq=i**(1/2)
print('O dobro de {} é {}, já o triplo é {}, por sua vez a Raiz quadradada de {} é {}'.format(i, d, t, i, rq))
