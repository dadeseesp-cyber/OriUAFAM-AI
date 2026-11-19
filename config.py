"""
config.py
Configuración general de OriUAFAM AI.

Aquí se centralizan rutas y constantes para que no queden
"quemadas" (hardcodeadas) dentro de cada módulo. Si más adelante
cambias de SQLite a otro motor, o mueves la carpeta de datos,
solo tocas este archivo.
"""

import os

# Carpeta raíz del proyecto (donde está este archivo)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Carpeta donde vivirá el archivo de base de datos SQLite
DATA_DIR = os.path.join(BASE_DIR, "datos")
os.makedirs(DATA_DIR, exist_ok=True)

# Ruta del archivo .db (SQLite guarda toda la BD en un solo archivo)
DB_PATH = os.path.join(DATA_DIR, "oriuafam.db")

# Ruta del esquema SQL que crea las tablas
ESQUEMA_SQL_PATH = os.path.join(BASE_DIR, "database", "esquema.sql")

# Nombre del prototipo (útil para títulos en la interfaz Streamlit)
NOMBRE_APP = "OriUAFAM AI"

# Roles de usuario permitidos (coincide con RF-01 / RF-10 de la tesis)
ROLES_PERMITIDOS = ("estudiante", "administrador")

# Etapas del ciclo de vida estudiantil consideradas en el prototipo
ETAPAS_CICLO_VIDA = (
    "ingreso",
    "permanencia",
    "egreso",
    "transicion_profesional",
)
