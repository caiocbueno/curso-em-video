##Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#  Faça um programa que ajude ele,
#  lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

nomes = ["caio", "maria", "joao", "jose"]
nome = random.choice(nomes)
print(f"Alunos: {nomes[0]}, {nomes[1]}, {nomes[2]} e {nomes[3]}")
print(f"Aluno escolhido: {nome}")