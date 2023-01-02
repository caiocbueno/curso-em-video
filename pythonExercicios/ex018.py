##Faça um programa que leia um ângulo qualquer
#  e mostre na tela o valor do seno,
#  cosseno e tangente desse ângulo.

import math
ang = float(input("Digite o ângulo: "))
print(
    f'''
Ângulo {ang}
Seno {math.sin(math.radians(ang))}
Coseno {math.cos(math.radians(ang))}
Tangente {math.tan(math.radians(ang))}    
    
    
    
    
    '''
)