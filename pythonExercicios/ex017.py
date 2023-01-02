##Faça um programa que leia o comprimento do cateto oposto
#  e do cateto adjacente de um triângulo retângulo.
#  Calcule e mostre o comprimento da hipotenusa.

#import math
from math import hypot
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
#hi = math.hypot(co, ca)
hi = hypot(co, ca)
print(f"O valor da hipotenusa é: {hi:.2f}")