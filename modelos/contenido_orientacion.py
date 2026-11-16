import sqlite3
import os
from database.conexion import obtener_conexion

# ==========================================
# FUNCIONES PARA EL TEST VOCACIONAL (RIASEC)
# ==========================================

def obtener_preguntas_vocacionales():
    """Obtiene las 20 preguntas del test RIASEC registradas en la base de datos."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id, pregunta, dimension FROM preguntas_riasec")
    preguntas = cursor.fetchall()
    conn.close()
    return preguntas

def guardar_resultado_vocacional(usuario_id, codigo_riasec, carrera_sugerida):
    """Guarda el resultado del test vocacional para un usuario determinado."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO resultados_vocacionales (usuario_id, codigo_riasec, carrera_sugerida)
        VALUES (?, ?, ?)
        """,
        (usuario_id, codigo_riasec, carrera_sugerida)
    )
    conn.commit()
    conn.close()

def obtener_historial_resultados(usuario_id):
    """Obtiene el historial de tests vocacionales realizados por el usuario."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT id, codigo_riasec, carrera_sugerida, fecha
        FROM resultados_vocacionales
        WHERE usuario_id = ?
        ORDER BY fecha DESC
        """,
        (usuario_id,)
    )
    resultados = cursor.fetchall()
    conn.close()
    return resultados


# ==========================================
# FUNCIONES DE ADMINISTRACIÓN Y CONTENIDOS
# ==========================================

def crear_contenido(titulo, categoria, descripcion, enlace_url=""):
    """Crea un nuevo recurso o contenido en la base de datos."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO recursos (titulo, categoria, descripcion, enlace_url)
        VALUES (?, ?, ?, ?)
        """,
        (titulo, categoria, descripcion, enlace_url)
    )
    conn.commit()
    conn.close()

def listar_todos_los_contenidos():
    """Obtiene todos los contenidos y recursos registrados."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, categoria, descripcion, enlace_url FROM recursos ORDER BY id DESC")
    contenidos = cursor.fetchall()
    conn.close()
    return contenidos

def eliminar_contenido(contenido_id):
    """Elimina un recurso o contenido por su ID."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM recursos WHERE id = ?", (contenido_id,))
    conn.commit()
    conn.close()