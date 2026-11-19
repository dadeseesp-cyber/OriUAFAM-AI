import io
from pathlib import Path
import streamlit as st
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer


def _resolver_ruta_documento(nombre_archivo: str) -> Path:
    """Busca el PDF institucional en las rutas probables del proyecto."""
    ruta_archivo = Path(__file__).resolve()
    candidatos = [
        ruta_archivo.parent.parent / "documentos" / nombre_archivo,
        ruta_archivo.parent / "documentos" / nombre_archivo,
        ruta_archivo.parent.parent.parent / "documentos" / nombre_archivo,
        Path("documentos") / nombre_archivo,
        Path("oriuafam_ai") / "documentos" / nombre_archivo,
    ]
    for ruta in candidatos:
        if ruta.exists() and ruta.is_file():
            return ruta
    return candidatos[0]


def generar_pdf_respaldo(titulo_doc: str, subtitulo_doc: str, cuerpo_texto: str) -> bytes:
    """Genera un PDF válido en memoria si el archivo físico no se encuentra."""
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
        "TituloUAFAM",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=14,
        textColor=colors.HexColor("#1B365D"),
        alignment=1,
    )
    estilo_sub = ParagraphStyle(
        "SubtituloUAFAM",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=11,
        textColor=colors.HexColor("#2E5B88"),
        alignment=1,
        spaceAfter=12,
    )
    estilo_cuerpo = ParagraphStyle(
        "CuerpoUAFAM",
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
    """Lee el PDF desde documentos/ o genera un PDF de respaldo en memoria."""
    ruta_pdf = _resolver_ruta_documento(nombre_archivo)
    if ruta_pdf.exists() and ruta_pdf.is_file():
        return ruta_pdf.read_bytes()
    return generar_pdf_respaldo(titulo_respaldo, subtitulo_respaldo, texto_respaldo)


def mostrar_recursos(usuario=None) -> None:
    st.title("🏛️ Centro de Información - UAFAM")
    st.write(
        "Explora las guías, documentos oficiales, recursos bibliográficos y servicios "
        "institucionales para apoyar tu desarrollo académico y vocacional."
    )
    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(
        [
            "📚 Biblioteca y Recursos",
            "📜 Documentos y Reglamentos",
            "🕒 Horarios y Servicios",
        ]
    )

    with tab1:
        st.subheader("Catálogo y Recursos Bibliográficos")
        st.write(
            "Consulta referencias académicas, guías metodológicas y recursos de apoyo "
            "para tus asignaturas y proyecto de grado."
        )

        busqueda = st.text_input(
            "🔍 Buscar guías, temas o recursos:",
            placeholder="Ej. RIASEC, calendario 2027, reglamento, Python...",
            key="buscar_recurso_uafam",
        )

        if busqueda:
            st.info(f"Mostrando sugerencias relacionadas con: **{busqueda}**")
            st.markdown(
                """
- **Guía del Modelo Vocacional RIASEC (UAFAM)** — Orientación vocacional y afinidad por carreras.
- **Calendario Académico Oficial 2027** — Fechas de inscripción, docencia y evaluaciones.
- **Reglamento Académico Estudiantil** — Normativa de permanencia, evaluación y deberes estudiantiles.
- **Solicitud de Servicios Estudiantiles** — Trámites de orientación, tutorías y registro.
                """
            )
        else:
            st.markdown(
                """
### 📌 Recursos Destacados para Estudiantes
- 📖 **Normas APA 7ma Edición:** Lineamientos de citación y redacción académica para trabajos y tesis.
- 🧭 **Modelo Vocacional RIASEC:** Marco de referencia para explorar perfiles e intereses profesionales.
- 📅 **Planificación Académica 2027:** Consulta de períodos y fechas clave del año académico.
                """
            )

    with tab2:
        st.subheader("Documentos y Reglamentos Oficiales")
        st.write(
            "Descarga los documentos institucionales disponibles en el repositorio de la plataforma."
        )

        pdf_reglamento = leer_documento_o_generar(
            "reglamento.pdf",
            "Reglamento Académico Estudiantil",
            "Normativas de Evaluación, Matrícula y Permanencia - UAFAM",
            "Documento oficial que establece los deberes, derechos, criterios de evaluación y disposiciones académicas de la Universidad Agroforestal Fernando Arturo de Meriño.",
        )
        pdf_riasec = leer_documento_o_generar(
            "Guia_Modelo_RIASEC_UAFAM.pdf",
            "Guía Oficial del Modelo Vocacional RIASEC",
            "Marco Metodológico de Orientación Vocacional - OriUAFAM AI",
            "Guía institucional sobre las dimensiones vocacionales RIASEC aplicadas a la orientación académica y profesional en UAFAM.",
        )
        pdf_calendario = leer_documento_o_generar(
            "calendario_2027.pdf",
            "Calendario Académico Oficial 2027",
            "Fechas de Inscripción, Docencia y Evaluaciones - UAFAM",
            "Cronograma de períodos académicos, inscripciones, retiros y evaluaciones correspondientes al año 2027.",
        )
        pdf_servicios = leer_documento_o_generar(
            "Solicitud_Servicios_UAFAM.pdf",
            "Formulario de Solicitud de Servicios Estudiantiles",
            "Departamento de Orientación y Registro Académico",
            "Formato institucional para solicitar servicios estudiantiles, asesoría académica y orientación vocacional.",
        )

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("##### 📌 Normativas y Guías")
            st.download_button(
                label="📥 Descargar Reglamento Estudiantil (PDF)",
                data=pdf_reglamento,
                file_name="reglamento.pdf",
                mime="application/pdf",
                use_container_width=True,
                key="dl_reglamento_uafam",
            )
            st.download_button(
                label="📥 Descargar Guía Modelo RIASEC (PDF)",
                data=pdf_riasec,
                file_name="Guia_Modelo_RIASEC_UAFAM.pdf",
                mime="application/pdf",
                use_container_width=True,
                key="dl_riasec_uafam",
            )

        with col2:
            st.markdown("##### 📌 Calendario y Trámites")
            st.download_button(
                label="📥 Descargar Calendario Académico 2027 (PDF)",
                data=pdf_calendario,
                file_name="calendario_2027.pdf",
                mime="application/pdf",
                use_container_width=True,
                key="dl_calendario_2027_uafam",
            )
            st.download_button(
                label="📥 Descargar Solicitud de Servicios (PDF)",
                data=pdf_servicios,
                file_name="Solicitud_Servicios_UAFAM.pdf",
                mime="application/pdf",
                use_container_width=True,
                key="dl_servicios_uafam",
            )

    with tab3:
        st.subheader("Horarios de Atención y Servicios")
        st.info("🕒 **Lunes a Viernes:** 8:00 AM - 9:00 PM | **Sábados:** 8:00 AM - 4:00 PM")
        st.markdown(
            """
### Servicios Disponibles en el Campus
- **Orientación Académica y Vocacional:** Acompañamiento para planificación de asignaturas y toma de decisiones.
- **Consulta Bibliográfica y Apoyo a la Investigación:** Acceso a materiales de estudio y guías de trabajo académico.
- **Gestión y Registro Estudiantil:** Orientación sobre trámites y calendarios institucionales.
            """
        )


_usuario_sesion = (
    st.session_state.get("usuario_actual")
    or st.session_state.get("usuario")
)
mostrar_recursos(_usuario_sesion)
