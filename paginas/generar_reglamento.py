import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Crear carpeta si no existe
os.makedirs("documentos", exist_ok=True)

# Configurar documento PDF
doc = SimpleDocTemplate(
    "documentos/reglamento.pdf",
    pagesize=letter,
    rightMargin=40,
    leftMargin=40,
    topMargin=40,
    bottomMargin=40
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'TitleStyle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=18,
    textColor=colors.HexColor('#1B365D'),
    alignment=1,
    spaceAfter=10
)

subtitle_style = ParagraphStyle(
    'SubTitleStyle',
    parent=title_style,
    fontSize=14,
    textColor=colors.HexColor('#4B6B94'),
    alignment=1
)

h2_style = ParagraphStyle(
    'H2Style',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=12,
    textColor=colors.HexColor('#1B365D'),
    spaceBefore=14,
    spaceAfter=6
)

body_style = ParagraphStyle(
    'BodyStyle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=10,
    leading=14,
    spaceAfter=8
)

story = [
    Paragraph("UNIVERSIDAD AGROFORESTAL FERNANDO ARTURO DE MERIÑO", title_style),
    Paragraph("REGLAMENTO ESTUDIANTIL INSTITUCIONAL", subtitle_style),
    HRFlowable(width="100%", thickness=2, color=colors.HexColor('#1B365D'), spaceAfter=15),
    
    Paragraph("CAPÍTULO I: DISPOSICIONES GENERALES Y ADMISIÓN", h2_style),
    Paragraph("<b>Artículo 1:</b> El presente reglamento rige los derechos, deberes y procesos académicos de todos los estudiantes matriculados en la Universidad Agroforestal Fernando Arturo de Meriño (UAFAM).", body_style),
    Paragraph("<b>Artículo 2:</b> Todo estudiante tiene derecho a recibir formación académica de excelencia, hacer uso de las instalaciones y recursos digitales de la institución, y ser evaluado de manera justa e imparcial.", body_style),
    
    Paragraph("CAPÍTULO II: DEBERES Y NORMAS DISCIPLINARIAS", h2_style),
    Paragraph("<b>Artículo 3:</b> Son deberes fundamentales del estudiante: mantener un índice académico acumulado superior al mínimo establecido, asistir puntualmente a sus asignaturas y mantener un comportamiento ético e íntegro.", body_style),
    Paragraph("<b>Artículo 4:</b> Toda falta a la integridad académica, incluyendo el plagio o fraude en evaluaciones, será sancionada conforme a las normativas del Comité Disciplinario.", body_style),
    
    Paragraph("CAPÍTULO III: EVALUACIÓN Y CALIFICACIONES", h2_style),
    Paragraph("<b>Artículo 5:</b> El sistema de evaluación comprende pruebas parciales, trabajos prácticos, participación y examen final. La calificación mínima de aprobación por asignatura es de 70 puntos (C).", body_style),
    Paragraph("<b>Artículo 6:</b> El estudiante tiene derecho a solicitar revisión de pruebas o exámenes en un plazo no mayor a cinco (5) días hábiles tras la publicación de notas.", body_style),
    
    Paragraph("CAPÍTULO IV: PERMANENCIA Y GRADUACIÓN", h2_style),
    Paragraph("<b>Artículo 7:</b> Para optar por la titulación en cualquier grado académico, el estudiante deberá haber completado la totalidad de los créditos del pensum vigente y cumplir con el trabajo de grado correspondiente.", body_style)
]

doc.build(story)
print("✅ PDF del Reglamento generado exitosamente en documentos/reglamento.pdf")