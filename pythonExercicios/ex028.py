##Escreva um programa que faça o computador
#  “pensar” em um número inteiro
#  entre 0 e 5 e peça para o usuário tentar descobrir 
# qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
pc = random.randint(0, 5)
user = int(input("Digite um número entre 0 e 5: "))
print("Acertou" if user == pc else "Errou")
print(f"O número certo é {pc}")
