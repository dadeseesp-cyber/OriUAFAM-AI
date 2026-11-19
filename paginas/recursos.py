import os
import io
from pathlib import Path
import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors


def _resolver_ruta_documento(nombre_archivo: str) -> Path:
    """Busca el documento en ubicaciones probables dentro del proyecto."""
    base_actual = Path(__file__).resolve().parent  # .../oriuafam_ai/paginas
    candidatos = [
        base_actual.parent / "documentos" / nombre_archivo,          # .../oriuafam_ai/documentos/archivo.pdf
        base_actual.parent.parent / "documentos" / nombre_archivo,   # .../documentos/archivo.pdf
        Path("documentos") / nombre_archivo,                           # ./documentos/archivo.pdf
        Path("oriuafam_ai") / "documentos" / nombre_archivo,           # ./oriuafam_ai/documentos/archivo.pdf
    ]
    for ruta in candidatos:
        if ruta.exists():
            return ruta
    return candidatos[0]


def generar_pdf_respaldo(titulo_doc: str, subtitulo_doc: str, cuerpo_texto: str) -> bytes:
    """Genera un PDF válido en memoria si el archivo físico no está en la carpeta documentos."""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=45,
        leftMargin=45,
        topMargin=45,
        bottomMargin=45,
    )
    styles = getSampleStyleSheet()

    estilo_titulo = ParagraphStyle(
        "T",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=14,
        textColor=colors.HexColor("#1B365D"),
        alignment=1,
    )
    estilo_sub = ParagraphStyle(
        "S",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=11,
        textColor=colors.HexColor("#2E5B88"),
        alignment=1,
        spaceAfter=12,
    )
    estilo_cuerpo = ParagraphStyle(
        "C",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#2D3748"),
    )

    story = [
        Paragraph(
            "UNIVERSIDAD AGROFORESTAL FERNANDO ARTURO DE MERIÑO (UAFAM)",
            estilo_titulo,
        ),
        Paragraph(titulo_doc, estilo_sub),
        HRFlowable(
            width="100%",
            thickness=1,
            color=colors.HexColor("#1B365D"),
            spaceAfter=12,
        ),
        Paragraph(f"<b>{subtitulo_doc}</b>", estilo_cuerpo),
        Spacer(1, 8),
        Paragraph(cuerpo_texto, estilo_cuerpo),
    ]
    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()


def leer_documento_o_generar(
    nombre_archivo: str,
    titulo_respaldo: str,
    subtitulo_respaldo: str,
    texto_respaldo: str,
) -> bytes:
    """Lee el PDF real desde documentos/ o genera uno válido al instante."""
    ruta_doc = _resolver_ruta_documento(nombre_archivo)
    if ruta_doc.exists() and ruta_doc.is_file():
        return ruta_doc.read_bytes()
    return generar_pdf_respaldo(titulo_respaldo, subtitulo_respaldo, texto_respaldo)


