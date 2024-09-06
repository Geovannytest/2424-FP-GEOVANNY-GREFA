# Crear una matriz bidimensional (3x3) para el ejemplo.txt# Crear una matriz 3D para almacenar datos de temperaturas
# # Primera dimensión: Ciudades (3 ciudades)
# # Segunda dimensión: Semanas (4 semanas)
# # Tercera dimensión: Días de la semana (7 días)
# temperaturas = [
#     [   # Ciudad 1
#         [   # Semana 1
#             {"day": "Lunes", "temp": 78},
#             {"day": "Martes", "temp": 80},
#             {"day": "Miércoles", "temp": 82},
#             {"day": "Jueves", "temp": 79},
#             {"day": "Viernes", "temp": 85},
#             {"day": "Sábado", "temp": 88},
#             {"day": "Domingo", "temp": 92}
#         ],
#         [   # Semana 2
#             {"day": "Lunes", "temp": 76},
#             {"day": "Martes", "temp": 79},
#             {"day": "Miércoles", "temp": 83},
#             {"day": "Jueves", "temp": 81},
#             {"day": "Viernes", "temp": 87},
#             {"day": "Sábado", "temp": 89},
#             {"day": "Domingo", "temp": 93}
#         ],
#         [   # Semana 3
#             {"day": "Lunes", "temp": 77},
#             {"day": "Martes", "temp": 81},
#             {"day": "Miércoles", "temp": 85},
#             {"day": "Jueves", "temp": 82},
#             {"day": "Viernes", "temp": 88},
#             {"day": "Sábado", "temp": 91},
#             {"day": "Domingo", "temp": 95}
#         ],
#         [   # Semana 4
#             {"day": "Lunes", "temp": 75},
#             {"day": "Martes", "temp": 78},
#             {"day": "Miércoles", "temp": 80},
#             {"day": "Jueves", "temp": 79},
#             {"day": "Viernes", "temp": 84},
#             {"day": "Sábado", "temp": 87},
#             {"day": "Domingo", "temp": 91}
#         ]
#     ],
#     [   # Ciudad 2
#         [   # Semana 1
#             {"day": "Lunes", "temp": 62},
#             {"day": "Martes", "temp": 64},
#             {"day": "Miércoles", "temp": 68},
#             {"day": "Jueves", "temp": 70},
#             {"day": "Viernes", "temp": 73},
#             {"day": "Sábado", "temp": 75},
#             {"day": "Domingo", "temp": 79}
#         ],
#         [   # Semana 2
#             {"day": "Lunes", "temp": 63},
#             {"day": "Martes", "temp": 66},
#             {"day": "Miércoles", "temp": 70},
#             {"day": "Jueves", "temp": 72},
#             {"day": "Viernes", "temp": 75},
#             {"day": "Sábado", "temp": 77},
#             {"day": "Domingo", "temp": 81}
#         ],
#         [   # Semana 3
#             {"day": "Lunes", "temp": 61},
#             {"day": "Martes", "temp": 65},
#             {"day": "Miércoles", "temp": 68},
#             {"day": "Jueves", "temp": 70},
#             {"day": "Viernes", "temp": 72},
#             {"day": "Sábado", "temp": 76},
#             {"day": "Domingo", "temp": 80}
#         ],
#         [   # Semana 4
#             {"day": "Lunes", "temp": 64},
#             {"day": "Martes", "temp": 67},
#             {"day": "Miércoles", "temp": 69},
#             {"day": "Jueves", "temp": 71},
#             {"day": "Viernes", "temp": 74},
#             {"day": "Sábado", "temp": 77},
#             {"day": "Domingo", "temp": 80}
#         ]
#     ],
#     [   # Ciudad 3
#         [   # Semana 1
#             {"day": "Lunes", "temp": 90},
#             {"day": "Martes", "temp": 92},
#             {"day": "Miércoles", "temp": 94},
#             {"day": "Jueves", "temp": 91},
#             {"day": "Viernes", "temp": 88},
#             {"day": "Sábado", "temp": 85},
#             {"day": "Domingo", "temp": 82}
#         ],
#         [   # Semana 2
#             {"day": "Lunes", "temp": 89},
#             {"day": "Martes", "temp": 91},
#             {"day": "Miércoles", "temp": 93},
#             {"day": "Jueves", "temp": 90},
#             {"day": "Viernes", "temp": 87},
#             {"day": "Sábado", "temp": 84},
#             {"day": "Domingo", "temp": 81}
#         ],
#         [   # Semana 3
#             {"day": "Lunes", "temp": 91},
#             {"day": "Martes", "temp": 93},
#             {"day": "Miércoles", "temp": 95},
#             {"day": "Jueves", "temp": 92},
#             {"day": "Viernes", "temp": 89},
#             {"day": "Sábado", "temp": 86},
#             {"day": "Domingo", "temp": 83}
#         ],
#         [   # Semana 4
#             {"day": "Lunes", "temp": 88},
#             {"day": "Martes", "temp": 90},
#             {"day": "Miércoles", "temp": 92},
#             {"day": "Jueves", "temp": 89},
#             {"day": "Viernes", "temp": 86},
#             {"day": "Sábado", "temp": 83},
#             {"day": "Domingo", "temp": 80}
#         ]
#     ]
# ]
#
# # Calcular el promedio de temperaturas para cada ciudad y semana
# for ciudad in temperaturas:
#     for semana in ciudad:
#         suma = 0
#         for dia in semana:
#             suma += dia['temp']
#         print(suma)
matriz = [
    [5, 2, 9],
    [3, 7, 1],
    [8, 4, 6]
]

# Función para ordenar una fila de manera ascendente utilizando Bubble Sort
def bubble_sort_fila(fila):
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambiar elementos

# Función para mostrar la matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Mostrar la matriz original
print("Matriz Original:")
mostrar_matriz(matriz)

# Ordenar cada fila de la matriz utilizando Bubble Sort
for fila in matriz:
    bubble_sort_fila(fila)

# Mostrar la matriz ordenada
print("\nMatriz Ordenada por Filas:")
mostrar_matriz(matriz)


# En este ejemplo.txt:
# Creamos una matriz 3x3 para representar nuestros datos.
# Implementamos la función bubble_sort_fila que utiliza el algoritmo del Método de la Burbuja para ordenar una fila de manera ascendente.
# Utilizamos un bucle para recorrer cada fila de la matriz y aplicar bubble_sort_fila para ordenar las filas individualmente.
# Mostramos la matriz original y luego la matriz ordenada por filas.
# El algoritmo Bubble Sort compara pares de elementos adyacentes y los intercambia si están en el orden incorrecto. Repite este proceso hasta que la matriz esté completamente ordenada. Es importante recordar que este algoritmo puede no ser eficiente en arreglos grandes debido a su complejidad de tiempo cuadrática.