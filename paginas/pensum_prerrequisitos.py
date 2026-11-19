import streamlit as st

PENSUM_POR_CARRERA = {
    "Licenciatura en Informática": {
        "Primer Cuatrimestre": [
            {"codigo": "INF-101", "nombre": "Introducción a la Informática", "creditos": 4, "prerrequisito": "Ninguno", "estado": "Aprobada"},
            {"codigo": "MAT-101", "nombre": "Matemática Básica", "creditos": 4, "prerrequisito": "Ninguno", "estado": "Aprobada"},
            {"codigo": "ESP-101", "nombre": "Español I", "creditos": 3, "prerrequisito": "Ninguno", "estado": "Cursando"},
            {"codigo": "SOC-101", "nombre": "Sociología Rural", "creditos": 2, "prerrequisito": "Ninguno", "estado": "Pendiente"},
        ],
        "Segundo Cuatrimestre": [
            {"codigo": "INF-102", "nombre": "Programación I", "creditos": 4, "prerrequisito": "INF-101", "estado": "Pendiente"},
            {"codigo": "MAT-102", "nombre": "Cálculo I", "creditos": 4, "prerrequisito": "MAT-101", "estado": "Pendiente"},
            {"codigo": "ING-101", "nombre": "Inglés Técnico I", "creditos": 3, "prerrequisito": "Ninguno", "estado": "Pendiente"},
        ],
        "Tercer Cuatrimestre": [
            {"codigo": "INF-201", "nombre": "Estructura de Datos", "creditos": 4, "prerrequisito": "INF-102", "estado": "Pendiente"},
            {"codigo": "INF-202", "nombre": "Bases de Datos I", "creditos": 4, "prerrequisito": "INF-102", "estado": "Pendiente"},
        ],
    },
    "Licenciatura en Contabilidad (LCO)": {
        "Primer Cuatrimestre": [
            {"codigo": "CON-101", "nombre": "Contabilidad General I", "creditos": 4, "prerrequisito": "Ninguno", "estado": "Aprobada"},
            {"codigo": "MAT-101", "nombre": "Matemática Básica", "creditos": 4, "prerrequisito": "Ninguno", "estado": "Aprobada"},
            {"codigo": "ESP-101", "nombre": "Español I", "creditos": 3, "prerrequisito": "Ninguno", "estado": "Cursando"},
        ],
        "Segundo Cuatrimestre": [
            {"codigo": "CON-102", "nombre": "Contabilidad General II", "creditos": 4, "prerrequisito": "CON-101", "estado": "Pendiente"},
            {"codigo": "MFN-101", "nombre": "Matemática Financiera", "creditos": 3, "prerrequisito": "MAT-101", "estado": "Pendiente"},
            {"codigo": "ECO-101", "nombre": "Microeconomía", "creditos": 3, "prerrequisito": "Ninguno", "estado": "Pendiente"},
        ],
        "Tercer Cuatrimestre": [
            {"codigo": "CON-201", "nombre": "Contabilidad de Costos I", "creditos": 4, "prerrequisito": "CON-102", "estado": "Pendiente"},
            {"codigo": "FIS-101", "nombre": "Legislación Tributaria", "creditos": 3, "prerrequisito": "CON-102", "estado": "Pendiente"},
        ],
    },
    "Licenciatura en Administración de Empresas (ADM)": {
        "Primer Cuatrimestre": [
            {"codigo": "ADM-101", "nombre": "Principios de Administración", "creditos": 4, "prerrequisito": "Ninguno", "estado": "Aprobada"},
            {"codigo": "MAT-101", "nombre": "Matemática Básica", "creditos": 4, "prerrequisito": "Ninguno", "estado": "Aprobada"},
            {"codigo": "ESP-101", "nombre": "Español I", "creditos": 3, "prerrequisito": "Ninguno", "estado": "Cursando"},
        ],
        "Segundo Cuatrimestre": [
            {"codigo": "ADM-102", "nombre": "Proceso Administrativo", "creditos": 4, "prerrequisito": "ADM-101", "estado": "Pendiente"},
            {"codigo": "ECO-101", "nombre": "Microeconomía", "creditos": 3, "prerrequisito": "Ninguno", "estado": "Pendiente"},
            {"codigo": "MKT-101", "nombre": "Fundamentos de Mercadeo", "creditos": 3, "prerrequisito": "ADM-101", "estado": "Pendiente"},
        ],
        "Tercer Cuatrimestre": [
            {"codigo": "ADM-201", "nombre": "Gestión del Talento Humano", "creditos": 3, "prerrequisito": "ADM-102", "estado": "Pendiente"},
            {"codigo": "FIN-101", "nombre": "Finanzas Corporativas I", "creditos": 4, "prerrequisito": "ECO-101", "estado": "Pendiente"},
        ],
    },
    "Ingeniería Agroforestal (IAG)": {
        "Primer Cuatrimestre": [
            {"codigo": "AGR-101", "nombre": "Botánica General", "creditos": 4, "prerrequisito": "Ninguno", "estado": "Aprobada"},
            {"codigo": "MAT-101", "nombre": "Matemática Básica", "creditos": 4, "prerrequisito": "Ninguno", "estado": "Aprobada"},
            {"codigo": "QUI-101", "nombre": "Química General", "creditos": 4, "prerrequisito": "Ninguno", "estado": "Cursando"},
        ],
        "Segundo Cuatrimestre": [
            {"codigo": "FOR-101", "nombre": "Dendrología", "creditos": 4, "prerrequisito": "AGR-101", "estado": "Pendiente"},
            {"codigo": "SUE-101", "nombre": "Ciencia del Suelo", "creditos": 4, "prerrequisito": "QUI-101", "estado": "Pendiente"},
            {"codigo": "MAT-102", "nombre": "Cálculo I", "creditos": 4, "prerrequisito": "MAT-101", "estado": "Pendiente"},
        ],
        "Tercer Cuatrimestre": [
            {"codigo": "AGF-201", "nombre": "Sistemas Agroforestales", "creditos": 4, "prerrequisito": "FOR-101", "estado": "Pendiente"},
            {"codigo": "HID-101", "nombre": "Hidrología y Conservación", "creditos": 3, "prerrequisito": "SUE-101", "estado": "Pendiente"},
        ],
    },
    "Turismo (TUR)": {
        "Primer Cuatrimestre": [
            {"codigo": "TUR-101", "nombre": "Introducción al Turismo", "creditos": 3, "prerrequisito": "Ninguno", "estado": "Aprobada"},
            {"codigo": "GEO-101", "nombre": "Geografía Turística", "creditos": 3, "prerrequisito": "Ninguno", "estado": "Aprobada"},
            {"codigo": "ESP-101", "nombre": "Español I", "creditos": 3, "prerrequisito": "Ninguno", "estado": "Cursando"},
        ],
        "Segundo Cuatrimestre": [
            {"codigo": "TUR-102", "nombre": "Gestión Hotelera y Servicios", "creditos": 4, "prerrequisito": "TUR-101", "estado": "Pendiente"},
            {"codigo": "ECO-101", "nombre": "Ecoturismo y Sostenibilidad", "creditos": 3, "prerrequisito": "GEO-101", "estado": "Pendiente"},
            {"codigo": "ING-101", "nombre": "Inglés Aplicado al Turismo I", "creditos": 3, "prerrequisito": "Ninguno", "estado": "Pendiente"},
        ],
        "Tercer Cuatrimestre": [
            {"codigo": "TUR-201", "nombre": "Diseño de Productos Turísticos", "creditos": 4, "prerrequisito": "TUR-102", "estado": "Pendiente"},
            {"codigo": "PAT-101", "nombre": "Patrimonio Cultural y Natural", "creditos": 3, "prerrequisito": "GEO-101", "estado": "Pendiente"},
        ],
    },
}


