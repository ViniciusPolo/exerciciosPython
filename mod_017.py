#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
#import math - importei toda a biblioteca matemática, nesse caso tenho que usar o "math." antetes de chamar o hypot
from math import hypot
catetoop = float(input('Qual é a medida do cateto oposto: '))
catetoad = float(input('Qual é a medida do cateto adjacente: '))
#hipotenusa = catetoop**2 + catetoad**2
hipotenusa = hypot(catetoop, catetoad)
#hipotenusa = math.hypot(catetoop, catetoad)
print('Os catetos oposto que mede {} e adjacente que mede {} tem uma hipotenusa de {:.2f}'.format(catetoop, catetoad, hipotenusa**(1/2)))