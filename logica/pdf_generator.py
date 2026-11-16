import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generar_pdf_riasec(nombre_estudiante, resultados_riasec, recomendacion):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    story = []
    styles = getSampleStyleSheet()

    # Estilos personalizados
    titulo_style = ParagraphStyle(
        'TituloUAFAM',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#004d25'),  # Verde UAFAM
        alignment=1,
        spaceAfter=15
    )
    
    subtitulo_style = ParagraphStyle(
        'SubtituloUAFAM',
        parent=styles['Heading2'],
        fontSize=13,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=10
    )

    # Encabezado
    story.append(Paragraph("<b>UNIVERSIDAD AGROFORESTAL FERNANDO ARTURO DE MERIÑO (UAFAM)</b>", titulo_style))
    story.append(Paragraph("<b>Informe Oficial de Orientación Vocacional - OriUAFAM AI</b>", subtitulo_style))
    story.append(Spacer(1, 15))

    # Datos del Estudiante
    story.append(Paragraph(f"<b>Estudiante:</b> {nombre_estudiante}", styles['Normal']))
    story.append(Spacer(1, 10))

    # Tabla de Resultados RIASEC
    story.append(Paragraph("<b>Perfil Vocacional (RIASEC)</b>", subtitulo_style))
    data_tabla = [["Dimensión RIASEC", "Puntaje Obtenido"]]
    for dimension, puntaje in resultados_riasec.items():
        data_tabla.append([dimension, str(puntaje)])

    tabla = Table(data_tabla, colWidths=[250, 150])
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#004d25')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ]))
    story.append(tabla)
    story.append(Spacer(1, 15))

    # Recomendación
    story.append(Paragraph("<b>Recomendación Académica:</b>", subtitulo_style))
    story.append(Paragraph(recomendacion, styles['Normal']))

    doc.build(story)
    buffer.seek(0)
    return buffer