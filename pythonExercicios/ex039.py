##Faça um programa que leia o ano de nascimento de um jovem e informe,
#  de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#  se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime

ano = int(input("Digite o ano de nascimento: "))
now = datetime.now().year
idade = now - ano
print(f"Você tem {idade} anos.")
if idade == 18:
    print(f"Está na hora de se alistar no exército.")
elif idade > 18:
    print(f"Já se passaram {idade -18} anos desde o alistamento militar.")
elif idade <18:
    print(f"Faltam {18 - idade} anos para o alistamento militar.")
