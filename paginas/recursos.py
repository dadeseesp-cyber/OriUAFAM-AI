import os
import streamlit as st

def mostrar_recursos(usuario=None):
    st.title("📚 Recursos y Materiales Académicos UAFAM")
    st.write("Explora las guías, documentos oficiales y herramientas para apoyar tu desarrollo académico y vocacional.")

    st.markdown("---")

    # Ruta base apuntando a la raíz del proyecto para ubicar 'documentos/'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DOCS_DIR = os.path.join(BASE_DIR, "documentos")

    # ==========================================
    # SECCIÓN 1: DOCUMENTOS Y REGLAMENTOS OFICIALES
    # ==========================================
    st.subheader("📄 Documentos Oficiales UAFAM")
    
    col1, col2 = st.columns(2)

    with col1:
        with st.expander("📖 Reglamento Estudiantil UAFAM", expanded=False):
            st.markdown("""
            ### 📌 Aspectos Clave del Reglamento Estudiantil
            
            * **Derechos Estudiantiles:** Recibir educación de calidad, libertad de expresión académica y acceso a servicios estudiantiles.
            * **Deberes:** Mantener un índice académico mínimo, cumplir con la asistencia y respetar las normas disciplinarias.
            * **Evaluación y Calificaciones:** 
                * Exámenes parciales, trabajos prácticos y evaluación final.
                * Puntuaciones mínimas de aprobación y proceso de revisión de pruebas.
            * **Bajas y Retiros:** Fechas límites y procedimientos para retiro oficial de asignaturas sin penalización académica.
            """)
            st.caption("Formato: PDF | Versión Oficial Vigente 2026")
            
            reglamento_path = os.path.join(DOCS_DIR, "reglamento.pdf")
            if os.path.exists(reglamento_path):
                with open(reglamento_path, "rb") as f:
                    st.download_button(
                        label="📥 Descargar Reglamento Completo (PDF)",
                        data=f,
                        file_name="Reglamento_Estudiantil_UAFAM.pdf",
                        mime="application/pdf",
                        key="btn_reglamento"
                    )
            else:
                st.error("⚠️ El archivo 'reglamento.pdf' no se encuentra en la carpeta 'documentos/'.")

        with st.expander("🗓️ Calendario Académico 2027", expanded=False):
            st.markdown("""
            ### 📅 Fechas Clave del Período Lectivo
            * **Inscripciones y Reinscripciones:** Inicio de cuatrimestres.
            * **Período de Evaluaciones:** Parciales y finales.
            * **Recesos Académicos y Feriados:** Fechas no lectivas institucionales.
            """)
            st.caption("Formato: PDF | Período 2027")
            
            calendario_path = os.path.join(DOCS_DIR, "calendario_2027.pdf")
            if os.path.exists(calendario_path):
                with open(calendario_path, "rb") as f:
                    st.download_button(
                        label="📥 Descargar Calendario",
                        data=f,
                        file_name="Calendario_Academico_UAFAM_2027.pdf",
                        mime="application/pdf",
                        key="btn_calendario"
                    )
            else:
                st.error("⚠️ El archivo 'calendario_2027.pdf' no se encuentra en la carpeta 'documentos/'.")

    with col2:
        with st.expander("🎓 Guía de Orientación Vocacional RIASEC", expanded=False):
            st.markdown("""
            ### 💡 Modelo Vocacional John Holland
            * **6 Dimensiones:** Realista, Investigador, Artístico, Social, Emprendedor y Convencional.
            * Explicación de cómo la prueba asigna recomendaciones de carreras en la UAFAM.
            """)
            st.caption("Formato: PDF | OriUAFAM AI")
            
            riasec_path = os.path.join(DOCS_DIR, "Guia_Modelo_RIASEC_UAFAM.pdf")
            if os.path.exists(riasec_path):
                with open(riasec_path, "rb") as f:
                    st.download_button(
                        label="📥 Descargar Guía RIASEC",
                        data=f,
                        file_name="Guia_Modelo_RIASEC_UAFAM.pdf",
                        mime="application/pdf",
                        key="btn_guia_riasec"
                    )
            else:
                st.error("⚠️ El archivo 'Guia_Modelo_RIASEC_UAFAM.pdf' no se encuentra en la carpeta 'documentos/'.")

        with st.expander("📋 Solicitud de Servicios Estudiantiles", expanded=False):
            st.markdown("""
            ### 📝 Tramitaciones Disponibles
            * Certificaciones de estudio y récords de notas.
            * Cartas de grado y homologaciones de asignaturas.
            * Formularios oficiales para Departamento de Registro.
            """)
            st.caption("Formato: PDF | Registro y Control")
            
            solicitud_path = os.path.join(DOCS_DIR, "Solicitud_Servicios_UAFAM.pdf")
            if os.path.exists(solicitud_path):
                with open(solicitud_path, "rb") as f:
                    st.download_button(
                        label="📥 Descargar Formulario",
                        data=f,
                        file_name="Solicitud_Servicios_UAFAM.pdf",
                        mime="application/pdf",
                        key="btn_formulario"
                    )
            else:
                st.error("⚠️ El archivo 'Solicitud_Servicios_UAFAM.pdf' no se encuentra en la carpeta 'documentos/'.")

    st.markdown("---")

    # ==========================================
    # SECCIÓN 2: OFERTA ACADÉMICA Y PENSUMS
    # ==========================================
    st.subheader("🎓 Pensums por Carrera")
    
    carreras_pensum = {
        "Licenciatura en Informática (INF)": "Especializada en desarrollo de software, bases de datos y redes.",
        "Licenciatura en Contabilidad (LCO)": "Enfocada en auditoría, contabilidad financiera y normativa tributaria.",
        "Licenciatura en Administración de Empresas (ADM)": "Orientada a la gestión gerencial, estrategia y emprendimiento.",
        "Ingeniería Agronómica (IAG)": "Especializada en producción agrícola, sostenibilidad y biotecnología.",
        "Licenciatura en Turismo (TUR)": "Desarrollo de proyectos turísticos, ecoturismo y gestión hotelera."
    }

    for idx, (carrera, desc) in enumerate(carreras_pensum.items()):
        with st.expander(f"📌 {carrera}"):
            st.write(desc)
            nombre_corto = carrera.split('(')[0].strip()
            codigo_carrera = carrera.split('(')[1].replace(')', '') if '(' in carrera else f"carrera_{idx}"

            pensum_path = os.path.join(DOCS_DIR, f"Pensum_{codigo_carrera}.pdf")
            if os.path.exists(pensum_path):
                with open(pensum_path, "rb") as f:
                    st.download_button(
                        label=f"📄 Descargar Pensum de {nombre_corto}",
                        data=f,
                        file_name=f"Pensum_{codigo_carrera}.pdf",
                        mime="application/pdf",
                        key=f"btn_pensum_idx_{idx}_{codigo_carrera}"
                    )
            else:
                st.warning(f"⚠️ El PDF del pensum ('Pensum_{codigo_carrera}.pdf') no está disponible aún en 'documentos/'.")

    st.markdown("---")

    # ==========================================
    # SECCIÓN 3: CONSEJOS DE ESTUDIO Y PRODUCTIVIDAD
    # ==========================================
    st.subheader("💡 Consejos de Rendimiento Académico")
    
    st.info("🎯 **Técnica Pomodoro:** Estudia durante 25 minutos sin distracciones y descansa 5 minutos. Repite el ciclo 4 veces y toma un descanso largo.")
    st.success("📝 **Toma de Apuntes Eficiente:** Utiliza el método Cornell dividiendo tus notas en ideas clave, apuntes detallados y un resumen final.")
    st.warning("🤝 **Grupos de Estudio:** Explicar los temas a un compañero es una de las formas más efectivas de consolidar el aprendizaje.")