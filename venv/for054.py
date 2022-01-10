#054 Crie um programa que leia o ano de nascimento de 7 pessoas e no final mostre quantas pessoas ainda não atigiram a maioridade e quantas já são maiores
from datetime import date
maior=0
menor=0
atual = date.today().year
for c in range (1,8):
    ano=int(input(f"Digite o ano de Nascimento da {c}º pessoa: "))
    if (atual-ano)>=18:
        maior = maior +1
    else:
        menor = menor +1

print(f"Entre os anos digitados há {maior} maiores de idade e {menor} menores de idade")