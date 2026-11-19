import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "oriuafam.db")

RESPUESTAS_RAPIDAS = {
    "cita": "Puedes agendar tu cita desde el módulo correspondiente, seleccionando la fecha, hora y el motivo de tu consulta con el consejero UAFAM.",
    "calendario": "El calendario académico de la UAFAM opera bajo un régimen estricto de tres cuatrimestres (Enero-Abril, Mayo-Agosto y Septiembre-Diciembre), incluyendo fechas de inicio de docencia, exámenes parciales y finales. Puedes descargar el PDF oficial en el módulo de 'Orientación Académica'.",
    "reglamento": "El reglamento universitario UAFAM establece las normas de asistencia, índice académico mínimo requerido y los procesos institucionales del estudiantado.",
    "riasec": "El test RIASEC evalúa 6 áreas vocacionales (Realista, Investigativo, Artístico, Social, Emprendedor y Convencional) para sugerirte las carreras universitarias ideales de la UAFAM según tu perfil.",
    "modelo": "El modelo educativo de la UAFAM se estructura bajo un régimen cuatrimestral que optimiza la formación técnico-profesional y el acompañamiento integral del ciclo de vida estudiantil.",
    "cuatrimestre": "La UAFAM opera con tres cuatrimestres al año: el Primer Cuatrimestre (Enero-Abril), el Segundo Cuatrimestre (Mayo-Agosto) y el Tercer Cuatrimestre (Septiembre-Diciembre).",
    "pensum": "Puedes consultar la malla curricular, los créditos y las dependencias o prerrequisitos de cada asignatura en el módulo de 'Pensum y Prerrequisitos'.",
    "prerrequisito": "Los prerrequisitos son asignaturas obligatorias que debes aprobar antes de cursar materias de niveles superiores. Puedes verificarlos interactivamente en el módulo de Pensum."
}

def generar_respuesta_asistente(prompt, usuario_id=None):
    if not prompt or not prompt.strip():
        return "Por favorable, escribe una consulta válida."

    prompt_lower = prompt.lower()

    # 1. Buscar coincidencias en respuestas rápidas por palabras clave amplias
    for clave, respuesta in RESPUESTAS_RAPIDAS.items():
        if clave in prompt_lower:
            return respuesta

    # 2. Buscar en la base de datos si existe la tabla recursos
    try:
        if os.path.exists(DB_PATH):
            conn = sqlite3.connect(DB_PATH)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT titulo, descripcion FROM recursos")
            recursos = cursor.fetchall()
            conn.close()

            for rec in recursos:
                if any(p in rec["descripcion"].lower() for p in prompt_lower.split() if len(p) > 3):
                    return f"**{rec['titulo']}**:\n{rec['descripcion']}"
    except Exception:
        pass

    # 3. Respuesta de respaldo inteligente orientada al contexto UAFAM
    return (
        f"Entiendo tu consulta sobre '{prompt}'. Como asistente de OriUAFAM AI, "
        "estoy especializado en orientarte sobre el **Test RIASEC**, el **Calendario de 3 Cuatrimestres**, "
        "el **Pensum y Prerrequisitos**, o los reglamentos institucionales de la universidad. "
        "¿Te gustaría que profundicemos en alguna de estas áreas?"
    )