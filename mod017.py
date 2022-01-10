#Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import cos, sin, tan, radians
#para calcular seno, cosseno e tangente o valor deve ser convertido para radiano
angulo = float(input('Digite o angulo: '))
cos = cos(radians(angulo))
sen = sin(radians(angulo))
tan = tan(radians(angulo))
print ('O Angulo de {}º apresenta os seguintes valores:\nCosseno: {:.2f}\nSeno: {:.2f}\nTangente: {:.2f}'.format(angulo, cos, sen, tan))
