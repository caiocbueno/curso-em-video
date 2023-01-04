##Escreva um programa em Python que leia um número inteiro qualquer 
# e peça para o usuário escolher qual será a base de conversão: 
# 1 para binário, 2 para octal e 3 para hexadecimal.

print("CONVERSOR NUMÉRICO")
print("------------------")
n = int(input("Digite um número: "))
opcao = str.lower(input("Escolha um tipo de conversão: 'B' para binário, 'O' para octal e 'H' para hexadecimal: "))
if opcao == "b":
    print(bin(n))
elif opcao == "o":
    print(oct(n))
elif opcao == "h":
    print(hex(n))
else:
    print("Opção inválida")