def es_primo(numero):
  if numero <= 1:
    return False
  elif numero <= 3:
    return True
  elif numero % 2 == 0 or numero % 3 == 0:
    return False
  i = 5
  while i * i <= numero:
    if numero % i == 0 or numero % (i + 2) == 0:
      return False
    i += 6
  return True
while True:
  numero = int(input("Ingrese un número (0 para salir): "))
  if numero == 0:
    break
  es_primo = es_primo(numero)
  print(f"El número {numero} {'es primo' if es_primo else 'no es primo'}")
