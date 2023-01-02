# Escreva um programa que pergunte a quantidade de Km percorridos
#  por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#  Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = int(input("Quantidade de dias alugados: "))
km = float(input("Kilometros rodados: "))
pd = d * 60
pkm = km * 0.15
total = pd + pkm
print(f"Você alugou o carro por {d} dias e rodou {km} kilometros. Total a pagar: R${total:.2f}")