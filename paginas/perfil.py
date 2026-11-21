"""
perfil.py
Pantalla de perfil estudiantil — RF-02.
"""

import streamlit as st

from config import ETAPAS_CICLO_VIDA
from modelos.perfil_estudiante import (
    crear_perfil,
    obtener_perfil_por_usuario,
    actualizar_perfil,
)

CLAVE_MENSAJE_PERFIL = "mensaje_perfil_exito"


def _normalizar_carrera(carrera: str | None) -> str:
    if not carrera:
        return ""
    texto = carrera.strip()
    reemplazos = {
        "Informatica": "Informática",
        "informatica": "informática",
    }
    for incorrecto, correcto in reemplazos.items():
        if correcto not in texto and incorrecto in texto:
            texto = texto.replace(incorrecto, correcto)
    return texto


def _normalizar_etapa(etapa: str | None) -> str:
    if not etapa:
        return ETAPAS_CICLO_VIDA[0].capitalize()
    limpia = etapa.strip()
    for opcion in ETAPAS_CICLO_VIDA:
        if opcion.lower() == limpia.lower():
            return opcion.capitalize()
    return limpia.capitalize()


def _mostrar_mensaje_pendiente():
    mensaje = st.session_state.pop(CLAVE_MENSAJE_PERFIL, None)
    if mensaje:
        st.success(mensaje)


def mostrar_perfil(usuario: dict):
    st.header("Mi perfil estudiantil")
    _mostrar_mensaje_pendiente()

    id_usuario = usuario["id_usuario"]
    perfil = obtener_perfil_por_usuario(id_usuario)

    if perfil is None:
        st.info("Todavía no has completado tu perfil. Hazlo para continuar.")
        _formulario_crear_perfil(id_usuario)
    else:
        _formulario_editar_perfil(perfil)


def _formulario_crear_perfil(id_usuario: int):
    with st.form("formulario_crear_perfil"):
        matricula = st.text_input("Matrícula")
        carrera = st.text_input("Carrera")
        etapa_mostrar = st.selectbox(
            "Etapa de tu ciclo de vida estudiantil",
            [_normalizar_etapa(op) for op in ETAPAS_CICLO_VIDA],
        )
        intereses = st.text_area(
            "Intereses (separados por coma)",
            placeholder="Ej: inteligencia artificial, redes, bases de datos",
        )
        guardar = st.form_submit_button("Guardar perfil")

    if guardar:
        if not matricula.strip() or not carrera.strip():
            st.warning("Matrícula y carrera son obligatorias.")
        else:
            carrera_limpia = _normalizar_carrera(carrera)
            etapa_guardar = etapa_mostrar.lower()
            crear_perfil(
                id_usuario, matricula.strip(), carrera_limpia, etapa_guardar, intereses
            )
            st.session_state[CLAVE_MENSAJE_PERFIL] = "Perfil creado correctamente."
            st.rerun()


def _formulario_editar_perfil(perfil):
    st.write(f"**Matrícula:** {perfil['matricula']}")

    opciones_etapa = [_normalizar_etapa(op) for op in ETAPAS_CICLO_VIDA]
    carrera_mostrada = _normalizar_carrera(perfil["carrera"])
    etapa_mostrada = _normalizar_etapa(perfil["etapa_ciclo_vida"])

    with st.form("formulario_editar_perfil"):
        carrera = st.text_input("Carrera", value=carrera_mostrada)
        indice_etapa = (
            opciones_etapa.index(etapa_mostrada)
            if etapa_mostrada in opciones_etapa
            else 0
        )
        etapa_seleccionada = st.selectbox(
            "Etapa de tu ciclo de vida estudiantil",
            opciones_etapa,
            index=indice_etapa,
        )
        intereses = st.text_area("Intereses", value=perfil["intereses"] or "")
        guardar = st.form_submit_button("Actualizar perfil")

    if guardar:
        carrera_limpia = _normalizar_carrera(carrera)
        etapa_guardar = etapa_seleccionada.lower()
        actualizar_perfil(
            perfil["id_usuario"],
            carrera=carrera_limpia,
            etapa_ciclo_vida=etapa_guardar,
            intereses=intereses,
        )
        st.session_state[CLAVE_MENSAJE_PERFIL] = "Perfil actualizado correctamente."
        st.rerun()

    st.caption(f"Última actualización: {perfil['fecha_actualizacion']}")


# =========================================================================
# Lógica de renderizado para app.py / st.navigation
# =========================================================================
if "usuario_actual" in st.session_state and st.session_state["usuario_actual"]:
    mostrar_perfil(st.session_state["usuario_actual"])
elif "usuario" in st.session_state and st.session_state["usuario"]:
    mostrar_perfil(st.session_state["usuario"])
else:
    st.warning("Por favor, inicia sesión para ver tu perfil.")