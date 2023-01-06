##A Confederação Nacional de Natação precisa de um programa 
# que leia o ano de nascimento de um atleta
#  e mostre sua categoria, de acordo com a idade:

# Até 9 anos: MIRIM

#– Até 14 anos: INFANTIL

#– Até 19 anos: JÚNIOR

#– Até 25 anos: SÊNIOR

#– Acima de 25 anos: MASTER

from datetime import datetime
now = datetime.now().year
ano = int(input("Digite o ano de nascimento: "))
idade = now - ano
if idade <= 9:
    print(f"Idade {idade} anos, categoria MIRIM")
elif idade > 9 and idade <= 14:
    print(f"Idade {idade} anos, categoria INFANTIL")
elif idade > 14 and idade <= 19:
    print(f"Idade {idade} anos, categoria JÚNIOR")
elif idade > 19 and idade <= 25:
    print(f"Idade {idade} anos, categoria SÊNIOR")
elif idade > 25:
    print(f"Idade {idade} anos, categoria MASTER")
