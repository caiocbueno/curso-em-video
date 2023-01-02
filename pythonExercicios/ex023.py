##Faça um programa que leia um número de 0 a 9999
#  e mostre na tela cada um dos dígitos separados.



numero = int(input("Digite um número entre 0 e 9999: "))
if numero > 0 and numero < 9999:
    for n in str(numero):
        print(n)
else:
    print("Número inválido")
    