#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
#O programa será interrompido quando o número solicitado for negativo. 
while True:
    t = int (0)
    tot = int (0)
    n = int(input('Digite o número para ver sua tabuada, digite um negativo para encerrar: '))
    while t <= 10:
        if n<0:
            print('Número negativo digitado, programa encerrado')
            break
        tot = n*t
        print(f'{n} x {t} = {tot}')
        t+=1
    print(10*'-=')