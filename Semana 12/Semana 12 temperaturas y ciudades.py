# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad Tena
        [   # Semana 1
            {"day": "Lunes", "temp": 38},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 38},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 36},
            {"day": "Martes", "temp": 39},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 41},
            {"day": "Viernes", "temp": 37},
            {"day": "Sábado", "temp": 39},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 37},
            {"day": "Martes", "temp": 41},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 41},
            {"day": "Domingo", "temp": 35}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 38},
            {"day": "Miércoles", "temp": 40},
            {"day": "Jueves", "temp": 39},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 41}
        ]
    ],
    [   # Ciudad Loreto
        [   # Semana 1
            {"day": "Lunes", "temp": 42},
            {"day": "Martes", "temp": 44},
            {"day": "Miércoles", "temp": 38},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 43},
            {"day": "Sábado", "temp": 45},
            {"day": "Domingo", "temp": 39}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 43},
            {"day": "Martes", "temp": 38},
            {"day": "Miércoles", "temp": 40},
            {"day": "Jueves", "temp": 42},
            {"day": "Viernes", "temp": 39},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 41}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 41},
            {"day": "Martes", "temp": 40},
            {"day": "Miércoles", "temp": 38},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 42},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 40}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 39},
            {"day": "Martes", "temp": 37},
            {"day": "Miércoles", "temp": 39},
            {"day": "Jueves", "temp": 41},
            {"day": "Viernes", "temp": 40},
            {"day": "Sábado", "temp": 37},
            {"day": "Domingo", "temp": 40}
        ]
    ],
    [   # Ciudad Puyo
        [   # Semana 1
            {"day": "Lunes", "temp": 35},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 38},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 32}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 31},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 37},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 31}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 34},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 33}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 33},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 32},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 36},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 30}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["ciudad 1","ciudad 2","ciudad 3"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate (ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio}")







for ciudad in temperaturas:
    for semana in ciudad:
        suma = 0
        for dia in semana:
            suma += dia['temp']
        print(suma)
