#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
i = float(input('Escreva uma metragem: '))
k = i/1000
hm = i/100
dm = i / 10
mm = i * 1000
cm = i* 100
print('{} metros, equivalem a {} centimetros e {} milimetros.\nE {} Kilometros, {} Hectometros e {} decametros'.format(i, cm, mm, k, hm, dm))