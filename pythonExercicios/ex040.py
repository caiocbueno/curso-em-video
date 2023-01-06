##Crie um programa que leia duas notas de um aluno e calcule sua média,
#  mostrando uma mensagem no final, de acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO

#– Média entre 5.0 e 6.9: RECUPERAÇÃO

#– Média 7.0 ou superior: APROVADO

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f"Sua nota foi {media}.\nMédia 7.0 ou superior: APROVADO")
if media >= 5 and media < 7:
    print(f"Sua nota foi {media}.\nMédia entre 5.0 e 6.9: RECUPERAÇÃO")
if media < 5:
    print(f"Sua nota foi {media}.\nMédia abaixo de 5.0: REPROVADO")