#Crear el diccionario inicial
informacion_personal = {
    "nombre": "<Veronica Shiguango>",
    "edad": 35,
    "ciudad": "Loreto",
    "profesion": "Maestra",
}

#Acceder el valor de la ciudad y modificarlo
informacion_personal ["ciudad"] = "Tena"

#Actualizar la clave de la profesion
informacion_personal ["profesion"] = "Ingeniera"

#Verificar si la clave "telefono" existe y agregarlo
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0968256700"

#Eliminar la clave "edad"
informacion_personal.pop("edad")

#Imprimir el diccionario final
print("diccionario final:", informacion_personal)

# Imprimir el diccionario final utilizando iteración
print("Diccionario final:")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")