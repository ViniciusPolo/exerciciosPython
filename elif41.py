#Exercício Python 041:
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER
from datetime import date
ano = int(input('Qual é o ano de nascimento do atleta: '))
idade = (date.today().year)-ano
if idade<=9:
    print('Com {} anos é um atleta MIRIM'.format(idade))
elif idade>9 and idade<=14:
    print('Com {} anos é um atleta INFANTIL'.format(idade))
elif idade>14 and idade<=19:
    print('Com {} anos é um atleta JÚNIOR'.format(idade))
elif idade>19 and idade<=25:
    print('Com {} anos é um atleta SENIOR'.format(idade))
else:
    print('Com {} anos é um atleta MASTER'.format(idade))