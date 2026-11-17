
from django.shortcuts import render

from .services import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):

    # Historial de consumos de las plantas industriales
    registros = [
        {"planta": "Norte", "consumo_kwh": 1200},
        {"planta": "Sur", "consumo_kwh": 850},
        {"planta": "Norte", "consumo_kwh": 1400}
    ]

    # Procesamos las métricas mediante services.py
    metricas = obtener_metricas_consumo(registros)

    # Preparamos el diccionario de contexto
    contexto = {
        "total_emisiones": metricas["total_emisiones"],
        "planta_top": metricas["planta_top"]
    }

    # Renderizamos la plantilla HTML
    return render(
        request,
        "sustentabilidad/panel.html",
        contexto
    )
