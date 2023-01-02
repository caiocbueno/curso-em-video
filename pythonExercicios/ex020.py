##O mesmo professor do desafio 19 quer sortear a ordem
#  de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos
#  e mostre a ordem sorteada.

import random

nomes = ["caio", "maria", "joao", "jose"]
print(nomes)
random.shuffle(nomes)
print(
    f'''
    Primeiro aluno: {nomes[0]}
    Segundo aluno: {nomes[1]}
    Terceiro aluno: {nomes[2]}
    Quarto aluno {nomes[3]}
    '''
)