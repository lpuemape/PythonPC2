def contar_digito(numero, digito):
  numero_str = str(numero)
  return numero_str.count(str(digito))
numero = 15789000
digito = 0
cantidad_digito = contar_digito(numero, digito)
print(f"Cantidad de veces {digito} en el número {numero}: {cantidad_digito}")
