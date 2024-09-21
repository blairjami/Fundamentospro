def calcular_temperatura_promedio(temperaturas):
    """
    Calcula la temperatura promedio de varias ciudades durante un período de tiempo.

    :param temperaturas: Diccionario donde las claves son nombres de ciudades y los valores son listas de temperaturas.
    :return: Diccionario con las temperaturas promedio de cada ciudad.
    """
    promedios = {}
    for ciudad, temps in temperaturas.items():
        if temps:  # Verifica que la lista de temperaturas no esté vacía
            promedio = sum(temps) / len(temps)
            promedios[ciudad] = promedio
        else:
            promedios[ciudad] = None  # Si no hay datos, asigna None

    return promedios

def main():
    # Ejemplo de datos de temperaturas para 3 ciudades durante 4 semanas
    datos_temperaturas = {
        "Quito": [15, 16, 14, 15],
        "Guayaquil": [25, 26, 24, 25],
        "Cuenca": [12, 13, 11, 12],
    }

    # Calcular las temperaturas promedio
    promedios = calcular_temperatura_promedio(datos_temperaturas)

    # Mostrar resultados
    for ciudad, promedio in promedios.items():
        if promedio is not None:
            print(f"La temperatura promedio en {ciudad} es: {promedio:.2f}°C")
        else:
            print(f"No hay datos disponibles para {ciudad}.")

if __name__ == "__main__":
    main()
