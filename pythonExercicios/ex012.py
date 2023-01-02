##faça um algoritmo que leia o preço de um produto
#  e mostre seu novo preço com 5% de desconto.
po = float(input("Preço original do produto: "))
pd = po - po * 0.05
print(f"Preço com 5% de desconto: R${pd:.2f}")