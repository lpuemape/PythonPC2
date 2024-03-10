def eliminar_vocales(texto):
  vocales = "aeiouAEIOU"
  texto_sin_vocales = ""
  for letra in texto:
    if letra not in vocales:
      texto_sin_vocales += letra
  return texto_sin_vocales
texto = input("Ingrese una cadena de texto: ")
texto_sin_vocales = eliminar_vocales(texto)
print(f"Texto sin vocales: {texto_sin_vocales}")
