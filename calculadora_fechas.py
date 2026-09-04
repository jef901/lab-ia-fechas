#!/usr/bin/env python3
"""
Calculadora de Fechas
Calcula cuántos días faltan para una fecha específica ingresada por el usuario.
"""

from datetime import datetime


def calcular_dias_restantes(fecha_objetivo: str) -> int:
    """Calcula los días restantes hasta la fecha objetivo (formato: DD/MM/AAAA)."""
    hoy = datetime.now().date()
    destino = datetime.strptime(fecha_objetivo, "%d/%m/%Y").date()
    return (destino - hoy).days


def main():
    print("=" * 45)
    print("   CALCULADORA DE FECHAS")
    print("=" * 45)
    fecha = input("Ingresa la fecha objetivo (DD/MM/AAAA): ").strip()

    try:
        dias = calcular_dias_restantes(fecha)
        destino = datetime.strptime(fecha, "%d/%m/%Y").date()

        if dias > 0:
            print(f"\nFaltan {dias} día(s) para el {destino.strftime('%d/%m/%Y')}.")
        elif dias == 0:
            print(f"\n¡Hoy es {destino.strftime('%d/%m/%Y')}!")
        else:
            print(f"\nLa fecha {destino.strftime('%d/%m/%Y')} ya pasó hace {abs(dias)} día(s).")
    except ValueError:
        print("Formato de fecha inválido. Usa DD/MM/AAAA (ejemplo: 25/12/2025).")


if __name__ == "__main__":
    main()
