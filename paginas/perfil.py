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


def mostrar_perfil(usuario: dict):
    st.header("Mi perfil estudiantil")

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
        etapa = st.selectbox("Etapa de tu ciclo de vida estudiantil", ETAPAS_CICLO_VIDA)
        intereses = st.text_area(
            "Intereses (separados por coma)",
            placeholder="Ej: inteligencia artificial, redes, bases de datos",
        )
        guardar = st.form_submit_button("Guardar perfil")

    if guardar:
        if not matricula or not carrera:
            st.warning("Matrícula y carrera son obligatorias.")
        else:
            crear_perfil(id_usuario, matricula, carrera, etapa, intereses)
            st.success("Perfil creado correctamente.")
            st.rerun()


def _formulario_editar_perfil(perfil):
    st.write(f"**Matrícula:** {perfil['matricula']}")

    with st.form("formulario_editar_perfil"):
        carrera = st.text_input("Carrera", value=perfil["carrera"] or "")
        etapa_actual = perfil["etapa_ciclo_vida"] or ETAPAS_CICLO_VIDA[0]
        indice_etapa = (
            ETAPAS_CICLO_VIDA.index(etapa_actual)
            if etapa_actual in ETAPAS_CICLO_VIDA
            else 0
        )
        etapa = st.selectbox(
            "Etapa de tu ciclo de vida estudiantil",
            ETAPAS_CICLO_VIDA,
            index=indice_etapa,
        )
        intereses = st.text_area("Intereses", value=perfil["intereses"] or "")
        guardar = st.form_submit_button("Actualizar perfil")

    if guardar:
        actualizar_perfil(
            perfil["id_usuario"],
            carrera=carrera,
            etapa_ciclo_vida=etapa,
            intereses=intereses,
        )
        st.success("Perfil actualizado correctamente.")
        st.rerun()

    st.caption(f"Última actualización: {perfil['fecha_actualizacion']}")


# =========================================================================
# Lógica de renderizado para app.py / st.navigation
# =================================5========================================
if "usuario_actual" in st.session_state and st.session_state["usuario_actual"]:
    mostrar_perfil(st.session_state["usuario_actual"])
elif "usuario" in st.session_state and st.session_state["usuario"]:
    mostrar_perfil(st.session_state["usuario"])
else:
    st.warning("Por favor, inicia sesión para ver tu perfil.")