##faça um programa que leia a largura e a altura de uma parede em metros,
#  calcule a sua área e a quantidade de tinta 
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

l = float(input("Largura da parede: "))
a = float(input("Altura da parede: "))
area = l * a
tinta = area / 2
print(
    f'''
Área da parede: {area:.2f}m²
Quantidade de tinta necessária: {tinta:.2f}L
    '''
)