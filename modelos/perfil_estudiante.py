"""
perfil_estudiante.py
Capa de aplicación — operaciones sobre la entidad PerfilEstudiante.
Corresponde a RF-02 (perfil estudiantil y base de datos).
"""

from database.conexion import conexion_bd


def crear_perfil(id_usuario: int, matricula: str, carrera: str,
                  etapa_ciclo_vida: str, intereses: str = "") -> int:
    with conexion_bd() as conexion:
        cursor = conexion.execute(
            """
            INSERT INTO PerfilEstudiante
                (id_usuario, matricula, carrera, etapa_ciclo_vida, intereses)
            VALUES (?, ?, ?, ?, ?)
            """,
            (id_usuario, matricula, carrera, etapa_ciclo_vida, intereses),
        )
        return cursor.lastrowid


def obtener_perfil_por_usuario(id_usuario: int):
    with conexion_bd() as conexion:
        cursor = conexion.execute(
            "SELECT * FROM PerfilEstudiante WHERE id_usuario = ?", (id_usuario,)
        )
        return cursor.fetchone()


def actualizar_perfil(id_usuario: int, **campos):
    """
    Actualiza cualquier combinación de columnas del perfil.
    Ejemplo: actualizar_perfil(5, carrera="Informática", intereses="IA, redes")
    """
    if not campos:
        return
    columnas = ", ".join(f"{clave} = ?" for clave in campos)
    valores = list(campos.values()) + [id_usuario]
    with conexion_bd() as conexion:
        conexion.execute(
            f"""
            UPDATE PerfilEstudiante
            SET {columnas}, fecha_actualizacion = datetime('now')
            WHERE id_usuario = ?
            """,
            valores,
        )
