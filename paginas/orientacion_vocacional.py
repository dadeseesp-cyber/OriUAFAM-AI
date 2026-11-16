import streamlit as st
from database.conexion import obtener_conexion
from modelos.contenido_orientacion import guardar_resultado_vocacional
from modelos.reporte_pdf import generar_reporte_vocacional_pdf

def obtener_preguntas_vocacionales():
    """Obtiene las preguntas RIASEC desde la base de datos."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("SELECT id, pregunta, dimension FROM preguntas_riasec")
    preguntas = cursor.fetchall()
    conn.close()
    return preguntas

def obtener_valor_usuario(usuario, claves, valor_defecto=""):
    """Obtiene un valor del objeto o diccionario usuario probando múltiples nombres de clave."""
    if isinstance(usuario, dict):
        for clave in claves:
            if clave in usuario and usuario[clave] is not None:
                return usuario[clave]
    else:
        for clave in claves:
            if hasattr(usuario, clave) and getattr(usuario, clave) is not None:
                return getattr(usuario, clave)
    return valor_defecto

def mostrar_orientacion_vocacional(usuario):
    st.title("🎓 Orientación Vocacional (Test RIASEC)")
    st.write("Responde el siguiente cuestionario para identificar tus áreas de mayor afinidad profesional.")

    preguntas = obtener_preguntas_vocacionales()

    if not preguntas:
        st.warning("No hay preguntas registradas en el sistema.")
        return

    st.markdown("---")
    respuestas = {}

    with st.form("form_test_riasec"):
        st.subheader("Cuestionario de Intereses Profesionales")
        st.caption("Selecciona tu nivel de interés para cada una de las siguientes afirmaciones:")

        opciones_escala = {
            1: "1 - Nada de acuerdo / No me interesa",
            2: "2 - Poco de acuerdo",
            3: "3 - Neutral / Indiferente",
            4: "4 - De acuerdo",
            5: "5 - Muy de acuerdo / Me apasiona"
        }

        # Usamos enumerate(..., start=1) para que se muestren numeradas limpiamente desde el 1
        for idx, p in enumerate(preguntas, start=1):
            p_id = p["id"]
            p_texto = p["pregunta"]
            p_dim = p["dimension"]

            st.write(f"**{idx}. {p_texto}**")
            val = st.radio(
                f"Evaluación P{p_id}",
                options=[1, 2, 3, 4, 5],
                format_func=lambda x: opciones_escala[x],
                key=f"pregunta_{p_id}",
                label_visibility="collapsed"
            )
            respuestas[p_id] = {"dimension": p_dim, "valor": val}
            st.write("")

        enviado = st.form_submit_button("📊 Evaluar Respuestas y Generar Resultado", type="primary")

    if enviado:
        # Calcular puntajes RIASEC
        puntajes = {"R": 0, "I": 0, "A": 0, "S": 0, "E": 0, "C": 0}
        for resp in respuestas.values():
            puntajes[resp["dimension"]] += resp["valor"]

        # Ordenar dimensiones de mayor a menor
        ordenados = sorted(puntajes.items(), key=lambda x: x[1], reverse=True)
        top_tres = [item[0] for item in ordenados[:3]]
        codigo_riasec = "".join(top_tres)

        # Mapeo de carreras UAFAM según dimensión principal
        carreras_map = {
            "I": "Licenciatura en Informática (INF)",
            "R": "Ingeniería Agronómica (IAG)",
            "E": "Licenciatura en Administración de Empresas (LAE)",
            "C": "Licenciatura en Contabilidad (LCO)",
            "A": "Licenciatura en Turismo Sustentable (LTS)",
            "S": "Licenciatura en Administración / Turismo"
        }
        dim_principal = top_tres[0]
        carrera_sugerida = carreras_map.get(dim_principal, "Licenciatura en Informática (INF)")

        # Extraer datos de usuario de forma segura con soporte para múltiples nombres de claves
        usuario_id = obtener_valor_usuario(usuario, ["id", "id_usuario", "usuario_id"], 1)
        nombre_usuario = obtener_valor_usuario(usuario, ["nombre", "nombre_completo", "usuario"], "Estudiante UAFAM")
        correo_usuario = obtener_valor_usuario(usuario, ["correo", "email"], "estudiante@uafam.edu.do")

        guardar_resultado_vocacional(usuario_id, codigo_riasec, carrera_sugerida)

        st.success("¡Evaluación completada con éxito!")
        st.subheader(f"🎯 Tu código de perfil RIASEC: **{codigo_riasec}**")
        st.info(f"🎓 Carrera UAFAM sugerida: **{carrera_sugerida}**")

        # Desglose de puntajes
        st.write("### Desglose por Dimensión:")
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        col1.metric("Realista (R)", puntajes["R"])
        col2.metric("Investigador (I)", puntajes["I"])
        col3.metric("Artístico (A)", puntajes["A"])
        col4.metric("Social (S)", puntajes["S"])
        col5.metric("Emprendedor (E)", puntajes["E"])
        col6.metric("Convencional (C)", puntajes["C"])

        # Generar reporte PDF
        try:
            pdf_bytes = generar_reporte_vocacional_pdf(
                nombre_estudiante=nombre_usuario,
                correo_estudiante=correo_usuario,
                codigo_riasec=codigo_riasec,
                carrera_sugerida=carrera_sugerida,
                puntajes=puntajes
            )
            st.download_button(
                label="📄 Descargar Informe Oficial (PDF)",
                data=pdf_bytes,
                file_name=f"Informe_Vocacional_{codigo_riasec}.pdf",
                mime="application/pdf",
                type="primary"
            )
        except Exception as e:
            st.warning(f"No se pudo generar la descarga del PDF en este momento: {e}")


# =========================================================================
# Lógica de renderizado para app.py / st.navigation
# =========================================================================
if "usuario_actual" in st.session_state and st.session_state["usuario_actual"]:
    mostrar_orientacion_vocacional(st.session_state["usuario_actual"])
elif "usuario" in st.session_state and st.session_state["usuario"]:
    mostrar_orientacion_vocacional(st.session_state["usuario"])
else:
    st.warning("Por favor, inicia sesión para acceder al módulo de Orientación RIASEC.")