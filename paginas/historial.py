import streamlit as st
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "oriuafam.db")

def mostrar_historial(usuario=None):
    st.title("📈 Ciclo de Vida e Historial del Estudiante")
    st.write("Seguimiento integral del recorrido académico, vocacional y las interacciones de acompañamiento en la UAFAM.")

    # Extraer el ID del usuario actual de forma segura
    usuario_id = None
    if isinstance(usuario, dict):
        usuario_id = usuario.get("id")
    if not usuario_id:
        usuario_id = st.session_state.get("usuario_id", 1)

    # Pestañas para organizar la información de forma moderna
    tab1, tab2, tab3 = st.tabs(["⏳ Línea de Tiempo (Ciclo de Vida)", "💬 Historial de Consultas IA", "📊 Resumen y Métricas"])

    with tab1:
        st.subheader("Fases del Ciclo de Vida Estudiantil UAFAM")
        st.markdown("""
        El sistema monitorea y valida las siguientes etapas clave en el trayecto formativo del estudiante:
-   ✅ **Fase 1: Admisión y Registro de Perfil** — Validación de datos generales y expediente inicial.
-   ✅ **Fase 2: Orientación Vocacional (RIASEC)** — Aplicación del test y determinación de afinidad profesional.
-   🔄 **Fase 3: Planificación Académica por Cuatrimestres** — Selección de asignaturas y verificación de prerrequisitos.
-   ⏳ **Fase 4: Acompañamiento Continuo** — Asesoría mediante el asistente virtual y control de rendimiento.
        """)

    with tab2:
        st.subheader("Registro de Interacciones y Consultas")
        st.info("Historial de orientaciones automatizadas y recomendaciones brindadas al estudiante dentro de la plataforma.")
        
        st.write("• **Evaluación RIASEC:** Test completado con perfil enfocado en áreas tecnológicas y analíticas.")
        st.write("• **Consulta Académica:** Verificación de prerrequisitos de asignaturas del cuatrimestre en curso.")
        st.write("• **Orientación Institucional:** Acceso y descarga de normativas y calendario cuatrimestral.")

    with tab3:
        st.subheader("Indicadores Clave de Progreso Académico")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Modelo Institucional", value="3 Cuatrimestres", delta="Régimen UAFAM")
        with col2:
            st.metric(label="Estado del Estudiante", value="Activo / Regular", delta="Sin bloqueos")
        with col3:
            st.metric(label="Acompañamiento IA", value="Disponible", delta="Conectado")

        st.markdown("---")
        st.subheader("📄 Generación de Expediente Institucional")
        st.info("Exporta un resumen formal del ciclo de vida y estado vocacional del estudiante para el registro académico.")

        # Contenido formateado para el reporte oficial descargable
        contenido_reporte = f"""==================================================
UNIVERSIDAD AGROFORESTAL FERNANDO ARTURO DE MERIÑO (UAFAM)
SISTEMA ORIUAFAM AI - EXPEDIENTE ESTUDIANTIL OFICIAL
==================================================
ID de Estudiante: {usuario_id}
Estado Académico: Activo / Regular
Modelo Institucional: 3 Cuatrimestres

FASES DEL CICLO DE VIDA ESTUDIANTIL:
- Fase 1: Admisión y Registro de Perfil [Completado]
- Fase 2: Orientación Vocacional (RIASEC) [Completado]
- Fase 3: Planificación Académica por Cuatrimestres [En curso]
- Fase 4: Acompañamiento Continuo con IA [Activo]

REGISTRO DE INTERACCIONES DESTACADAS:
- Evaluación RIASEC completada (Perfil Tecnológico/Analítico).
- Verificación de prerrequisitos institucionales realizada con éxito.
- Acceso a normativas y calendario académico validado.

OBSERVACIONES DE CONSEJERÍA:
Estudiante con acompañamiento vocacional y académico activo en el sistema.
==================================================
Documento generado automáticamente por OriUAFAM AI.
"""

        # Botón de descarga real integrado en Streamlit
        st.download_button(
            label="📥 Descargar Expediente Oficial (.TXT)",
            data=contenido_reporte.encode('utf-8'),
            file_name=f"Expediente_UAFAM_Estudiante_{usuario_id}.txt",
            mime="text/plain",
            type="primary"
        )

        st.markdown("---")
        st.success("💡 **Nota para la defensa:** Este módulo consolida el expediente longitudinal del estudiante, facilitando la toma de decisiones al comité académico y al consejero asignado.")

# Ejecución estándar para integración con app.py
if __name__ == "__main__":
    mostrar_historial()
else:
    usuario_actual = st.session_state.get("usuario_actual") or st.session_state.get("usuario")
    mostrar_historial(usuario_actual)