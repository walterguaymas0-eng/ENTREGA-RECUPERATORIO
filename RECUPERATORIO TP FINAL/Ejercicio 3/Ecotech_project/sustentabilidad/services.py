
def calcular_emisiones_carbono(
    consumo_kwh: float,
    factor_emision: float = 0.4
) -> float:
    """
    Calcula las emisiones de carbono según el consumo energético.

    Eleva ValueError cuando el consumo es negativo.
    """

    if consumo_kwh < 0:
        raise ValueError("El consumo energético no puede ser negativo.")

    emisiones = consumo_kwh * factor_emision

    return emisiones


def obtener_metricas_consumo(registros: list[dict]) -> dict:
    """
    Procesa el historial de consumos de las plantas industriales.

    Calcula las emisiones totales y determina qué planta
    registra el mayor consumo acumulado.
    """

    total_emisiones = 0.0
    consumos_por_planta = {}

    for registro in registros:

        planta = registro.get("planta")
        consumo = registro.get("consumo_kwh", 0)

        # Calculamos las emisiones de cada registro
        emisiones = calcular_emisiones_carbono(consumo)

        # Acumulamos las emisiones globales
        total_emisiones += emisiones

        # Acumulamos el consumo por planta
        consumos_por_planta[planta] = (
            consumos_por_planta.get(planta, 0) + consumo
        )

    # Determinamos la planta con mayor consumo acumulado
    if consumos_por_planta:
        planta_top = max(
            consumos_por_planta,
            key=consumos_por_planta.get
        )
    else:
        planta_top = None



    return {
        "total_emisiones": total_emisiones,
        "planta_top": planta_top
    }



