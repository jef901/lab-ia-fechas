#!/usr/bin/env python3
"""
Tests unitarios para calculadora_fechas.py
Framework: unittest (stdlib)
"""

import unittest
from unittest.mock import patch
from datetime import date, datetime

from calculadora_fechas import calcular_dias_restantes


class TestCalcularDiasRestantes(unittest.TestCase):
    """Pruebas para la función calcular_dias_restantes."""

    # ---------- fecha futura normal ----------
    @patch("calculadora_fechas.datetime")
    def test_fecha_futura(self, mock_dt):
        """Una fecha futura debe devolver un número positivo de días."""
        mock_dt.now.return_value = datetime(2026, 9, 1)
        mock_dt.strptime.side_effect = lambda s, f: datetime.strptime(s, f)

        resultado = calcular_dias_restantes("05/09/2026")

        self.assertEqual(resultado, 4)

    # ---------- hoy = 0 días ----------
    @patch("calculadora_fechas.datetime")
    def test_fecha_hoy(self, mock_dt):
        """La fecha de hoy debe devolver exactamente 0 días."""
        mock_dt.now.return_value = datetime(2026, 9, 1)
        mock_dt.strptime.side_effect = lambda s, f: datetime.strptime(s, f)

        resultado = calcular_dias_restantes("01/09/2026")

        self.assertEqual(resultado, 0)

    # ---------- fecha pasada ----------
    @patch("calculadora_fechas.datetime")
    def test_fecha_pasada(self, mock_dt):
        """Una fecha pasada debe devolver un número negativo de días."""
        mock_dt.now.return_value = datetime(2026, 9, 4)
        mock_dt.strptime.side_effect = lambda s, f: datetime.strptime(s, f)

        resultado = calcular_dias_restantes("01/01/2026")

        self.assertEqual(resultado, -246)

    # ---------- formato inválido ----------
    def test_formato_invalido(self):
        """Un formato incorrecto debe lanzar ValueError."""
        with self.assertRaises(ValueError):
            calcular_dias_restantes("2026/09/01")


if __name__ == "__main__":
    unittest.main()
