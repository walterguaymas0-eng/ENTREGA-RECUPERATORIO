
import unittest

from .services import calcular_emisiones_carbono
from .services import obtener_metricas_consumo


class TestCalculoEmisiones(unittest.TestCase):

    def test_calculo_correcto(self):
        resultado = calcular_emisiones_carbono(100.0, 0.4)

        self.assertEqual(resultado, 40.0)

    def test_factor_emision_por_defecto(self):
        resultado = calcular_emisiones_carbono(100.0)

        self.assertEqual(resultado, 40.0)

    def test_factor_emision_personalizado(self):
        resultado = calcular_emisiones_carbono(100.0, 0.5)

        self.assertEqual(resultado, 50.0)

    def test_consumo_cero(self):
        resultado = calcular_emisiones_carbono(0)

        self.assertEqual(resultado, 0.0)

    def test_consumo_negativo_lanza_excepcion(self):

        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50.0)


class TestMetricasConsumo(unittest.TestCase):

    def test_obtener_metricas_consumo(self):

        registros = [
            {"planta": "Norte", "consumo_kwh": 1200},
            {"planta": "Sur", "consumo_kwh": 850},
            {"planta": "Norte", "consumo_kwh": 1400}
        ]

        resultado = obtener_metricas_consumo(registros)

        self.assertEqual(resultado["total_emisiones"], 1380.0)
        self.assertEqual(resultado["planta_top"], "Norte")

    def test_registros_vacios(self):

        resultado = obtener_metricas_consumo([])

        self.assertEqual(resultado["total_emisiones"], 0.0)
        self.assertIsNone(resultado["planta_top"])


if __name__ == "__main__":
    unittest.main()