def _render_tabla_asignaturas(materias):
    filas = [
        "| Código | Asignatura | Créditos | Prerrequisito | Estado |",
        "| :--- | :--- | :---: | :--- | :---: |",
    ]
    for m in materias:
        filas.append(
            f"| {m['codigo']} | {m['nombre']} | {m['creditos']} | {m['prerrequisito']} | {m['estado']} |"
        )
    st.markdown("\n".join(filas))


def mostrar_pensum(usuario=None):
    st.title("🗂️ Gestión del Pensum y Prerrequisitos")
    st.markdown(
        "Consulta la malla curricular de tu carrera, los créditos de cada asignatura y las dependencias "
        "(prerrequisitos) necesarias para tu planificación académica."
    )

    carrera = st.selectbox(
        "Selecciona el Programa Académico:",
        list(PENSUM_POR_CARRERA.keys()),
    )

    malla = PENSUM_POR_CARRERA[carrera]
    todas_las_materias = [m for bloque in malla.values() for m in bloque]

    st.divider()
    st.subheader(f"Malla Curricular: {carrera}")

    cuatrimestres = list(malla.keys())
    tab1, tab2, tab3 = st.tabs(["📌 Primer Cuatrimestre", "📌 Segundo Cuatrimestre", "📌 Tercer Cuatrimestre"])

    with tab1:
        st.markdown("### Primer Cuatrimestre")
        st.info("💡 **Consejo de Prerrequisitos:** Asegúrate de aprobar las materias básicas antes de avanzar a los niveles superiores.")
        _render_tabla_asignaturas(malla[cuatrimestres[0]])

    with tab2:
        st.markdown("### Segundo Cuatrimestre")
        _render_tabla_asignaturas(malla[cuatrimestres[1]])

    with tab3:
        st.markdown("### Tercer Cuatrimestre y Ciclo Avanzado")
        st.markdown(
            "Consulta aquí los bloques de materias especializadas, laboratorios, tesis de grado y "
            "pasantías institucionales correspondientes al cierre de tu ciclo de vida estudiantil."
        )
        _render_tabla_asignaturas(malla[cuatrimestres[2]])

    st.divider()

    st.subheader("🔍 Verificador de Dependencias de Asignaturas")
    materia_buscar = st.text_input("Ingresa el código o nombre de una asignatura (ej. INF-102):").strip()

    if materia_buscar:
        termino = materia_buscar.lower()
        coincidencias = [
            m for m in todas_las_materias
            if termino in m["codigo"].lower() or termino in m["nombre"].lower()
        ]

        if coincidencias:
            for mat in coincidencias:
                st.success(f"📌 **Asignatura:** {mat['nombre']} ({mat['codigo']}) — {mat['creditos']} Créditos")
                if mat["prerrequisito"] == "Ninguno":
                    st.write("**Prerrequisito:** Sin restricción de prerrequisito.")
                else:
                    st.write(
                        f"**Prerrequisito obligatorio:** Debe haber cursado y aprobado "
                        f"**{mat['prerrequisito']}**."
                    )
        else:
            st.info("Asignatura consultada dentro del catálogo general del pensum UAFAM. Sin restricciones especiales adicionales.")


# =========================================================================
# Lógica de renderizado para app.py / st.navigation
# =========================================================================
if __name__ == "__main__":
    mostrar_pensum()
else:
    usuario_activo = st.session_state.get("usuario_actual") or st.session_state.get("usuario")
    mostrar_pensum(usuario_activo)
