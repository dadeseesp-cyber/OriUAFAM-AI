import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Diccionario explicativo por dimensión RIASEC
DESCRIPCIONES_RIASEC = {
    "R": ("Realista (R)", "Preferencia por actividades prácticas, uso de herramientas, tecnología aplicada y solución de problemas concretos."),
    "I": ("Investigador (I)", "Inclinación por el análisis de datos, el pensamiento lógico-matemático, la investigación científica y la programación."),
    "A": ("Artístico (A)", "Afinidad por la creatividad, la innovación visual, el diseño, la expresión de ideas y entornos no estructurados."),
    "S": ("Social (S)", "Vocación hacia el servicio, la enseñanza, la orientación a personas, la empatía y la colaboración comunitaria."),
    "E": ("Emprendedor (E)", "Liderazgo, habilidad para negociar, toma de decisiones estratégicas, gestión de proyectos y visión de negocios."),
    "C": ("Convencional (C)", "Gusto por la organización de procesos, análisis de datos financieros, gestión de registros, orden y metodologías estructuradas.")
}

# Opciones de carreras en UAFAM vinculadas
CARRERAS_UAFAM = {
    "I": [("Licenciatura en Informática (INF)", "Desarrollo de software, bases de datos y redes.")],
    "R": [("Ingeniería Agronómica (IAG)", "Producción agrícola, sostenibilidad y biotecnología.")],
    "E": [("Licenciatura en Administración de Empresas (LAE)", "Gestión comercial, liderazgo y finanzas corporativas.")],
    "C": [("Licenciatura en Contabilidad (LCO)", "Auditoría, contabilidad financiera y normativa tributaria.")],
    "A": [("Licenciatura en Turismo Sustentable (LTS)", "Ecoturismo, gestión ambiental y desarrollo cultural.")],
    "S": [("Licenciatura en Administración de Empresas (LAE)", "Enfoque en recursos humanos y gestión de equipos.")]
}

