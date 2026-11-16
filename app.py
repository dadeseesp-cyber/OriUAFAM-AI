import streamlit as st
from config import NOMBRE_APP
from paginas.login import mostrar_login

# Configuración global de la página
st.set_page_config(page_title=NOMBRE_APP, page_icon="🎓", layout="wide", initial_sidebar_state="expanded")

# --- CONTROL DE SESIÓN ---
if "usuario" not in st.session_state:
    st.session_state["usuario"] = None
if "rol" not in st.session_state:
    st.session_state["rol"] = None

if st.session_state["usuario"] is None:
    mostrar_login()
else:
    # --- DEFINICIÓN DE PÁGINAS Y MÓDULOS (CON NOMBRES EXACTOS DE TUS ARCHIVOS) ---
    p_perfil = st.Page("paginas/perfil.py", title="1. Mi Perfil y Expediente", icon="👤")
    p_riasec = st.Page("paginas/orientacion_vocacional.py", title="2. Orientación RIASEC", icon="🧭")
    p_academica = st.Page("paginas/orientacion_academica.py", title="3. Orientación Académica", icon="📚")
    p_pensum = st.Page("paginas/pensum_prerrequisitos.py", title="4. Pensum y Prerrequisitos", icon="📁")
    
    # Asistente oficial Ori
    p_asistente = st.Page("paginas/asistente.py", title="Ori - Asistente IA", icon="🤖")
    
    p_historial = st.Page("paginas/historial.py", title="6. Ciclo de Vida e Historial", icon="📈")
    p_recursos = st.Page("paginas/recursos.py", title="7. Centro de Información", icon="🏛️")
    p_admin = st.Page("paginas/administracion.py", title="⚙️ Administración", icon="🛠️")

    # --- NAVEGACIÓN AGRUPADA EN EL MENÚ LATERAL ---
    navegacion = st.navigation({
        "Identidad Estudiantil": [p_perfil],
        "Orientación": [p_riasec, p_academica],
        "Planificación Académica": [p_pensum],
        "Inteligencia Artificial": [p_asistente],
        "Seguimiento y Registro": [p_historial],
        "Recursos Institucionales": [p_recursos],
        "Gestión del Sistema": [p_admin]
    })

    # --- BARRA LATERAL ---
    with st.sidebar:
        st.divider()
        if st.button("Cerrar sesión", type="secondary", use_container_width=True):
            st.session_state["usuario"] = None
            st.session_state["rol"] = None
            st.rerun()
        st.caption("Universidad Agroforestal Fernando Arturo de Meriño (UAFAM)")

    # --- BANNER SUPERIOR INSTITUCIONAL (UAFAM) ---
    usuario_actual = st.session_state.get("usuario")
    nombre_usuario = usuario_actual.get("nombre", "Estudiante") if isinstance(usuario_actual, dict) else "Estudiante UAFAM"
    rol_usuario = usuario_actual.get("rol", "estudiante").capitalize() if isinstance(usuario_actual, dict) else "Estudiante"

    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 50%, #2563EB 100%); padding: 18px 26px; border-radius: 12px; color: white; margin-bottom: 22px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 6px 12px -2px rgba(30, 58, 138, 0.3); border-bottom: 4px solid #60A5FA;">
            <div style="display: flex; align-items: center; gap: 16px;">
                <div style="background-color: rgba(255, 255, 255, 0.15); padding: 12px; border-radius: 10px; border: 1px solid rgba(255, 255, 255, 0.3); text-align: center; min-width: 55px;">
                    <span style="font-size: 1.6rem;">🏛️</span>
                </div>
                <div>
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <span style="background-color: #3B82F6; color: white; font-size: 0.65rem; font-weight: bold; padding: 2px 8px; border-radius: 4px; letter-spacing: 0.5px;">UAFAM</span>
                        <h2 style="margin: 0; font-size: 1.35rem; color: white; font-weight: 700;">OriUAFAM AI</h2>
                    </div>
                    <p style="margin: 4px 0 0 0; font-size: 0.85rem; color: #93C5FD; font-weight: 500;">Plataforma de Acompañamiento para el Ciclo de Vida Estudiantil mediante Orientación Académica y Vocacional</p>
                </div>
            </div>
            <div style="text-align: right; background-color: rgba(15, 23, 42, 0.4); padding: 10px 18px; border-radius: 8px; border: 1px solid rgba(255, 255, 255, 0.2);">
                <p style="margin: 0; font-size: 0.7rem; color: #93C5FD; text-transform: uppercase; letter-spacing: 0.5px; font-weight: bold;">Sesión Activa</p>
                <p style="margin: 2px 0 0 0; font-size: 0.95rem; font-weight: bold; color: white;">{nombre_usuario}</p>
                <p style="margin: 0; font-size: 0.75rem; color: #CBD5E1;">{rol_usuario} UAFAM</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Ejecutar la página seleccionada en la navegación
    navegacion.run()