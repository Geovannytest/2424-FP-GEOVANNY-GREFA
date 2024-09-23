def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto con descuento aplicado.

    Parámetros:
    monto_total (float): El monto total de la compra.
    porcentaje_descuento (float): El porcentaje de descuento a aplicar (10% por defecto).

    Retorna:
    float: El monto total después de aplicar el descuento.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    monto_final = monto_total - descuento
    return monto_final
# Llamada con el valor predeterminado del 10%
total_con_descuento = calcular_descuento(100)
print(total_con_descuento)  # Debería imprimir 90.0

# Llamada con un descuento personalizado del 15%
total_con_descuento = calcular_descuento(100, 15)
print(total_con_descuento)  # Debería imprimir 85.0


def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a la compra.

    Parámetros:
    monto_total (float): El monto total de la compra.
    porcentaje_descuento (float): El porcentaje de descuento a aplicar (10% por defecto).

    Retorna:
    float: El monto del descuento.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento
# Llamada con el valor predeterminado del 10%
descuento = calcular_descuento(100)
print(descuento)  # Debería imprimir 10.0

# Llamada con un descuento personalizado del 15%
descuento = calcular_descuento(100, 15)
print(descuento)  # Debería imprimir 15.0


def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento aplicado a la compra.

    Parámetros:
    monto_total (float): El monto total de la compra.
    porcentaje_descuento (float): El porcentaje de descuento a aplicar (10% por defecto).

    Retorna:
    float: El monto del descuento.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento
# Llamada con el valor predeterminado del 10%
descuento = calcular_descuento(100)
print(descuento)  # Imprime 10.0 (10% de descuento sobre 100)

# Llamada con un descuento personalizado del 15%
descuento = calcular_descuento(100, 15)
print(descuento)  # Imprime 15.0 (15% de descuento sobre 100)
