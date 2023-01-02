##Faça um programa que leia três números
#  e mostre qual é o maior e qual é o menor.

print("Digite três números")
n1 = int(input("Primero número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))
if n1 > n2 and n1 > n3:
    print(f"{n1} é o maior")
if n2 > n1 and n2 > n3:
    print(f"{n2} é o maior")
if n3 > n1 and n3 > n2:
    print(f"{n3} é o maior")        
if n1 < n2 and n1 < n3:
    print(f"{n1} é o menor")    
if n2 < n1 and n2 < n3:
    print(f"{n2} é o menor") 
if n3 < n1 and n3 < n2:
    print(f"{n3} é o menor")       