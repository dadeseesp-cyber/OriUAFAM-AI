"""
usuario.py
Capa de aplicación — operaciones sobre la entidad Usuario.

Corresponde a RF-01 (módulo de autenticación) según la tabla de
relación entre requisitos y diseño (Cap. IV, 4.3.8) de la tesis.

Nota de seguridad: aquí solo se usa un hash simple (sha256) como
punto de partida. La tesis (2.4.6) exige "protección de las
credenciales", así que antes de la versión final conviene migrar a
un hash con "sal" pensado para contraseñas (por ejemplo, la librería
'bcrypt' o 'passlib'). Lo dejamos como nota pendiente.
"""

import hashlib

from database.conexion import conexion_bd


def _hash_contrasena(contrasena: str) -> str:
    """Convierte una contraseña en texto plano a un hash SHA-256."""
    return hashlib.sha256(contrasena.encode("utf-8")).hexdigest()


def crear_usuario(nombre: str, correo: str, contrasena: str, rol: str = "estudiante") -> int:
    """Crea un nuevo usuario y devuelve su id_usuario."""
    contrasena_hash = _hash_contrasena(contrasena)
    with conexion_bd() as conexion:
        cursor = conexion.execute(
            """
            INSERT INTO Usuario (nombre, correo, contrasena_hash, rol)
            VALUES (?, ?, ?, ?)
            """,
            (nombre, correo, contrasena_hash, rol),
        )
        return cursor.lastrowid


def obtener_usuario_por_correo(correo: str):
    """Devuelve la fila del usuario con ese correo, o None si no existe."""
    with conexion_bd() as conexion:
        cursor = conexion.execute(
            "SELECT * FROM Usuario WHERE correo = ?", (correo,)
        )
        return cursor.fetchone()


def verificar_credenciales(correo: str, contrasena: str):
    """
    Verifica correo + contraseña. Devuelve la fila del usuario si
    coinciden, o None si el usuario no existe o la contraseña es
    incorrecta.
    """
    usuario = obtener_usuario_por_correo(correo)
    if usuario is None:
        return None
    if usuario["contrasena_hash"] == _hash_contrasena(contrasena):
        return usuario
    return None


def listar_usuarios():
    """Lista todos los usuarios (pensado para el panel de administración, RF-10)."""
    with conexion_bd() as conexion:
        cursor = conexion.execute("SELECT * FROM Usuario ORDER BY fecha_registro DESC")
        return cursor.fetchall()