def mostrar_centro_informacion(usuario=None) -> None:
    st.title("🏛️ Centro de Información - UAFAM")
    st.write(
        "Repositorio centralizado de recursos bibliográficos, normativas institucionales "
        "y servicios de apoyo a la investigación."
    )

    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(
        ["📚 Biblioteca Digital", "📜 Reglamentos y Normativas", "🕒 Horarios y Servicios"]
    )

    with tab1:
        st.subheader("Catálogo y Recursos Bibliográficos")
        st.write(
            "Accede a bases de datos científicas, libros electrónicos y revistas especializadas "
            "para tu tesis y asignaturas."
        )

        busqueda = st.text_input(
            "🔍 Buscar libros, tesis o artículos en el repositorio:",
            placeholder="Ej. Programación Python, Inteligencia Artificial, Metodología...",
        )
        if busqueda:
            st.info(f"Mostrando resultados de búsqueda para: **{busqueda}**")
            st.markdown(
                """
- **Introducción a la Inteligencia Artificial en la Educación** (Autor: D. UAFAM, 2025) - *Disponible en línea*
- **Metodología de Investigación Científica y Tecnológica** (Autor: C. Pérez, 2024) - *Acceso institucional*
- **Guía de Desarrollo en Python y Streamlit para Tesis** (Autor: UAFAM Tech, 2026) - *Descarga directa*
                """
            )
        else:
            st.markdown(
                """
### 📌 Destacados para Estudiantes
- 📖 **Normas APA 7ma Edición:** Guía oficial para la presentación de trabajos de grado y tesis.
- 💻 **Repositorio de Tesis Anteriores:** Consulta proyectos de software y tesis de grado de ingeniería.
- 🌐 **Bases de Datos Externas:** Acceso preferencial a JSTOR, IEEE y Dialnet con tus credenciales institucionales.
                """
            )

    with tab2:
        st.subheader("Normativa Académica e Institucional")
        st.write(
            "Documentos oficiales que rigen la vida estudiantil, orientación vocacional "
            "y trámites administrativos."
        )

        pdf_reglamento = leer_documento_o_generar(
            "reglamento.pdf",
            "Reglamento Académico Estudiantil",
            "Normativas de Evaluación, Matrícula y Permanencia - UAFAM",
            "Documento oficial que establece los deberes, derechos, régimen disciplinario y criterios de evaluación académica de los estudiantes de grado de la Universidad Agroforestal Fernando Arturo de Meriño.",
        )
        pdf_riasec = leer_documento_o_generar(
            "Guia_Modelo_RIASEC_UAFAM.pdf",
            "Guía Oficial del Modelo Vocacional RIASEC",
            "Marco Metodológico de Orientación Vocacional - OriUAFAM AI",
            "Guía institucional sobre las seis dimensiones de personalidad vocacional de John Holland (Realista, Investigador, Artístico, Social, Emprendedor y Convencional) aplicadas a la oferta académica de UAFAM.",
        )
        pdf_calendario = leer_documento_o_generar(
            "calendario_2027.pdf",
            "Calendario Académico Oficial 2027",
            "Fechas de Inscripción, Docencia y Evaluaciones - UAFAM",
            "Cronograma oficial de períodos académicos, procesos de selección de asignaturas, retiros y evaluaciones finales correspondientes al año académico 2027.",
        )
        pdf_servicios = leer_documento_o_generar(
            "Solicitud_Servicios_UAFAM.pdf",
            "Formulario de Solicitud de Servicios Estudiantiles",
            "Departamento de Orientación y Registro Académico",
            "Formato institucional para la solicitud de tutorías académicas, evaluación vocacional personalizada, certificación de estudios y acompañamiento psicopedagógico.",
        )

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("##### 📌 Normativas y Guías")
            st.download_button(
                label="📥 Descargar Reglamento Estudiantil (PDF)",
                data=pdf_reglamento,
                file_name="Reglamento_Estudiantil_UAFAM.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
            st.download_button(
                label="📥 Descargar Guía Modelo RIASEC (PDF)",
                data=pdf_riasec,
                file_name="Guia_Modelo_RIASEC_UAFAM.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
        with col2:
            st.markdown("##### 📌 Calendario y Trámites")
            st.download_button(
                label="📥 Descargar Calendario Académico 2027 (PDF)",
                data=pdf_calendario,
                file_name="Calendario_Academico_2027_UAFAM.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
            st.download_button(
                label="📥 Formulario Solicitud de Servicios (PDF)",
                data=pdf_servicios,
                file_name="Solicitud_Servicios_UAFAM.pdf",
                mime="application/pdf",
                use_container_width=True,
            )

    with tab3:
        st.subheader("Horarios de Atención y Servicios")
        st.info("🕒 **Lunes a Viernes:** 8:00 AM - 9:00 PM | **Sábados:** 8:00 AM - 4:00 PM")

        st.markdown(
            """
### Servicios Disponibles en el Campus:
- **Préstamo en Sala y Circulación:** Solicitud de material bibliográfico físico con carnet estudiantil activo.
- **Cubículos de Estudio Grupal:** Espacios equipados para trabajo colaborativo y defensa de proyectos.
- **Salas de Cómputo:** Estaciones de desarrollo equipadas con internet de alta velocidad y entornos de programación.
            """
        )


usuario_activo = (
    st.session_state.get("usuario_actual")
    or st.session_state.get("usuario")
)
mostrar_centro_informacion(usuario_activo)