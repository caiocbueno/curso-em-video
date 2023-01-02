##Escreva um programa que converta uma temperatura 
# digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input("Temperatura em Celsius: "))
f = c * (9 / 5) + 32
print(f"Temperatura em Farenheit: {f:.1f}°F")

##(0 °C × 9/5) + 32 = 32 °F