def generar_reporte_vocacional_pdf(nombre_estudiante, correo_estudiante, codigo_riasec, carrera_sugerida, puntajes):
    """Genera un informe vocacional completo y detallado en formato PDF usando ReportLab."""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    
    # Estilos visuales
    titulo_principal = ParagraphStyle(
        'TituloPDF',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=colors.HexColor('#1B365D'),
        alignment=1,
        spaceAfter=4
    )
    
    subtitulo = ParagraphStyle(
        'SubtituloPDF',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#2E5B88'),
        alignment=1,
        spaceAfter=12
    )

    seccion_titulo = ParagraphStyle(
        'SeccionTitulo',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#1B365D'),
        spaceBefore=10,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'CuerpoPDF',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#2D3748'),
        spaceAfter=6
    )

    bold_style = ParagraphStyle(
        'NegritaPDF',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    story = []

    # Header institucional
    story.append(Paragraph("UNIVERSIDAD AGROFORESTAL FERNANDO ARTURO DE MERIÑO", titulo_principal))
    story.append(Paragraph("Plataforma OriUAFAM AI — Informe Completo de Orientación Vocacional", subtitulo))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1B365D'), spaceAfter=12))

    # 1. Datos del Estudiante
    story.append(Paragraph("1. Información del Estudiante", seccion_titulo))
    datos_estudiante = [
        [Paragraph("<b>Estudiante:</b>", body_style), Paragraph(str(nombre_estudiante), body_style)],
        [Paragraph("<b>Correo Electrónico:</b>", body_style), Paragraph(str(correo_estudiante), body_style)],
        [Paragraph("<b>Perfil RIASEC Resultante:</b>", body_style), Paragraph(f"<b>{codigo_riasec}</b>", bold_style)],
        [Paragraph("<b>Carrera Sugerida Principal:</b>", body_style), Paragraph(f"<b>{carrera_sugerida}</b>", bold_style)]
    ]
    t_datos = Table(datos_estudiante, colWidths=[150, 382])
    t_datos.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#F8FAFC')),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
        ('PADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_datos)
    story.append(Spacer(1, 10))

    # 2. Desglose de Puntajes por Dimensión
    story.append(Paragraph("2. Resultados Obtenidos por Dimensión (Test RIASEC)", seccion_titulo))
    tabla_riasec_data = [
        [Paragraph("<b>Dimensión</b>", bold_style), Paragraph("<b>Puntaje</b>", bold_style), Paragraph("<b>Nivel de Afinidad</b>", bold_style)]
    ]

    for dim_key, (dim_nombre, desc) in DESCRIPCIONES_RIASEC.items():
        pts = puntajes.get(dim_key, 0)
        nivel = "Alto" if pts >= 15 else ("Medio" if pts >= 10 else "Bajo")
        tabla_riasec_data.append([
            Paragraph(dim_nombre, body_style),
            Paragraph(f"<b>{pts}</b> / 25", body_style),
            Paragraph(nivel, body_style)
        ])

    t_puntajes = Table(tabla_riasec_data, colWidths=[200, 150, 182])
    t_puntajes.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E5B88')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('BOX', (0, 0), (-1, -1), 1, colors.HexColor('#CBD5E1')),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
        ('PADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(t_puntajes)
    story.append(Spacer(1, 10))

    # 3. Interpretación y Por Qué del Resultado
    story.append(Paragraph("3. Análisis e Interpretación del Resultado", seccion_titulo))
    top_tres = list(codigo_riasec) if len(codigo_riasec) >= 3 else ["C", "R", "I"]
    
    explicacion_texto = f"Tu perfil dominante está compuesto por las dimensiones <b>{top_tres[0]}</b>, <b>{top_tres[1]}</b> y <b>{top_tres[2]}</b>. "
    explicacion_texto += "Esto indica que posees una combinación de habilidades orientadas al análisis estructurado, la organización sistemática y la resolución pragmática de problemas.<br/><br/>"
    
    for d in top_tres:
        if d in DESCRIPCIONES_RIASEC:
            nombre, desc = DESCRIPCIONES_RIASEC[d]
            explicacion_texto += f"• <b>{nombre}:</b> {desc}<br/>"

    story.append(Paragraph(explicacion_texto, body_style))
    story.append(Spacer(1, 10))

    # 4. Oferta Académica UAFAM Recomendada
    story.append(Paragraph("4. Opciones de Carreras Sugeridas en UAFAM", seccion_titulo))
    carreras_mencionadas = []
    for d in top_tres:
        if d in CARRERAS_UAFAM:
            for c_nombre, c_desc in CARRERAS_UAFAM[d]:
                if c_nombre not in carreras_mencionadas:
                    carreras_mencionadas.append(c_nombre)
                    story.append(Paragraph(f"• <b>{c_nombre}:</b> {c_desc}", body_style))

    story.append(Spacer(1, 10))

    # 5. Recomendaciones de Desarrollo Profesional
    story.append(Paragraph("5. Recomendaciones para tu Plan Académico", seccion_titulo))
    recom_texto = (
        "1. <b>Consulta el Pensum:</b> Revisa las asignaturas de tu carrera de interés en el módulo de Orientación Académica.<br/>"
        "2. <b>Cita de Orientación:</b> Puedes programar una cita presencial o virtual con el departamento de orientación académica para profundizar en tu perfil.<br/>"
        "3. <b>Desarrollo de Competencias:</b> Fortalece tus habilidades en el área de tecnología, herramientas analíticas y gestión de proyectos."
    )
    story.append(Paragraph(recom_texto, body_style))
    story.append(Spacer(1, 15))

    # Pie institucional
    story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#94A3B8'), spaceAfter=8))
    story.append(Paragraph("<i>Informe generado de manera automatizada por el motor OriUAFAM AI. Universidad Agroforestal Fernando Arturo de Meriño (UAFAM).</i>", ParagraphStyle('Pie', parent=body_style, fontSize=8, alignment=1, textColor=colors.HexColor('#64748B'))))

    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()