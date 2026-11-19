import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def crear_pdf_solicitud_servicios():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    docs_dir = os.path.join(base_dir, "documentos")
    os.makedirs(docs_dir, exist_ok=True)
    pdf_path = os.path.join(docs_dir, "Solicitud_Servicios_UAFAM.pdf")

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
        'DocTitle', parent=styles['Heading1'],
        fontName='Helvetica-Bold', fontSize=18, leading=22,
        textColor=primary_color, alignment=1, spaceAfter=10
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=11, leading=15,
        textColor=secondary_color, alignment=1, spaceAfter=15
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom', parent=styles['Heading2'],
        fontName='Helvetica-Bold', fontSize=12, leading=16,
        textColor=primary_color, spaceBefore=8, spaceAfter=6
    )

    body_style = ParagraphStyle(
        'Body_Custom', parent=styles['Normal'],
        fontName='Helvetica', fontSize=9, leading=13,
        textColor=dark_neutral, spaceAfter=6
    )

    story = []

    # Encabezado
    story.append(Paragraph("UNIVERSIDAD AGROFORESTAL FERNANDO ARTURO DE MERIÑO (UAFAM)", subtitle_style))
    story.append(Paragraph("FORMULARIO DE SOLICITUD DE SERVICIOS ESTUDIANTILES", title_style))
    story.append(Paragraph("Departamento de Registro y Control Académico", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=primary_color, spaceAfter=12))

    # Sección 1: Datos del Estudiante
    story.append(Paragraph("1. DATOS DEL SOLICITANTE", h2_style))
    datos_estudiante = [
        [Paragraph("<b>Nombre Completo:</b>", body_style), Paragraph("________________________________________________", body_style)],
        [Paragraph("<b>Matrícula:</b>", body_style), Paragraph("________________________", body_style)],
        [Paragraph("<b>Carrera:</b>", body_style), Paragraph("________________________________________________", body_style)],
        [Paragraph("<b>Correo Electrónico:</b>", body_style), Paragraph("________________________", body_style)],
        [Paragraph("<b>Teléfono / Móvil:</b>", body_style), Paragraph("________________________", body_style)]
    ]
    t_datos = Table(datos_estudiante, colWidths=[1.8*inch, 5.2*inch])
    t_datos.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_datos)
    story.append(Spacer(1, 10))

    # Sección 2: Servicios Solicitados
    story.append(Paragraph("2. SERVICIO SOLICITADO (Marque con una X)", h2_style))
    servicios = [
        [Paragraph("[  ] Record de Notas Oficial", body_style), Paragraph("[  ] Carta de Grado", body_style)],
        [Paragraph("[  ] Certificación de Estudios", body_style), Paragraph("[  ] Homologación de Asignaturas", body_style)],
        [Paragraph("[  ] Carta de Conducta", body_style), Paragraph("[  ] Retiro de Asignaturas", body_style)],
        [Paragraph("[  ] Certificación para Visa/Trabajo", body_style), Paragraph("[  ] Reingreso Académico", body_style)]
    ]
    t_servicios = Table(servicios, colWidths=[3.5*inch, 3.5*inch])
    t_servicios.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F7FAFC")),
    ]))
    story.append(t_servicios)
    story.append(Spacer(1, 10))

    # Sección 3: Firmas
    story.append(Paragraph("3. CONFORMIDAD Y FIRMAS", h2_style))
    story.append(Spacer(1, 20))
    firmas = [
        [Paragraph("__________________________________<br/>Firma del Estudiante", body_style),
         Paragraph("__________________________________<br/>Recibido por Registro UAFAM", body_style)]
    ]
    t_firmas = Table(firmas, colWidths=[3.5*inch, 3.5*inch])
    t_firmas.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE')
    ]))
    story.append(t_firmas)

    # Pie
    story.append(Spacer(1, 25))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#CBD5E0"), spaceAfter=10))
    story.append(Paragraph("Formulario Oficial de Servicios Estudiantiles — UAFAM | OriUAFAM AI", ParagraphStyle('Footer', parent=body_style, fontSize=8, alignment=1, textColor=colors.gray)))

    doc.build(story)
    print("✅ Archivo 'Solicitud_Servicios_UAFAM.pdf' generado exitosamente en 'documentos/'.")

if __name__ == "__main__":
    crear_pdf_solicitud_servicios()