## Escreva um programa que pergunte o salário de um funcionário
#  e calcule o valor do seu aumento. Para salários superiores a R$1250,00
# , calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = int(input("Digite o salário: "))
if sal <= 1250:
    print(f"Aumento de 15% = R${sal + (sal * 0.15):.2f}")
if sal > 1250:
    print(f"Aumento de 10% = R${sal + (sal * 0.1):.2f}")

