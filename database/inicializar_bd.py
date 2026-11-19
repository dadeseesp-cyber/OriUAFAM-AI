"""
inicializar_bd.py
Script que se ejecuta UNA VEZ (o cada vez que cambies el esquema)
para crear el archivo oriuafam.db con todas las tablas definidas
en esquema.sql.

Cómo ejecutarlo desde la raíz del proyecto (en la terminal de VS Code):

    python -m database.inicializar_bd

Es seguro volver a ejecutarlo: todas las tablas usan
"CREATE TABLE IF NOT EXISTS", así que no borra datos que ya existan.
"""

import os
import sys

# Permite ejecutar este archivo directamente sin problemas de rutas
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import ESQUEMA_SQL_PATH, DB_PATH
from database.conexion import obtener_conexion


def inicializar_base_de_datos():
    print(f"Leyendo esquema desde: {ESQUEMA_SQL_PATH}")

    with open(ESQUEMA_SQL_PATH, "r", encoding="utf-8") as archivo:
        script_sql = archivo.read()

    conexion = obtener_conexion()
    try:
        conexion.executescript(script_sql)
        conexion.commit()
        print(f"Base de datos creada/actualizada correctamente en: {DB_PATH}")
    finally:
        conexion.close()


def mostrar_tablas_creadas():
    """Función de verificación rápida: lista las tablas que existen."""
    conexion = obtener_conexion()
    try:
        cursor = conexion.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
        )
        tablas = [fila["name"] for fila in cursor.fetchall()]
        print("Tablas encontradas en la base de datos:")
        for tabla in tablas:
            print(f"  - {tabla}")
    finally:
        conexion.close()


if __name__ == "__main__":
    inicializar_base_de_datos()
    mostrar_tablas_creadas()
