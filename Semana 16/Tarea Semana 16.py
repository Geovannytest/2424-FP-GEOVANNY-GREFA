# Definimos el nombre del archivo
file_name = "my_notes.txt"

# Abrimos el archivo en modo escritura (esto crea el archivo si no existe)
archivo_escritura = open(file_name, "w")

# Escribimos algunas líneas en el archivo
archivo_escritura.write("Línea 1: Hoy aprendí a usar archivos en Pyton.\n")
archivo_escritura.write("Línea 2: Me gusta mucho la programacion.\n")
archivo_escritura.write("Línea 3: Estoy emocionado por aprender más.\n")

# Cerramos el archivo
archivo_escritura.close()

# Definimos el nombre del archivo
file_name = "my_notes.txt"

# Abrimos el archivo en modo lectura
archivo_lectura = open(file_name, "r")

# Leemos y mostramos cada línea del archivo
for linea in archivo_lectura:
    print(linea.strip())  # .strip() elimina los caracteres de nueva línea al final de cada línea

# Cerramos el archivo
archivo_lectura.close()

# Definimos el nombre del archivo
file_name = "my_notes.txt"

# Abrimos el archivo en modo lectura
archivo_lectura = open(file_name, "r")

# Leemos y mostramos cada línea del archivo
for linea in archivo_lectura:
    print(linea.strip())  # .strip() elimina los caracteres de nueva línea al final de cada línea

# Cerramos el archivo
archivo_lectura.close()
