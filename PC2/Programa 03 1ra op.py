numeros = []
numero_pares = 0
numeros_impares = 0
while True:
# el numero 0 no se considera ni par ni impar, es por ello que considero al "0" como salida...
    numero = int(input("Digite un numero (0 para salir): "))
    if numero == 0:
        break
    numeros.append(numero)
    if numero % 2 == 0:
        numero_pares += 1
    else: 
        numeros_impares += 1
print("Numeros pares:", numero_pares)
print("Numeros impares:", numeros_impares)