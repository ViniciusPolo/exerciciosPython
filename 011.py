#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
l = float(input('Qual é a largura da parede: '))
a = float(input('Qual é a altura da parede: '))
c = float(l*a)*2
print('A sua parede de {} de altura e {} m de largura, você vai precisar de {} litros de tinta'.format(a, l, c))