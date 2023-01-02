##Crie um programa que leia o nome completo de uma pessoa e mostre:
#  - O nome com todas as letras maiúsculas e minúsculas.
#  - Quantas letras ao todo (sem considerar espaços).
#  - Quantas letras tem o primeiro nome.


nome = str(input("Digite seu nome completo: "))
print(f"Nome em maiúsculas: {nome.upper()}")
print(f"Nome em minúsculas: {nome.lower()}")
letras = len(nome.replace(" " , ""))
print(f"Quantidade de letras: {letras}")
primeiro = nome.split()
print(f"Primeiro nome: {primeiro[0]}")
print(f"Quantidade de letras do primeiro nome: {len(primeiro[0])}")