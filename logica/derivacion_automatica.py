"""
derivacion_automatica.py
Capa de aplicación — lógica de apoyo a RF-09 (derivación).

Detecta, mediante palabras clave, cuándo una consulta académica o
vocacional parece exceder el alcance del asistente (por ejemplo,
situaciones relacionadas con abandonar la carrera o la universidad)
y debería derivarse hacia atención humana, tal como exige la tesis
en 4.3.6: "Cuando la situación se encuentre fuera del alcance del
prototipo, el sistema deberá recomendar la consulta con un
profesional...".

Es intencionalmente una regla simple por palabras clave, no un
análisis real de intención — coherente con el alcance de un
prototipo académico. Ajusta PALABRAS_CLAVE_DERIVACION según lo que
vayas observando durante las pruebas.
"""

PALABRAS_CLAVE_DERIVACION = (
    "abandonar la carrera",
    "abandonar mis estudios",
    "dejar la universidad",
    "retirarme de la universidad",
    "no puedo continuar mis estudios",
    "necesito hablar con alguien",
    "cambiarme de universidad",
    "dar de baja mis materias",
)


def requiere_derivacion(consulta: str) -> bool:
    consulta_normalizada = consulta.lower()
    return any(clave in consulta_normalizada for clave in PALABRAS_CLAVE_DERIVACION)
