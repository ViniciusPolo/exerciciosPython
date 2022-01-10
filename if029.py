#Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
vel = float(input("Qual foi a velocidade do carro: "))
if (vel>80):
    print('\033[31mVocê foi multado e sua multa será de {}R$ {:.2f}'.format('\033[1m',(vel-80)*7))
else:
    print('Sua velocidade {}KM/h, \033[1;32mBoa Viagem'.format(vel))
