def desea_ingresar_numero():
  respuesta = input("¿Desea ingresar un número? (SI/NO): ")
  return respuesta.upper() == "SI"
numeros = []
numero_pares = 0
numero_impares = 0
while desea_ingresar_numero():
  numero = int(input("Ingrese el número: "))
  numeros.append(numero)
  if numero % 2 == 0:
    numero_pares += 1
  else:
    numero_impares += 1
print("Números ingresados:", numeros)
print("Cantidad de números pares:", numero_pares)
print("Cantidad de números impares:", numero_impares)
