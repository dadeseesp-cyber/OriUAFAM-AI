-- =====================================================================
-- esquema.sql
-- Esquema de base de datos para la plataforma OriUAFAM AI
-- Universidad Agroforestal Fernando Arturo de Meriño (UAFAM)
-- Licenciatura en Informática
-- =====================================================================

PRAGMA foreign_keys = ON;

-- ---------------------------------------------------------------------
-- Usuario: Autenticación y roles de usuario
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS Usuario (
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    correo TEXT NOT NULL UNIQUE,
    contrasena_hash TEXT NOT NULL,
    rol TEXT NOT NULL DEFAULT 'estudiante' CHECK (rol IN ('estudiante', 'administrador')),
    activo INTEGER NOT NULL DEFAULT 1,
    fecha_registro TEXT NOT NULL DEFAULT (datetime('now'))
);

-- ---------------------------------------------------------------------
-- PerfilEstudiante: Información académica y perfil del estudiante
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS PerfilEstudiante (
    id_perfil INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL UNIQUE,
    matricula TEXT,
    carrera TEXT,
    etapa_ciclo_vida TEXT,
    intereses TEXT,
    fecha_actualizacion TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (id_usuario) REFERENCES Usuario (id_usuario) ON DELETE CASCADE
);

-- ---------------------------------------------------------------------
-- Interaccion: Registro de consultas del asistente y del test
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS Interaccion (
    id_interaccion INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER NOT NULL,
    tipo_interaccion TEXT NOT NULL,
    contenido_consulta TEXT NOT NULL,
    contenido_respuesta TEXT,
    fecha_hora TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (id_usuario) REFERENCES Usuario (id_usuario) ON DELETE CASCADE
);

-- ---------------------------------------------------------------------
-- historial_interacciones: Tabla compatible para la vista de Historial
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS historial_interacciones (
    id_interaccion INTEGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTEGER,
    tipo_interaccion TEXT,
    consulta TEXT,
    respuesta TEXT,
    fecha_interaccion DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario) ON DELETE CASCADE
);

-- ---------------------------------------------------------------------
-- Recomendacion: Recomendaciones generadas por el sistema
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS Recomendacion (
    id_recomendacion INTEGER PRIMARY KEY AUTOINCREMENT,
    id_interaccion INTEGER NOT NULL,
    categoria TEXT NOT NULL,
    contenido TEXT NOT NULL,
    fecha_generacion TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (id_interaccion) REFERENCES Interaccion (id_interaccion) ON DELETE CASCADE
);

-- ---------------------------------------------------------------------
-- ContenidoOrientacion: Módulo de recursos y documentos institucionales
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS ContenidoOrientacion (
    id_contenido INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descripcion TEXT,
    categoria TEXT NOT NULL,
    tipo_recurso TEXT,
    url_o_ruta TEXT,
    fecha_creacion TEXT NOT NULL DEFAULT (datetime('now'))
);

-- ---------------------------------------------------------------------
-- Derivacion: Remisión a atención humana en la UAFAM
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS Derivacion (
    id_derivacion INTEGER PRIMARY KEY AUTOINCREMENT,
    id_interaccion INTEGER NOT NULL,
    motivo TEXT NOT NULL,
    canal_recomendado TEXT,
    atendida INTEGER NOT NULL DEFAULT 0,
    fecha TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY (id_interaccion) REFERENCES Interaccion (id_interaccion) ON DELETE CASCADE
);

-- ---------------------------------------------------------------------
-- Configuracion: Parámetros generales del sistema
-- ---------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS Configuracion (
    id_configuracion INTEGER PRIMARY KEY AUTOINCREMENT,
    clave TEXT NOT NULL UNIQUE,
    valor TEXT,
    descripcion TEXT
);