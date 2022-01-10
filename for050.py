#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
n=0
for c in range(1,7):
    i= int(input('Digite o {}º numero: '.format(c)))
    if i%2==0:
        soma = i+soma
        n=n+1
print('A soma dos {} numeros pares digitados é: {}'.format(n,soma))