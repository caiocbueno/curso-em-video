## Faça um programa que leia uma frase pelo teclado
#  e mostre quantas vezes aparece a letra "A",
#  em que posição ela aparece a primeira vez e
#  em que posição ela aparece a última vez.

frase = str(input("Digite uma frase qualquer:"))
low = frase.lower()
print(f"A letra 'A' aparece {low.count('a')} vezes.")
print(f"A primeira letra 'A' aparece na posição {low.find('a')} e a última na posição {low.rfind('a')}")