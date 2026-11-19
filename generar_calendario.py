import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

os.makedirs("documentos", exist_ok=True)

pdf_path = "documentos/calendario_2027.pdf"
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=letter,
    rightMargin=36,
    leftMargin=36,
    topMargin=36,
    bottomMargin=36
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'TitleStyle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=18,
    textColor=colors.HexColor('#1B365D'),
    alignment=1,
    spaceAfter=6
)

subtitle_style = ParagraphStyle(
    'SubTitleStyle',
    parent=title_style,
    fontSize=13,
    textColor=colors.HexColor('#4B6B94'),
    alignment=1,
    spaceAfter=12
)

h2_style = ParagraphStyle(
    'H2Style',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=11,
    textColor=colors.HexColor('#1B365D'),
    spaceBefore=10,
    spaceAfter=4
)

cell_header_style = ParagraphStyle(
    'CellHeader',
    fontName='Helvetica-Bold',
    fontSize=9,
    textColor=colors.white,
    alignment=1
)

cell_body_style = ParagraphStyle(
    'CellBody',
    fontName='Helvetica',
    fontSize=8.5,
    leading=11,
    textColor=colors.HexColor('#222222')
)

cell_body_bold = ParagraphStyle(
    'CellBodyBold',
    fontName='Helvetica-Bold',
    fontSize=8.5,
    leading=11,
    textColor=colors.HexColor('#1B365D')
)

story = [
    Paragraph("UNIVERSIDAD AGROFORESTAL FERNANDO ARTURO DE MERIÑO", title_style),
    Paragraph("CALENDARIO ACADÉMICO - PERÍODO LECTIVO 2027", subtitle_style),
    HRFlowable(width="100%", thickness=2, color=colors.HexColor('#1B365D'), spaceAfter=12),
]

cuatrimestres = [
    {
        "titulo": "PRIMER CUATRIMESTRE (Enero - Abril 2027)",
        "eventos": [
            ("07 - 12 de Enero", "Proceso de Reinscripción y Selección de Asignaturas"),
            ("14 de Enero", "Inicio de Clases - Primer Cuatrimestre 2027"),
            ("26 de Enero", "Feriado: Día de Duarte (No Lectivo)"),
            ("22 - 27 de Febrero", "Período de Evaluaciones Primer Parcial"),
            ("27 de Febrero", "Feriado: Día de la Independencia Nacional"),
            ("05 - 10 de Abril", "Período de Evaluaciones Finales y Cierre de Calificaciones"),
            ("12 - 17 de Abril", "Receso Académico Cuatrimestral / Semana Santa")
        ]
    },
    {
        "titulo": "SEGUNDO CUATRIMESTRE (Mayo - Agosto 2027)",
        "eventos": [
            ("19 - 24 de Abril", "Proceso de Selección de Asignaturas - Segundo Cuatrimestre"),
            ("04 de Mayo", "Inicio de Clases - Segundo Cuatrimestre 2027"),
            ("14 - 19 de Junio", "Período de Evaluaciones Primer Parcial"),
            ("16 de Agosto", "Feriado: Día de la Restauración"),
            ("16 - 21 de Agosto", "Período de Evaluaciones Finales"),
            ("23 - 28 de Agosto", "Receso Académico e Inscripción Cuatrimestral")
        ]
    },
    {
        "titulo": "TERCER CUATRIMESTRE (Septiembre - Diciembre 2027)",
        "eventos": [
            ("31 Ago - 04 Sep", "Proceso de Selección de Asignaturas - Tercer Cuatrimestre"),
            ("07 de Septiembre", "Inicio de Clases - Tercer Cuatrimestre 2027"),
            ("11 - 16 de Octubre", "Período de Evaluaciones Primer Parcial"),
            ("06 de Noviembre", "Feriado: Día de la Constitución"),
            ("13 - 18 de Diciembre", "Período de Evaluaciones Finales"),
            ("20 de Diciembre", "Cierre del Año Académico 2027 e Inicio de Receso Navideño")
        ]
    }
]

for q in cuatrimestres:
    story.append(Paragraph(q["titulo"], h2_style))
    table_data = [[Paragraph("Fecha / Período", cell_header_style), Paragraph("Actividad Académica / Evento", cell_header_style)]]
    for fecha, evento in q["eventos"]:
        table_data.append([
            Paragraph(fecha, cell_body_bold),
            Paragraph(evento, cell_body_style)
        ])
    t = Table(table_data, colWidths=[140, 390])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1B365D')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CCCCCC')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8F9FA')])
    ]))
    story.append(t)
    story.append(Spacer(1, 8))

doc.build(story)
print(f"✅ PDF generado exitosamente en: {pdf_path}")
