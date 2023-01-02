##Desenvolva um programa que pergunte a distância de uma viagem em Km.
#  Calcule o preço da passagem, cobrando R$0,50 por Km
#  para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = int(input("Digite a distância da viagem em KM: "))
if dist <= 200:
    print(f"Custo da viagem: R${dist * 0.5:.2f}")
else:
    print(f"Custo da viagem : R${dist * 0.45:.2f}") 
