def convertir_fecha(fecha):
  meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre"
  ]
  try:
    fecha_split = fecha.split()
  except ValueError:
    return "Error: La fecha debe estar separada por espacios o comas."
  if len(fecha_split) not in [3, 5]:
    return "Error: La fecha debe tener el formato 'mes-día-año' o 'mes día, año'."
  try:
    if len(fecha_split) == 3:
      mes_str = fecha_split[0]
      dia = int(fecha_split[1])
      año = int(fecha_split[2])
    else:
      mes_str = fecha_split[0]
      dia = int(fecha_split[2])
      año = int(fecha_split[4])
  except ValueError:
    return "Error: El día y el año deben ser números enteros."
  if mes_str not in meses:
    return "Error: El mes no es válido."
  if dia < 1 or dia > 31:
    return "Error: El día debe estar entre 1 y 31."
  mes_numero = meses.index(mes_str) + 1
  mes_str = f"{mes_numero:02}"
  dia_str = f"{dia:02}"
  fecha_convertida = f"{año}-{mes_str}-{dia_str}"
  return fecha_convertida
fecha = input("Ingrese una fecha (mes-día-año o mes día, año): ")
fecha_convertida = convertir_fecha(fecha)
if isinstance(fecha_convertida, str) and fecha_convertida.startswith("Error"):
  print(fecha_convertida)
else:
  print(f"Fecha en formato AAAA-MM-DD: {fecha_convertida}")

