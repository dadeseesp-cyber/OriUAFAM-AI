"""
recomendacion.py
Capa de aplicación — operaciones sobre la entidad Recomendacion.
Corresponde a RF-06 (motor de recomendaciones).
"""

from database.conexion import conexion_bd


def guardar_recomendacion(id_interaccion: int, categoria: str, contenido: str) -> int:
    with conexion_bd() as conexion:
        cursor = conexion.execute(
            """
            INSERT INTO Recomendacion (id_interaccion, categoria, contenido)
            VALUES (?, ?, ?)
            """,
            (id_interaccion, categoria, contenido),
        )
        return cursor.lastrowid


def obtener_recomendaciones_por_interaccion(id_interaccion: int):
    with conexion_bd() as conexion:
        cursor = conexion.execute(
            "SELECT * FROM Recomendacion WHERE id_interaccion = ?", (id_interaccion,)
        )
        return cursor.fetchall()
