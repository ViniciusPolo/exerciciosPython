#051 Desenvolva um programa que leia o primeiro termo da razão de uma PA, No final, mostre os 10 primeiros termos dessa progressão.

n1 = int(input('Favor digite o primeiro termo da PA: '))
p = int(input('Agora digite a razão: '))
n10 = n1+(10-1)*p      #formula para se descubrir o enésimo valor, quando o tamanho da progressão é definido, nesse caso 10
for i in range(n1,n10+p,p):  # Aqui se pode usar variaveis, para se definir o range, 1º termo, ultimo termo, progressão do range, o range é uma PA
    print('{}'.format(i), end=' > ')
print ('ACABOU')
