# OriUAFAM AI — Prototipo

Plataforma de acompañamiento para el ciclo de vida estudiantil mediante
orientación académica y vocacional (UAFAM). Este repositorio contiene el
arranque técnico del prototipo, en paralelo a la espera de aprobación
del tema por parte del CTG.

## Arquitectura (según Cap. II 2.4.1 y Cap. IV 4.3.1 de la tesis)

El código está organizado en las mismas 4 capas descritas en la tesis:

| Capa | Carpeta |
|---|---|
| Presentación | `app.py`, `paginas/` |
| Aplicación (lógica de negocio) | `modelos/`, `logica/` |
| Inteligencia artificial | `ia/` |
| Datos | `database/`, `datos/` |

## Entidades de la base de datos (Cap. IV 4.3.3)

`Usuario`, `PerfilEstudiante`, `Interaccion`, `Recomendacion`,
`ContenidoOrientacion`, `Derivacion`, `Configuracion`.

Ver el detalle de columnas en `database/esquema.sql`.

## Cómo arrancar el proyecto en Visual Studio Code

1. Abre esta carpeta en VS Code (`Archivo > Abrir carpeta...`).
2. Crea el entorno virtual:
   ```
   python -m venv venv
   ```
3. Activa el entorno virtual:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```
5. Crea la base de datos:
   ```
   python -m database.inicializar_bd
   ```
6. Ejecuta la app:
   ```
   streamlit run app.py
   ```

## Estado actual

Ya implementado dentro de `paginas/`, con pruebas funcionales pasadas
(incluyendo levantar la app real con `streamlit run` sin errores):

- **RF-01** — Registro e inicio de sesión (`login.py`).
- **RF-02** — Perfil estudiantil, crear y editar (`perfil.py`).
- **RF-03** — Orientación académica: consulta + recomendación (`orientacion_academica.py`).
- **RF-04** — Orientación vocacional: consulta + recomendación, usando
  los intereses del perfil como contexto (`orientacion_vocacional.py`).
- **RF-05** — Asistente conversacional tipo chat (`asistente.py`),
  apoyado en la capa de IA (`ia/asistente.py`).
- **RF-06** — Motor de recomendaciones por reglas simples
  (`logica/motor_recomendaciones.py`), usado como respaldo automático
  cuando no hay servicio de IA configurado.
- **RF-07** — Módulo de recursos con filtro por categoría y búsqueda
  (`recursos.py`).
- **RF-08** — Historial de interacciones y recomendaciones (`historial.py`).
- **RF-09** — Derivación automática por palabras clave
  (`logica/derivacion_automatica.py`), integrada en el asistente.
- **RF-10** — Panel de administración básico: usuarios, derivaciones
  pendientes y alta de contenidos (`administracion.py`), visible solo
  para usuarios con rol `administrador`.

### Sobre la capa de IA (RF-05)

`ia/asistente.py` intenta usar un servicio real (Anthropic) si
encuentra la variable de entorno `ANTHROPIC_API_KEY` configurada.
Si no la encuentra, o si la llamada falla por cualquier razón (sin
internet, clave inválida), cae automáticamente al motor de reglas
simple — así el prototipo nunca se queda sin responder durante las
pruebas. Cuando consigas una clave real, solo tienes que configurarla
como variable de entorno; no hace falta tocar código.

### Pendiente / ideas para seguir

- Reemplazar el hash de contraseñas (SHA-256 simple) por `bcrypt` antes
  de una versión final.
- El motor de reglas (RF-06) sigue siendo muy simple (sugiere el
  contenido más reciente de la categoría); se puede volver más
  sofisticado sin tocar el resto de la app, ya que está aislado en un
  solo archivo.
- La clasificación de categoría dentro del asistente conversacional
  usa palabras clave (heurística), no un análisis real — es un punto
  natural para mejorar más adelante.
- Todavía no hay pruebas automatizadas (unittest/pytest); por ahora la
  validación se hizo manualmente ejecutando cada módulo.

**Nota:** esta estructura y el esquema de base de datos son
preliminares — la propia tesis indica que la estructura definitiva de
tablas, atributos, claves y relaciones se define durante el
desarrollo. Este código está pensado para evolucionar junto con el
tema una vez sea aprobado por el CTG.
