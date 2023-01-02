##Escreva um programa que leia a velocidade de um carro.
#  Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#  A multa vai custar R$7,00 por cada Km acima do limite.


print("Velocidade máxima permitida 80km/h")
vel = int(input("Digite a velocidade do carro: "))
if vel > 80:
    print("Você foi multado!")
    print(f"Valor da multa: {(vel - 80)*7} reais.")
else:
    print("Velocidade permitida.")
