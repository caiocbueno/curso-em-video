##Crie um programa que leia o nome de uma pessoa 
# e diga se ela tem "SILVA" no nome.

nome = str(input("Digite seu nome completo:"))
nome2 = nome.lower()
if "silva" in nome2:
    print("Tem 'Silva' no nome")
else:
    print("Não tem 'Silva' no nome")