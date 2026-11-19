import datetime
import streamlit as st
import pandas as pd


CALENDARIO_2027 = [
    {
        "Periodo": "Cuatrimestre I - 2027",
        "Actividad": "Inscripción y selección de asignaturas",
        "Fecha / Ventana": "04 Ene - 12 Ene 2027",
        "Area": "Registro",
    },
    {
        "Periodo": "Cuatrimestre I - 2027",
        "Actividad": "Inicio de docencia regular",
        "Fecha / Ventana": "15 Ene 2027",
        "Area": "Docencia",
    },
    {
        "Periodo": "Cuatrimestre I - 2027",
        "Actividad": "Período de adición y retiro de materias",
        "Fecha / Ventana": "25 Ene - 03 Feb 2027",
        "Area": "Registro",
    },
    {
        "Periodo": "Cuatrimestre I - 2027",
        "Actividad": "Evaluaciones finales y cierre",
        "Fecha / Ventana": "19 Abr - 24 Abr 2027",
        "Area": "Evaluación",
    },
    {
        "Periodo": "Cuatrimestre II - 2027",
        "Actividad": "Inscripción y selección de asignaturas",
        "Fecha / Ventana": "03 May - 11 May 2027",
        "Area": "Registro",
    },
    {
        "Periodo": "Cuatrimestre II - 2027",
        "Actividad": "Inicio de docencia regular",
        "Fecha / Ventana": "14 May 2027",
        "Area": "Docencia",
    },
    {
        "Periodo": "Cuatrimestre II - 2027",
        "Actividad": "Evaluaciones finales y cierre",
        "Fecha / Ventana": "16 Ago - 21 Ago 2027",
        "Area": "Evaluación",
    },
    {
        "Periodo": "Cuatrimestre III - 2027",
        "Actividad": "Inscripción y selección de asignaturas",
        "Fecha / Ventana": "30 Ago - 07 Sep 2027",
        "Area": "Registro",
    },
    {
        "Periodo": "Cuatrimestre III - 2027",
        "Actividad": "Inicio de docencia regular",
        "Fecha / Ventana": "10 Sep 2027",
        "Area": "Docencia",
    },
    {
        "Periodo": "Cuatrimestre III - 2027",
        "Actividad": "Evaluaciones finales y cierre del año",
        "Fecha / Ventana": "13 Dic - 18 Dic 2027",
        "Area": "Evaluación",
    },
]


def _obtener_nombre_estudiante() -> str:
    for clave in ("usuario_nombre", "nombre_usuario", "user_name", "estudiante_nombre"):
        valor = st.session_state.get(clave)
        if isinstance(valor, str) and valor.strip():
            return valor.strip()

    usuario = st.session_state.get("usuario") or st.session_state.get("user")
    if isinstance(usuario, dict):
        for campo in ("nombre", "name", "full_name", "correo", "email"):
            valor = usuario.get(campo)
            if isinstance(valor, str) and valor.strip():
                return valor.strip()

    return "Estudiante UAFAM"


def _render_tab_calendario_2027() -> None:
    st.subheader("Cronograma Institucional 2027")

    periodos = ["Todos los períodos"] + sorted(
        {item["Periodo"] for item in CALENDARIO_2027},
        key=lambda p: (
            0 if "I - 2027" in p else 1 if "II - 2027" in p else 2
        ),
    )

    periodo_seleccionado = st.selectbox(
        "Filtrar por período académico:",
        options=periodos,
        index=0,
        key="filtro_periodo_2027",
    )

    if periodo_seleccionado == "Todos los períodos":
        datos_filtrados = CALENDARIO_2027
    else:
        datos_filtrados = [
            item for item in CALENDARIO_2027 if item["Periodo"] == periodo_seleccionado
        ]

    df_calendario = pd.DataFrame(datos_filtrados)
    st.dataframe(df_calendario, use_container_width=True, hide_index=True)


