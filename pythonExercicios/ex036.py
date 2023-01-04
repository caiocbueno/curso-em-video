##Exercício Python 36: Escreva um programa para 
# aprovar o empréstimo bancário para a compra de uma casa.
#  Pergunte o valor da casa,o salário do comprador e em quantos anos ele vai pagar.
#  A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.


valorCasa = int(input("Digite o valor do imóvel: "))
salario = int(input("Digite o valor do seu salário: "))
anos = int(input("Digite em quantos anos quer financiar: "))
meses = anos * 12
prestacao = valorCasa / meses
if prestacao <= salario * 0.3:
    print(f"Financiamento aprovado, valor da parcela: R${prestacao:.2f}")
else: 
    print(f"Financiamento reprovado, valor da prestação ultrapassou 30% do valor do salário")




