def notas(alumno):
  notas = []
  for i in range(3):
    nota = float(input(f"Digite la nota {i + 1} de {alumno}: "))
    notas.append(nota)
  return notas
def listado(alumnos):
  for alumno in alumnos:
    print(f"Alumno: {alumno['Nombre']}")
    print(f"Notas: {alumno['Notas']}")
    print("-" * 20)
alumnos = []
while True:
  nombre = input("Ingrese el nombre del alumno (o 'FIN' para salir): ")
  if nombre.upper() == "FIN":
    break
  notas = notas(nombre)
  alumnos.append({"Nombre": nombre, "Notas": notas})
listado(alumnos)
