##Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from calendar import isleap

ano = int(input("Digite o ano: "))
print("Ano bissexto" if isleap(ano) else "Não é bissexto") 