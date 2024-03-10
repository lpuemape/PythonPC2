def div_7_5(numero):
    return numero % 7 == 0 and numero % 5 == 0
num_encontrados = []
for numero in range(1500,2701):
    if div_7_5(numero):
        num_encontrados.append(numero)
print("Los numeros divisibles por 7 y multiplos de 5 en el rango de 1500 a 2700:")
print(", ".join(str(numero) for numero in num_encontrados))