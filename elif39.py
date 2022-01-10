#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

idade = int(input('Digite a idade: '))
sexo = int(input('''Digite o seu Sexo: 
[ 1 ] Masculino
[ 2 ] Feminino\n'''))
if sexo==2:
    print('Você é mulher e não precisa se alistar')
elif sexo!=1 and sexo!=2:
    print('Você digitou uma opção incorreta no sexo.')
elif idade==18 and sexo==1:
    print('Voce precisa se alistar imediatamente.')
elif idade<18 and sexo==1:
    print('Você ainda não precisa se alistar, seu alistamento militar será em {} ano(s).'.format(18 - idade))
else:
    print('Já passou seu tempo de alistamento a {} anos.'.format(idade-18))
