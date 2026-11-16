"""
administracion.py
Panel de administración básico — RF-10.

app.py solo muestra la opción "Administración" en el menú si el
usuario tiene rol 'administrador', pero se repite la verificación
aquí como segunda barrera de seguridad.
"""

import streamlit as st

from modelos.usuario import listar_usuarios
from modelos.derivacion import listar_derivaciones_pendientes, marcar_como_atendida
from modelos.contenido_orientacion import crear_contenido, listar_todos_los_contenidos


def mostrar_administracion(usuario: dict):
    if usuario.get("rol") != "administrador":
        st.error("No tienes permisos para ver esta sección.")
        return

    st.header("Panel de administración")

    pestaña_usuarios, pestaña_derivaciones, pestaña_contenidos = st.tabs(
        ["Usuarios", "Derivaciones pendientes", "Contenidos de orientación"]
    )

    # -------------------- Usuarios --------------------
    with pestaña_usuarios:
        usuarios = listar_usuarios()
        st.write(f"Total de usuarios registrados: {len(usuarios)}")
        for u in usuarios:
            estado = "activo" if u["activo"] else "inactivo"
            st.write(f"- **{u['nombre']}** ({u['correo']}) — rol: {u['rol']} — {estado}")

    # -------------------- Derivaciones pendientes --------------------
    with pestaña_derivaciones:
        derivaciones = listar_derivaciones_pendientes()
        if not derivaciones:
            st.success("No hay derivaciones pendientes.")
        else:
            for d in derivaciones:
                with st.expander(f"Derivación #{d['id_derivacion']} — {d['fecha']}"):
                    st.write(f"**Motivo:** {d['motivo']}")
                    st.write(f"**Canal recomendado:** {d['canal_recomendado'] or 'No especificado'}")
                    if st.button("Marcar como atendida", key=f"atender_{d['id_derivacion']}"):
                        marcar_como_atendida(d["id_derivacion"])
                        st.rerun()

    # -------------------- Contenidos de orientación --------------------
    with pestaña_contenidos:
        st.subheader("Contenidos existentes")
        contenidos = listar_todos_los_contenidos()
        st.write(f"Total: {len(contenidos)}")

        st.subheader("Agregar nuevo contenido")
        with st.form("formulario_nuevo_contenido"):
            titulo = st.text_input("Título")
            descripcion = st.text_area("Descripción")
            categoria = st.selectbox("Categoría", ["academica", "vocacional"])
            tipo_recurso = st.selectbox("Tipo de recurso", ["articulo", "enlace", "video", "documento"])
            url_o_ruta = st.text_input("URL o ruta (opcional)")
            guardar = st.form_submit_button("Guardar contenido")

        if guardar:
            if not titulo:
                st.warning("El título es obligatorio.")
            else:
                crear_contenido(titulo, descripcion, categoria, tipo_recurso, url_o_ruta)
                st.success("Contenido agregado correctamente.")
                st.rerun()
