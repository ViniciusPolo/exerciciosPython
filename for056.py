#056 - Desenvolva um programa que leia o nome idade e sexo de 4 pessoas.
#No final do programa, mostre: a idade média do grupo, qual é o nome do homem mais velho e quantas mulheres tem menos de 20 anos.
idade=0
idademaior=0
contmulher=0
total_idade=0
nomevelho=""
for c in range(1,5):
    nome=input('Digite o nome da {}° pessoa:\n'.format(c))
    idade=int(input('Digite a idade da {}º pessoa\n'.format(c)))
    sexo = input('Digite o sexo da {}º pessoa (m/f) '.format(c))
    total_idade+=idade
    if sexo in 'm' and idade>idademaior:
        idademaior = idade
        nomevelho=nome
    elif sexo in 'f' and idade<=20:
        contmulher=contmulher+1
    elif sexo != 'm' or sexo !='f':
        c=c-1
total_idade = total_idade/c
print (f"Idade media:{total_idade}\nMais velho: {nomevelho} com {idademaior} \n{contmulher} são do sexo feminino com menos de 20 anos")

