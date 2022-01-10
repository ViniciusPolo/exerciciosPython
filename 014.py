#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input('Digite os graus em celsius: '))
f = float(9 * c / 5 + 32)
#precedencia * e / tem o mesmo valor, portanto vale o que vem primeiro, e depois o +, dispensa o parenteses
print('{}ºC equivalem a {:.2f}ºF'.format(c, f))