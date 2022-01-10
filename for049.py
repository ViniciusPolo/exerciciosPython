#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
t=int(input('Digite qual número deseja fazer a tabuada: '))
for c in range(0,11,1):
    print('{} x {} = {}'.format(t,c,c*t))
