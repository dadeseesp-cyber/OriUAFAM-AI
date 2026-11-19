import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "oriuafam.db")

def obtener_conexion():
    """Establece conexión centralizada a la base de datos única oriuafam.db"""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

conexion_bd = obtener_conexion

def inicializar_base_de_datos():
    """Crea las tablas e inserta registros iniciales solo si la base de datos está vacía."""
    conn = obtener_conexion()
    cursor = conn.cursor()

    script_sql = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT UNIQUE NOT NULL,
        clave TEXT NOT NULL,
        carrera TEXT,
        rol TEXT DEFAULT 'estudiante',
        fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS carreras (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        codigo TEXT UNIQUE NOT NULL,
        duracion TEXT NOT NULL,
        modalidad TEXT DEFAULT 'Presencial / Semipresencial',
        descripcion TEXT
    );

    CREATE TABLE IF NOT EXISTS asignaturas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        carrera_id INTEGER,
        codigo TEXT NOT NULL,
        nombre TEXT NOT NULL,
        creditos INTEGER NOT NULL,
        cuatrimestre INTEGER NOT NULL,
        FOREIGN KEY(carrera_id) REFERENCES carreras(id)
    );

    CREATE TABLE IF NOT EXISTS preguntas_riasec (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pregunta TEXT NOT NULL,
        dimension TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS resultados_vocacionales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        codigo_riasec TEXT,
        carrera_sugerida TEXT,
        fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    );

    CREATE TABLE IF NOT EXISTS solicitudes_citas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        motivo TEXT NOT NULL,
        fecha_cita DATE NOT NULL,
        hora_cita TIME NOT NULL,
        estado TEXT DEFAULT 'Pendiente',
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    );

    CREATE TABLE IF NOT EXISTS recursos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        categoria TEXT NOT NULL,
        descripcion TEXT,
        enlace_url TEXT
    );
    """
    cursor.executescript(script_sql)

    # Verificar si ya existen registros en carreras antes de insertar
    cursor.execute("SELECT COUNT(*) FROM carreras")
    if cursor.fetchone()[0] == 0:
        carreras_uafam = [
            ("Licenciatura en Informática", "INF", "12 cuatrimestres (4 años)", "Desarrollo de software, bases de datos, redes y gestión de tecnologías de información."),
            ("Ingeniería Agronómica", "IAG", "12 cuatrimestres (4 años)", "Producción agrícola sostenible, gestión de suelo, riego y biotecnología agroforestal."),
            ("Licenciatura en Administración de Empresas", "LAE", "11 cuatrimestres", "Gestión empresarial, finanzas, planificación estratégica y liderazgo organizacional."),
            ("Licenciatura en Contabilidad", "LCO", "11 cuatrimestres", "Contabilidad financiera, auditoría, legislación tributaria y análisis de costos."),
            ("Licenciatura en Turismo Sustentable", "LTS", "11 cuatrimestres", "Ecoturismo, gestión hotelera, desarrollo turístico local e historia ambiental.")
        ]
        cursor.executemany(
            "INSERT INTO carreras (nombre, codigo, duracion, descripcion) VALUES (?, ?, ?, ?)",
            carreras_uafam
        )

        cursor.execute("SELECT id FROM carreras WHERE codigo = 'INF'")
        inf = cursor.fetchone()
        if inf:
            inf_id = inf["id"]
            asignaturas_inf = [
                (inf_id, "INF-101", "Introducción a la Programación", 4, 1),
                (inf_id, "MAT-101", "Matemática Superior", 4, 1),
                (inf_id, "INF-201", "Base de Datos I", 4, 2),
                (inf_id, "INF-202", "Estructura de Datos", 3, 2),
                (inf_id, "INF-301", "Ingeniería de Software", 4, 3),
                (inf_id, "INF-401", "Redes y Teleinformática", 4, 4),
            ]
            cursor.executemany(
                "INSERT INTO asignaturas (carrera_id, codigo, nombre, creditos, cuatrimestre) VALUES (?, ?, ?, ?, ?)",
                asignaturas_inf
            )

        preguntas_uafam = [
            ("Me gusta reparar objetos mecánicos, herramientas o dispositivos electrónicos.", "R"),
            ("Disfruto trabajar al aire libre, con plantas, cultivos o animales.", "R"),
            ("Prefiero actividades prácticas donde construya o ensamble piezas.", "R"),
            ("Me apasiona investigar causas de problemas complejos y analizar datos.", "I"),
            ("Disfruto resolver ejercicios matemáticos, acertijos o modelos lógicos.", "I"),
            ("Me llama la atención comprender cómo funcionan los lenguajes de programación.", "I"),
            ("Me gusta expresar mis ideas mediante el diseño, la escritura o el arte.", "A"),
            ("Prefiero buscar soluciones creativas e innovadoras ante un problema.", "A"),
            ("Disfruto crear contenidos visuales, gráficos o maquetas.", "A"),
            ("Siento satisfacción al enseñar, guiar o brindar orientación a otras personas.", "S"),
            ("Me gusta colaborar en proyectos comunitarios o de ayuda social.", "S"),
            ("Tengo facilidad para escuchar a las personas y ofrecerles consejo.", "S"),
            ("Me atrae liderar equipos de trabajo, negociar y tomar decisiones clave.", "E"),
            ("Disfruto emprender proyectos, presentar ideas y convencer a un público.", "E"),
            ("Me motiva asumir la responsabilidad de gestionar proyectos u organizaciones.", "E"),
            ("Sigo metodologías ordenadas, clasificación de archivos y gestión de registros.", "C"),
            ("Disfruto trabajar con hojas de cálculo, presupuestos y control de inventarios.", "C"),
            ("Prefiero entornos estructurados donde las normas y procesos estén bien definidos.", "C"),
            ("Me interesa supervisar el cumplimiento de normativas y la precisión de datos.", "C"),
            ("Me gusta organizar agendas, calendarios de eventos y expedientes administrativos.", "C")
        ]
        cursor.executemany(
            "INSERT INTO preguntas_riasec (pregunta, dimension) VALUES (?, ?)",
            preguntas_uafam
        )

    conn.commit()
    conn.close()

inicializar_base_de_datos()