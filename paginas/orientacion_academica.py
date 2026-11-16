import os
import streamlit as st

def mostrar_centro_informacion(usuario=None):
    st.title("🏛️ Centro de Información - UAFAM")
    st.write("Repositorio centralizado de recursos bibliográficos, normativas institucionales y servicios de apoyo a la investigación.")

    st.markdown("---")
    
    # Pestañas interactivas del centro de información
    tab1, tab2, tab3 = st.tabs(["📚 Biblioteca Digital", "📜 Reglamentos y Normativas", "🕒 Horarios y Servicios"])

    with tab1:
        st.subheader("Catálogo y Recursos Bibliográficos")
        st.write("Accede a bases de datos científicas, libros electrónicos y revistas especializadas para tu tesis y asignaturas.")
        
        # Buscador interactivo de recursos
        busqueda = st.text_input("🔍 Buscar libros, tesis o artículos en el repositorio:", placeholder="Ej. Programación Python, Inteligencia Artificial, Metodología...")
        if busqueda:
            st.info(f"Mostrando resultados de búsqueda para: **{busqueda}**")
            st.markdown("""
            * **Introducción a la Inteligencia Artificial en la Educación** (Autor: D. UAFAM, 2025) - *Disponible en línea*
            * **Metodología de Investigación Científica y Tecnológica** (Autor: C. Pérez, 2024) - *Acceso institucional*
            * **Guía de Desarrollo en Python y Streamlit para Tesis** (Autor: UAFAM Tech, 2026) - *Descarga directa*
            """)
        else:
            st.markdown("""
            ### 📌 Destacados para Estudiantes
            * 📖 **Normas APA 7ma Edición:** Guía oficial para la presentación de trabajos de grado y tesis.
            * 💻 **Repositorio de Tesis Anteriores:** Consulta proyectos de software y tesis de grado de ingeniería.
            * 🌐 **Bases de Datos Externas:** Acceso preferencial a JSTOR, IEEE y Dialnet con tus credenciales institucionales.
            """)

    with tab2:
        st.subheader("Normativa Académica e Institucional")
        st.write("Documentos legales y reglamentarios que rigen la vida estudiantil, docente y de investigación.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("##### 📌 Reglamentos Estudiantiles")
            st.download_button(
                label="📥 Descargar Reglamento Estudiantil (PDF)",
                data=b"Contenido simulado del reglamento estudiantil UAFAM",
                file_name="Reglamento_Estudiantil_UAFAM.pdf",
                mime="application/pdf",
                use_container_width=True
            )
            st.download_button(
                label="📥 Descargar Guía de Trabajos de Grado (PDF)",
                data=b"Contenido simulado de la guia de tesis",
                file_name="Guia_Trabajos_Grado_UAFAM.pdf",
                mime="application/pdf",
                use_container_width=True
            )
        with col2:
            st.markdown("##### 📌 Protocolos y Estatutos")
            st.download_button(
                label="📥 Descargar Estatuto Orgánico (PDF)",
                data=b"Contenido simulado del estatuto",
                file_name="Estatuto_Organico_UAFAM.pdf",
                mime="application/pdf",
                use_container_width=True
            )

    with tab3:
        st.subheader("Horarios de Atención y Servicios")
        st.info("🕒 **Lunes a Viernes:** 8:00 AM - 9:00 PM | **Sábados:** 8:00 AM - 4:00 PM")
        
        st.markdown("""
        ### Servicios Disponibles en el Campus:
        * **Préstamo en Sala y Circulación:** Solicitud de material bibliográfico físico con carnet estudiantil activo.
        * **Cubículos de Estudio Grupal:** Espacios equipados para trabajo colaborativo y defensa de proyectos.
        * **Salas de Cómputo:** Estaciones de desarrollo equipadas con internet de alta velocidad y entornos de programación.
        """)

# =========================================================================
# Lógica de renderizado para app.py / st.navigation
# =========================================================================
if __name__ == "__main__":
    mostrar_centro_informacion()
else:
    usuario_activo = st.session_state.get("usuario_actual") or st.session_state.get("usuario")
    mostrar_centro_informacion(usuario_activo)