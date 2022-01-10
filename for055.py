#Faça um programa que leia o peso de cinco pessoas, No final mostre qual o maior e qual o menor peso lidos
maior=float(0)
menor=float(0)
for c in range (1,6):
    peso=float(input("Digite o peso da {}º pessoa ".format(c)))
    if c==1: #para evitar a gambiarra de um peso altissimo, cuidado, o usuario vai testar, faça do jeito certo
        menor=peso
        maior=peso
    else:
        if peso>maior:
            maior=peso
        elif peso<menor:
            menor=peso

print ("O maior peso declado foi {} Kg, enquanto o menor foi {} Kg.".format(maior,menor))


