##Crie um programa que leia o nome de uma cidade
#  diga se ela começa ou não com o nome "SANTO".

cidade = str(input("Digite o nome de uma cidade: ")).strip()
cidade2 = cidade.lower()
if cidade2[:5] == 'santo':
    print("Cidade começa com 'Santo'")
else:
    print("Cidade não começa com 'Santo'")


#if "santo" in cidade2:
#    print("Cidade começa com 'Santo'")
#else:
#    print("Cidade Não começa com 'Santo'")