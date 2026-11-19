"""
motor_recomendaciones.py
Capa de aplicación — lógica de RF-06 (motor de recomendaciones).

Esta es una versión DELIBERADAMENTE simple: busca contenido cargado
en ContenidoOrientacion para la categoría solicitada y lo devuelve
como recomendación. Es un punto de partida coherente con lo que tu
tesis describe como "motor de inferencia basado en reglas" — todavía
sin el componente de IA conversacional (eso es RF-05, capa de IA,
pendiente).

Cuando integres el servicio de IA real, este archivo es el lugar
natural para decidir: ¿la recomendación sale de reglas simples, de
IA, o de una combinación de ambas?
"""

from modelos.contenido_orientacion import listar_contenidos_por_categoria


def generar_recomendacion_simple(categoria: str, consulta: str) -> str:
    """
    Regla simple: si hay contenido cargado para la categoría, recomienda
    el más reciente. Si no hay nada cargado, devuelve un mensaje
    honesto en vez de inventar una recomendación.
    """
    contenidos = listar_contenidos_por_categoria(categoria)

    if not contenidos:
        return (
            "Todavía no hay contenido de orientación cargado para esta "
            "categoría. Esta respuesta es un marcador de posición mientras "
            "se completa el módulo de recursos (RF-07)."
        )

    contenido_sugerido = contenidos[0]
    recomendacion = f"Basado en tu consulta, te recomendamos revisar: **{contenido_sugerido['titulo']}**."
    if contenido_sugerido["descripcion"]:
        recomendacion += f"\n\n{contenido_sugerido['descripcion']}"

    return recomendacion
