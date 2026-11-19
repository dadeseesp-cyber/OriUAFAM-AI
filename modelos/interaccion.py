from database.conexion import conexion_bd


def registrar_interaccion(
    id_usuario: int,
    tipo_interaccion: str,
    contenido_consulta: str,
    contenido_respuesta: str = "",
) -> int:
  with conexion_bd() as conexion:
    cursor = conexion.execute(
        """
            INSERT INTO Interaccion (id_usuario, tipo_interaccion, contenido_consulta, contenido_respuesta)
            VALUES (?, ?, ?, ?)
        """,
        (
            id_usuario,
            tipo_interaccion,
            contenido_consulta,
            contenido_respuesta,
        ),
    )
    return cursor.lastrowid


def registrar_solicitud_cita(
    id_usuario: int, departamento: str, motivo: str
) -> int:
  """Registra una solicitud de cita u orientación personalizada como una interacción."""
  consulta = f"Solicitud de Cita - Departamento: {departamento}"
  respuesta = f"Motivo registrado: {motivo}"
  return registrar_interaccion(
      id_usuario=id_usuario,
      tipo_interaccion="cita",
      contenido_consulta=consulta,
      contenido_respuesta=respuesta,
  )


def obtener_historial_por_usuario(id_usuario: int, limite: int = 50):
  """Devuelve las interacciones del usuario de forma compatible."""
  with conexion_bd() as conexion:
    try:
      cursor = conexion.execute(
          """
                SELECT id_interaccion, tipo_interaccion, contenido_consulta AS consulta, 
                       contenido_respuesta AS respuesta, fecha_hora AS fecha_interaccion
                FROM Interaccion
                WHERE id_usuario = ?
                ORDER BY fecha_hora DESC
                LIMIT ?
            """,
          (id_usuario, limite),
      )
      return cursor.fetchall()
    except Exception:
      cursor = conexion.execute(
          """
                SELECT * FROM Interaccion 
                WHERE id_usuario = ? 
                LIMIT ?
            """,
          (id_usuario, limite),
      )
      return cursor.fetchall()