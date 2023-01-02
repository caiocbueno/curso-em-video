#escreva um programa que leia um valor em metros e o exiba 
#convertido em centímetros e milímetros

met = float(input("Valor em metros: "))
cent = int(met * 100)
mili = int(met * 1000)
print(f"O valor convertido é {cent} centímetros")
print(f"O valor convertido é {mili} milímetros")