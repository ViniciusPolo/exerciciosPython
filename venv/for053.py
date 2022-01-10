#crie um programa que leia uma frade qualquer e diga se ela é um palíndromo

frase = str(input('Digite uma frase: ')).strip().upper() #Os metodos strip e upper retiram os espaços e passam para maiusculas
palavras = frase.split() #separa as palavras em uma lista(array)
junto = ''.join(palavras) #junta as palavras
lista= list(junto)#não precisa
inverso =''


for c in range(len(lista)-1,-1,-1):
    inverso += junto[c]

print(junto)
print(inverso)
if (junto == inverso):
    print("É um palindromo")
else:
    print("Não é um palindromo")

