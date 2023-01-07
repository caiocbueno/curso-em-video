##: Elabore um programa que calcule o valor a ser pago por um produto,
#  considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal 

#– 3x ou mais no cartão: 20% de juros

valor = float(input("Digite o valor do produto: "))
print("""FORMA DE PAGAMENTO
[1] À vista dinheiro/cheque: 10% de desconto
[2] À vista no cartão: 5% de desconto
[3] 2x no cartão
[4] 3x ou mais no cartão: 20% de juros""")
opcao = int(input("Digite uma opção de pagamento: "))
dinheiro = valor - valor * 0.10
cartao = valor - valor * 0.05
duas = valor / 2
juros = (valor + valor * 0.2)
if opcao == 1:
    print(f"O valor à vista (dinheiro/cheque) com 10% de desconto é R${dinheiro:.2f}")
elif opcao == 2:
    print(f"O valor á vista (cartão) com 5% de desconto é R${cartao:.2f}")
elif opcao == 3:
    print(f"O valor é R${valor:.2f} em duas vezes de R${duas:.2f}")
elif opcao == 4:
    parcela = int(input("Digite o número de parcelas: "))
    if parcela <= 2:
        print("Opção inválida")
    else:
        print(f"O valor com 20% de juros é R${juros:.2f} em {parcela} vezes de R${juros / parcela:.2f}")
else:
    print("Opção inválida")