def _render_tab_planificacion() -> None:
    st.subheader("Planificación Académica")
    st.info(
        "Organiza tu carga académica de 2027 tomando en cuenta las fechas de inscripción, "
        "adición/retiro y cierres cuatrimestrales, así como los prerrequisitos de tu pensum."
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### Cuatrimestre I - 2027")
        st.write("- **Inscripción:** 04 Ene - 12 Ene 2027")
        st.write("- **Inicio de clases:** 15 Ene 2027")
        st.write("- **Adición y retiro:** 25 Ene - 03 Feb 2027")
        st.write("- **Cierre:** 19 Abr - 24 Abr 2027")

    with col2:
        st.markdown("#### Cuatrimestre II - 2027")
        st.write("- **Inscripción:** 03 May - 11 May 2027")
        st.write("- **Inicio de clases:** 14 May 2027")
        st.write("- **Cierre:** 16 Ago - 21 Ago 2027")

    with col3:
        st.markdown("#### Cuatrimestre III - 2027")
        st.write("- **Inscripción:** 30 Ago - 07 Sep 2027")
        st.write("- **Inicio de clases:** 10 Sep 2027")
        st.write("- **Cierre anual:** 13 Dic - 18 Dic 2027")

    st.markdown("---")
    st.markdown("#### Recomendaciones clave para planificar")
    st.write(
        "1. **Valida prerrequisitos antes de inscribir:** Revisa las asignaturas base y sus dependencias "
        "en *Pensum y Prerrequisitos* antes de abrir el período de inscripción."
    )
    st.write(
        "2. **Equilibra créditos y turno:** Combina asignaturas de mayor exigencia con materias introductorias "
        "o complementarias según tu disponibilidad horaria."
    )
    st.write(
        "3. **Aprovecha la ventana de adición y retiro:** Verifica tu carga real en las primeras semanas de docencia "
        "antes de que cierre el período correspondiente."
    )


def _render_tab_solicitud_cita() -> None:
    st.subheader("Solicitar Asesoría o Cita Académica")

    if "citas_academicas_2027" not in st.session_state:
        st.session_state["citas_academicas_2027"] = []

    with st.form("form_solicitud_cita_2027", clear_on_submit=False):
        col_izq, col_der = st.columns(2)

        with col_izq:
            motivo = st.selectbox(
                "Motivo de la cita:",
                options=[
                    "Revisión de avance y prerrequisitos",
                    "Planificación de carga académica 2027",
                    "Orientación vocacional y cambio de carrera",
                    "Consulta sobre calendario y trámites académicos",
                ],
                index=0,
            )

        with col_der:
            fecha_preferida = st.date_input(
                "Fecha preferida:",
                value=datetime.date(2027, 1, 15),
                min_value=datetime.date(2027, 1, 1),
                max_value=datetime.date(2027, 12, 31),
                format="YYYY/MM/DD",
            )

        col_mod, col_turno = st.columns(2)

        with col_mod:
            modalidad = st.radio(
                "Modalidad:",
                options=["Presencial", "Virtual"],
                horizontal=True,
                index=0,
            )

        with col_turno:
            turno = st.selectbox(
                "Turno preferido:",
                options=[
                    "Mañana (8:30 AM - 12:00 PM)",
                    "Tarde (2:00 PM - 5:30 PM)",
                    "Noche (6:00 PM - 8:30 PM)",
                ],
                index=0,
            )

        detalle = st.text_area(
            "Detalle o consulta breve (opcional):",
            placeholder="Ej. Quiero validar mis próximos créditos antes de iniciar el cuatrimestre...",
        )

        enviado = st.form_submit_button(
            "📌 Registrar Solicitud de Cita",
            use_container_width=True,
        )

    if enviado:
        nueva_cita = {
            "Estudiante": _obtener_nombre_estudiante(),
            "Motivo": motivo,
            "Modalidad": modalidad,
            "Fecha": fecha_preferida.strftime("%d/%m/%Y"),
            "Turno": turno,
            "Detalle": detalle.strip() if detalle else "-",
            "Estado": "Registrada",
        }
        st.session_state["citas_academicas_2027"].append(nueva_cita)
        st.success("Tu solicitud de cita académica ha sido registrada correctamente.")

    if st.session_state["citas_academicas_2027"]:
        st.markdown("### Citas registradas en esta sesión")
        df_citas = pd.DataFrame(st.session_state["citas_academicas_2027"])
        st.dataframe(df_citas, use_container_width=True, hide_index=True)


def render_orientacion_academica() -> None:
    st.title("🎓 Orientación Académica y Calendario 2027")
    st.write(
        "Consulta las fechas clave del calendario académico 2027, organiza tu planificación de asignaturas "
        "y solicita acompañamiento con orientación académica en UAFAM."
    )
    st.markdown("---")

    tab_calendario, tab_planificacion, tab_cita = st.tabs(
        [
            "📅 Calendario Académico 2027",
            "🕒 Planificación Académica",
            "🗓️ Solicitud de Cita",
        ]
    )

    with tab_calendario:
        _render_tab_calendario_2027()

    with tab_planificacion:
        _render_tab_planificacion()

    with tab_cita:
        _render_tab_solicitud_cita()


def main() -> None:
    render_orientacion_academica()


if __name__ == "__main__":
    main()
