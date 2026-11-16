import sqlite3
from database.conexion import obtener_conexion

def sembrar_datos():
    conn = obtener_conexion()
    cursor = conn.cursor()

    # 1. Crear tabla de recursos si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            categoria TEXT NOT NULL,
            contenido TEXT NOT NULL,
            fecha_publicacion DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # 2. Limpiar registros antiguos para evitar duplicados
    cursor.execute("DELETE FROM recursos")

    # 3. Insertar información de orientación institucional (RF-07)
    recursos_iniciales = [
        (
            "Requisitos de Monográfico o Tesis",
            "General",
            "Para solicitar la inscripción del Proyecto de Grado, Monográfico o Tesis en la UAFAM, debes cumplir con los siguientes requisitos:\n"
            "1. Tener aprobadas el 100% de las asignaturas del pensum de tu carrera.\n"
            "2. Estar al día con los pagos y obligaciones financieras en la universidad.\n"
            "3. Presentar carta de saldo y certificación de estudios expedida por Registro.\n"
            "4. Someter la propuesta de tema ante la Dirección Académica para su aprobación."
        ),
        (
            "Agendamiento de Citas de Orientación",
            "General",
            "Para agendar una cita presencial o virtual de orientación académica o vocacional:\n"
            "1. Accede al formulario en el módulo de Asistente de OriUAFAM AI.\n"
            "2. Selecciona el motivo de consulta, tu disponibilidad de horario y la fecha deseada.\n"
            "3. La solicitud quedará registrada en el sistema y será revisada por el departamento de orientación."
        ),
        (
            "Reglamento Académico e Inscripciones",
            "General",
            "El proceso de selección y selección de asignaturas se realiza según el calendario académico publicado por la vicerrectoría. Se requiere un índice académico mínimo de 2.0 para mantener la condición de estudiante regular."
        )
    ]

    cursor.executemany("""
        INSERT INTO recursos (titulo, categoria, contenido)
        VALUES (?, ?, ?)
    """, recursos_iniciales)

    conn.commit()
    conn.close()
    print("✅ Datos de orientación y recursos sembrados correctamente en database/oriuafam.db")

if __name__ == "__main__":
    sembrar_datos()