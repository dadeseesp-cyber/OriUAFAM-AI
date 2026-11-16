import streamlit as st

def mostrar_pensum(usuario=None):
    st.title("🗂️ Gestión del Pensum y Prerrequisitos")
    st.markdown("Consulta la malla curricular de tu carrera, los créditos de cada asignatura y las dependencias (prerrequisitos) necesarias para tu planificación académica.")

    # Selección de carrera / programa académico
    carrera = st.selectbox(
        "Selecciona el Programa Académico:",
        ["Licenciatura en Informática", "Licenciatura en Contabilidad (LCO)", "Licenciatura en Administración de Empresas (ADM)", "Ingeniería Agroforestal (IAG)", "Turismo (TUR)"]
    )

    st.divider()

    # Contenedor visual del pensum estructurado por cuatrimestres
    st.subheader(f"Malla Curricular: {carrera}")

    tab1, tab2, tab3 = st.tabs(["📌 Primer Cuatrimestre", "📌 Segundo Cuatrimestre", "📌 Tercer Cuatrimestre"])

    with tab1:
        st.markdown("### Primer Cuatrimestre")
        st.info("💡 **Consejo de Prerrequisitos:** Asegúrate de aprobar las materias básicas antes de avanzar a los niveles superiores.")
        
        st.markdown("""
        | Código | Asignatura | Créditos | Prerrequisito | Estado |
        | :--- | :--- | :---: | :--- | :---: |
        | INF-101 | Introducción a la Informática | 4 | Ninguno | Aprobada |
        | MAT-101 | Matemática Básica | 4 | Ninguno | Aprobada |
        | ESP-101 | Español I | 3 | Ninguno | Cursando |
        | SOC-101 | Sociología Rural | 2 | Ninguno | Pendiente |
        """)

    with tab2:
        st.markdown("### Segundo Cuatrimestre")
        st.markdown("""
        | Código | Asignatura | Créditos | Prerrequisito | Estado |
        | :--- | :--- | :---: | :--- | :---: |
        | INF-102 | Programación I | 4 | INF-101 | Pendiente |
        | MAT-102 | Cálculo I | 4 | MAT-101 | Pendiente |
        | ING-101 | Inglés Técnico I | 3 | Ninguno | Pendiente |
        """)

    with tab3:
        st.markdown("### Tercer Cuatrimestre y Ciclo Avanzado")
        st.markdown("Consulta aquí los bloques de materias especializadas, laboratorios, tesis de grado y pasantías institucionales correspondientes al cierre de tu ciclo de vida estudiantil.")
        st.markdown("""
        | Código | Asignatura | Créditos | Prerrequisito | Estado |
        | :--- | :--- | :---: | :--- | :---: |
        | INF-201 | Estructura de Datos | 4 | INF-102 | Pendiente |
        | INF-202 | Bases de Datos I | 4 | INF-102 | Pendiente |
        """)

    st.divider()

    # Sección interactiva de consulta de prerrequisitos
    st.subheader("🔍 Verificador de Dependencias de Asignaturas")
    materia_buscar = st.text_input("Ingresa el código o nombre de una asignatura (ej. INF-102):")

    if materia_buscar:
        if "INF-102" in materia_buscar.upper():
            st.success("📌 **Asignatura:** Programación I (4 Créditos)")
            st.write("**Prerrequisito obligatorio:** Debe haber cursado y aprobado **INF-101 (Introducción a la Informática)**.")
        elif "MAT-102" in materia_buscar.upper():
            st.success("📌 **Asignatura:** Cálculo I (4 Créditos)")
            st.write("**Prerrequisito obligatorio:** Debe haber cursado y aprobado **MAT-101 (Matemática Básica)**.")
        elif "INF-201" in materia_buscar.upper():
            st.success("📌 **Asignatura:** Estructura de Datos (4 Créditos)")
            st.write("**Prerrequisito obligatorio:** Debe haber cursado y aprobado **INF-102 (Programación I)**.")
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