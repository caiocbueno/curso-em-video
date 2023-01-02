##crie um programa que leia quanto dinhero uma pessoa tem na carteira
##e mostre quantos dólares ela pode comprar.
## considere U$D = R$ 3.27
real = float(input("Saldo em R$: "))
dolar = real / 3.27
print(f"Você pode comprar US${dolar:.2f}")