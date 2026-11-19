from datetime import date, timedelta
import streamlit as st

CALENDARIO_2027 = [
    {"Periodo": "Cuatrimestre I - 2027", "Actividad": "Inscripción y selección de asignaturas", "Fecha / Ventana": "04 Ene - 12 Ene 2027", "Area": "Registro"},
    {"Periodo": "Cuatrimestre I - 2027", "Actividad": "Inicio de docencia regular", "Fecha / Ventana": "15 Ene 2027", "Area": "Docencia"},
    {"Periodo": "Cuatrimestre I - 2027", "Actividad": "Período de adición y retiro de materias", "Fecha / Ventana": "25 Ene - 03 Feb 2027", "Area": "Registro"},
    {"Periodo": "Cuatrimestre I - 2027", "Actividad": "Evaluaciones finales y cierre", "Fecha / Ventana": "19 Abr - 24 Abr 2027", "Area": "Evaluación"},
    {"Periodo": "Cuatrimestre II - 2027", "Actividad": "Inscripción y selección de asignaturas", "Fecha / Ventana": "03 May - 11 May 2027", "Area": "Registro"},
    {"Periodo": "Cuatrimestre II - 2027", "Actividad": "Inicio de docencia regular", "Fecha / Ventana": "14 May 2027", "Area": "Docencia"},
    {"Periodo": "Cuatrimestre II - 2027", "Actividad": "Evaluaciones finales y cierre", "Fecha / Ventana": "16 Ago - 21 Ago 2027", "Area": "Evaluación"},
    {"Periodo": "Cuatrimestre III - 2027", "Actividad": "Inscripción y selección de asignaturas", "Fecha / Ventana": "30 Ago - 07 Sep 2027", "Area": "Registro"},
    {"Periodo": "Cuatrimestre III - 2027", "Actividad": "Inicio de docencia regular", "Fecha / Ventana": "10 Sep 2027", "Area": "Docencia"},
    {"Periodo": "Cuatrimestre III - 2027", "Actividad": "Evaluaciones finales y cierre del año", "Fecha / Ventana": "13 Dic - 18 Dic 2027", "Area": "Evaluación"},
]


def _obtener_nombre_usuario(usuario):
    if isinstance(usuario, dict):
        return usuario.get("nombre") or usuario.get("usuario") or "Estudiante UAFAM"
    if isinstance(usuario, str) and usuario.strip():
        return usuario.strip()
    return "Estudiante UAFAM"


def mostrar_orientacion_academica(usuario=None):
    nombre_est = _obtener_nombre_usuario(usuario)

    st.title("🎓 Orientación Académica y Calendario 2027")
    st.markdown(
        "Consulta las fechas clave del calendario académico 2027, organiza tu planificación de asignaturas "
        "y solicita acompañamiento con orientación académica en UAFAM."
    )

    st.divider()

    tab1, tab2, tab3 = st.tabs([
        "📅 Calendario Académico 2027",
        "🧭 Planificación Académica",
        "🗓️ Solicitud de Cita",
    ])

    with tab1:
        st.subheader("Cronograma Institucional 2027")
        periodos = ["Todos los períodos"] + sorted(
            {item["Periodo"] for item in CALENDARIO_2027},
            key=lambda p: ["Cuatrimestre I - 2027", "Cuatrimestre II - 2027", "Cuatrimestre III - 2027"].index(p),
        )
        periodo_sel = st.selectbox("Filtrar por período académico:", periodos)

        eventos = (
            CALENDARIO_2027
            if periodo_sel == "Todos los períodos"
            else [item for item in CALENDARIO_2027 if item["Periodo"] == periodo_sel]
        )
        st.dataframe(eventos, use_container_width=True, hide_index=True)

    with tab2:
        st.subheader("Criterios para una Planificación Coherente")
        st.markdown(
            f"Hola **{nombre_est}**, para mantener un avance constante sin contratiempos administrativos:"
        )
        st.markdown(
            """
            * **Verifica prerrequisitos primero:** Confirma en *Gestión del Pensum y Prerrequisitos* que hayas completado las asignaturas base antes de inscribir materias avanzadas.
            * **Equilibra tu carga de créditos:** Combina asignaturas de alta exigencia o laboratorio con materias teóricas o complementarias según tu disponibilidad de tiempo.
            * **Respeta las ventanas del calendario:** Ten presentes las fechas de inscripción y retiro para evitar recargos o materias cursadas sin validez de avance.
            """
        )
        st.info("💡 Consejo: Si estás en etapas finales o preparando tu trabajo de grado, coordina con anticipación los requisitos de cierre de pensum.")

    with tab3:
        st.subheader("Solicitar Asesoría o Cita Académica")
        if "citas_academicas_2027" not in st.session_state:
            st.session_state["citas_academicas_2027"] = []

        with st.form("form_cita_academica", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                motivo = st.selectbox(
                    "Motivo de la cita:",
                    [
                        "Revisión de avance y prerrequisitos",
                        "Planificación de carga cuatrimestral",
                        "Orientación sobre trabajo de grado / pasantía",
                        "Consulta sobre calendario y trámites académicos",
                    ],
                )
                modalidad = st.radio("Modalidad:", ["Presencial", "Virtual"], horizontal=True)
            with col2:
                fecha_sugerida = st.date_input(
                    "Fecha preferida:",
                    value=date.today() + timedelta(days=2),
                    min_value=date.today(),
                )
                turno = st.selectbox("Turno preferido:", ["Mañana (8:30 AM - 12:00 PM)", "Tarde (2:00 PM - 5:30 PM)", "Noche (6:00 PM - 8:30 PM)"])

            comentario = st.text_area(
                "Detalle o consulta breve (opcional):",
                placeholder="Ej. Quiero validar mis próximos créditos antes de iniciar el cuatrimestre...",
            )
            enviada = st.form_submit_button("📌 Registrar Solicitud de Cita", use_container_width=True)

            if enviada:
                nueva_cita = {
                    "Estudiante": nombre_est,
                    "Motivo": motivo,
                    "Modalidad": modalidad,
                    "Fecha": fecha_sugerida.strftime("%d/%m/%Y"),
                    "Turno": turno,
                    "Estado": "Registrada",
                }
                st.session_state["citas_academicas_2027"].append(nueva_cita)
                st.success("✅ Tu solicitud de cita académica ha sido registrada correctamente.")

        if st.session_state["citas_academicas_2027"]:
            st.markdown("##### Citas registradas en esta sesión")
            st.dataframe(st.session_state["citas_academicas_2027"], use_container_width=True, hide_index=True)


# =========================================================================
# Lógica de renderizado para app.py / st.navigation
# =========================================================================
if __name__ == "__main__":
    mostrar_orientacion_academica()
else:
    usuario_activo = st.session_state.get("usuario_actual") or st.session_state.get("usuario")
    mostrar_orientacion_academica(usuario_activo)