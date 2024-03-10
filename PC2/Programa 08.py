def factorial(numero):
  if numero < 0:
    raise ValueError("El número debe ser un entero no negativo")
  elif numero == 0 or numero == 1:
    return 1
  else:
    return numero * factorial(numero - 1)
numero = 20
factorial_numero = factorial(numero)
print(f"El factorial de {numero} es {factorial_numero}")
