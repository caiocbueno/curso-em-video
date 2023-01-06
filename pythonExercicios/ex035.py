## Desenvolva um programa que leia o comprimento
#  de três retas e diga ao usuário
#  se elas podem ou não formar um triângulo.



print("Digite os valores para formar um triângulo: ")
a = int(input("Digite o primeiro valor:"))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))
if a+b > c and a+c > b and b+c > a:
    print("É possível construir o triângulo")
else:
    print("Não é possível construir o triângulo")    