##Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro 
# e o último nome separadamente.

nome = str(input("Digite seu nome completo: "))
separado = nome.split()
print(f"Primeiro nome: {separado[0].capitalize()}")
print(f"Último nome: {separado[-1].capitalize()}")