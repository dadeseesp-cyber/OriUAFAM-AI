import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def crear_pdf_riasec():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    docs_dir = os.path.join(base_dir, "documentos")
    os.makedirs(docs_dir, exist_ok=True)
    pdf_path = os.path.join(docs_dir, "Guia_Modelo_RIASEC_UAFAM.pdf")

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=40, leftMargin=40,
        topMargin=40, bottomMargin=40
    )

    styles = getSampleStyleSheet()
    
    primary_color = colors.HexColor("#1A365D")
    secondary_color = colors.HexColor("#2B6CB0")
    dark_neutral = colors.HexColor("#2D3748")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=primary_color,
        alignment=1,
        spaceAfter=10
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=secondary_color,
        alignment=1,
        spaceAfter=15
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=primary_color,
        spaceBefore=10,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=dark_neutral,
        spaceAfter=8
    )

    story = []

    story.append(Paragraph("UNIVERSIDAD AGROFORESTAL FERNANDO ARTURO DE MERIÑO (UAFAM)", subtitle_style))
    story.append(Paragraph("Guía Oficial del Modelo Vocacional RIASEC", title_style))
    story.append(Paragraph("Sistema de Orientación Vocacional e Inteligencia Artificial (OriUAFAM AI)", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=primary_color, spaceAfter=15))

    story.append(Paragraph("1. Introducción al Modelo Holland (RIASEC)", h2_style))
    p1 = ("El Modelo RIASEC, desarrollado por el psicólogo John Holland, postula que las preferencias "
          "vocacionales y la elección de una carrera profesional son una expresión de la personalidad de cada individuo. "
          "En <b>OriUAFAM AI</b>, este modelo fundamenta la evaluación vocacional de los estudiantes para relacionar "
          "sus intereses con las carreras ofrecidas por la universidad.")
    story.append(Paragraph(p1, body_style))

    story.append(Paragraph("2. Las 6 Dimensiones Vocacionales", h2_style))
    
    tabla_datos = [
        [Paragraph("<b>Dimensión</b>", body_style), Paragraph("<b>Características Principales</b>", body_style), Paragraph("<b>Carreras UAFAM Relacionadas</b>", body_style)],
        [Paragraph("<b>Realista (R)</b>", body_style), Paragraph("Preferencia por trabajo práctico, uso de herramientas, plantas o maquinaria.", body_style), Paragraph("Ingeniería Agronómica", body_style)],
        [Paragraph("<b>Investigador (I)</b>", body_style), Paragraph("Pensamiento analítico, resolución de problemas y curiosidad científica.", body_style), Paragraph("Lic. en Informática, Ingeniería Agronómica", body_style)],
        [Paragraph("<b>Artístico (A)</b>", body_style), Paragraph("Expresión creativa, diseño, innovación e imaginación.", body_style), Paragraph("Lic. en Turismo", body_style)],
        [Paragraph("<b>Social (S)</b>", body_style), Paragraph("Vocación de servicio, enseñanza, orientación y colaboración.", body_style), Paragraph("Lic. en Turismo, Educación", body_style)],
        [Paragraph("<b>Emprendedor (E)</b>", body_style), Paragraph("Liderazgo, iniciativa de negocios, persuasión y gestión.", body_style), Paragraph("Lic. en Administración de Empresas", body_style)],
        [Paragraph("<b>Convencional (C)</b>", body_style), Paragraph("Organización, análisis de datos, contabilidad y estructura.", body_style), Paragraph("Lic. en Contabilidad", body_style)]
    ]

    tabla = Table(tabla_datos, colWidths=[1.3*inch, 3.8*inch, 2.2*inch])
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#EDF2F7")),
        ('TEXTCOLOR', (0, 0), (-1, 0), primary_color),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    
    story.append(tabla)
    story.append(Spacer(1, 15))

    story.append(Paragraph("3. Metodología en OriUAFAM AI", h2_style))
    p2 = ("El cuestionario evaluativo consta de 20 preguntas ponderadas según la escala RIASEC. "
          "Al finalizar, la plataforma calcula el perfil dominante del estudiante y genera sugerencias personalizadas, "
          "facilitando la toma de decisiones informadas sobre su futuro académico.")
    story.append(Paragraph(p2, body_style))

    story.append(Spacer(1, 20))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#CBD5E0"), spaceAfter=10))
    story.append(Paragraph("Documento Institucional Oficial — OriUAFAM AI | Universidad Agroforestal Fernando Arturo de Meriño", ParagraphStyle('Footer', parent=body_style, fontSize=8, alignment=1, textColor=colors.gray)))

    doc.build(story)
    print("✅ Archivo 'Guia_Modelo_RIASEC_UAFAM.pdf' generado con éxito en 'documentos/'.")

if __name__ == "__main__":
    crear_pdf_riasec()