## Refaça o DESAFIO 35 dos triângulos, acrescentando 
# o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferentes

print("Digite os valores para formar um triângulo: ")
a = int(input("Digite o primeiro valor:"))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))
if a+b > c and a+c > b and b+c > a:
    print("É possível construir o triângulo")
    if a == b and b == c:
        print("Triângulo EQUILÁTERO, todos os lados são iguais.")
    elif a == b or a ==c or b == c:
        print("Triângulo ISÓSCELES, dois lados iguais, um diferente.")
    else:
        print("Triângulo ESCALENO, todos os lados diferentes.") 
else:
    print("Não é possível construir o triângulo")    