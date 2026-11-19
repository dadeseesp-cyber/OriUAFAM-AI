"""
derivacion.py
Capa de aplicación — operaciones sobre la entidad Derivacion.
Corresponde a RF-09 (mecanismo de derivación a atención humana).
"""

from database.conexion import conexion_bd

def registrar_derivacion(id_interaccion: int, motivo: str, canal_recomendado: str = "") -> int:
    with conexion_bd() as conexion:
        cursor = conexion.execute(
            """
            INSERT INTO Derivacion (id_interaccion, motivo, canal_recomendado)
            VALUES (?, ?, ?)
            """,
            (id_interaccion, motivo, canal_recomendado),
        )
        return cursor.lastrowid

def marcar_como_atendida(id_derivacion: int):
    with conexion_bd() as conexion:
        conexion.execute(
            "UPDATE Derivacion SET atendida = 1 WHERE id_derivacion = ?",
            (id_derivacion,),
        )

def listar_derivaciones_pendientes():
    """Pensado para el panel de administración (RF-10)."""
    with conexion_bd() as conexion:
        cursor = conexion.execute(
            "SELECT * FROM Derivacion WHERE atendida = 0 ORDER BY fecha DESC"
        )
        return cursor.fetchall()