import io
import re
import streamlit as st

try:
    from gtts import gTTS
    GTTS_DISPONIBLE = True
except ImportError:
    GTTS_DISPONIBLE = False


def limpiar_texto_para_voz(texto):
    """Limpia marcas Markdown para que la lectura por voz suene natural."""
    texto_limpio = re.sub(r"\*\*(.*?)\*\*", r"\1", texto)
    texto_limpio = re.sub(r"\*(.*?)\*", r"\1", texto_limpio)
    texto_limpio = re.sub(r"`(.*?)`", r"\1", texto_limpio)
    texto_limpio = re.sub(r"\s+", " ", texto_limpio).strip()
    return texto_limpio


def generar_audio_espanol(texto):
    """Genera bytes MP3 en español con gTTS; devuelve None si no es posible."""
    if not GTTS_DISPONIBLE or not texto:
        return None
    try:
        texto_voz = limpiar_texto_para_voz(texto)
        if not texto_voz:
            return None
        buffer_audio = io.BytesIO()
        tts = gTTS(text=texto_voz, lang="es", slow=False)
        tts.write_to_fp(buffer_audio)
        buffer_audio.seek(0)
        return buffer_audio.getvalue()
    except Exception:
        return None


def responder_consulta(pregunta, nombre_estudiante):
    """Genera respuestas contextualizadas según la consulta del estudiante."""
    pregunta_lower = pregunta.lower()

    if "prerrequisito" in pregunta_lower or "informática" in pregunta_lower or "pensum" in pregunta_lower:
        return (
            f"Con gusto te oriento, **{nombre_estudiante}**. En la carrera de Licenciatura en Informática de la UAFAM, "
            "las asignaturas de programación y bases de datos siguen una secuencia obligatoria. Puedes verificar el mapa "
            "completo y tus materias desbloqueadas en el **Módulo 4 (Pensum y Prerrequisitos)**."
        )
    elif "riasec" in pregunta_lower or "vocacional" in pregunta_lower or "perfil" in pregunta_lower:
        return (
            f"Tu perfil RIASEC evalúa seis dimensiones vocacionales (Realista, Investigador, Artístico, Social, Emprendedor y Convencional). "
            f"**{nombre_estudiante}**, si aún no has completado la evaluación de 20 preguntas o deseas descargar tu informe en PDF, "
            "dirígete al **Módulo 2 (Orientación RIASEC)**."
        )
    elif "centro" in pregunta_lower or "información" in pregunta_lower or "biblioteca" in pregunta_lower:
        return (
            f"El **Centro de Información (Módulo 7)** centraliza los reglamentos académicos, el calendario institucional 2027 "
            f"y los enlaces directos a la biblioteca digital de la UAFAM para apoyar tus investigaciones, **{nombre_estudiante}**."
        )
    elif "cita" in pregunta_lower or "orientador" in pregunta_lower or "académica" in pregunta_lower:
        return (
            f"Para recibir acompañamiento personalizado con un orientador de la UAFAM, puedes agendar una sesión directamente "
            f"desde el **Módulo 3 (Orientación Académica)**, **{nombre_estudiante}**."
        )
    else:
        return (
            f"He registrado tu consulta sobre *'{pregunta}'*, **{nombre_estudiante}**. Como asistente institucional de la UAFAM, "
            "te recomiendo revisar las normativas vigentes en el **Centro de Información (Módulo 7)** o agendar una asesoría "
            "en el **Módulo 3** si requieres validación directa de coordinación académica."
        )


def mostrar_asistente_ia(usuario=None):
    # Extraer el nombre real del estudiante desde la sesión activa
    nombre_estudiante = "Estudiante"
    if isinstance(usuario, dict):
        nombre_estudiante = usuario.get("nombre", "Estudiante")
    elif isinstance(st.session_state.get("usuario"), dict):
        nombre_estudiante = st.session_state["usuario"].get("nombre", "Estudiante")

    # Encabezado principal
    st.title("🤖 Ori — Asistente Académico y Vocacional")
    st.write(
        f"Bienvenida/o, **{nombre_estudiante}**. Tu compañera virtual con inteligencia artificial para orientarte en normativas, procesos y vida universitaria en la UAFAM."
    )

    # Indicador de estado y botón de reinicio de chat
    col_estado, col_audio_toggle, col_limpiar = st.columns([4, 3, 2])
    with col_estado:
        st.success("🟢 **Ori está activa** · Conectada al perfil estudiantil")
    with col_audio_toggle:
        leer_automatico = st.toggle(
            "🔊 Audio automático",
            value=False,
            help="Reproduce en voz alta cada respuesta nueva de Ori"
        )
    with col_limpiar:
        if st.button("🔄 Nueva conversación", use_container_width=True):
            st.session_state.mensajes_ori_v3 = [
                {
                    "role": "assistant",
                    "content": f"¡Hola **{nombre_estudiante}**! Soy **Ori**, tu asistente inteligente de OriUAFAM AI. ¿En qué puedo apoyarte hoy con tu planificación académica, tus asignaturas o tu orientación vocacional?"
                }
            ]
            st.session_state.pop("ultimo_audio_ori", None)
            st.rerun()

    if not GTTS_DISPONIBLE:
        st.caption("ℹ️ Para activar la voz en español de Ori, instala `gTTS` en tu entorno (`pip install gTTS`). El chat escrito funciona con normalidad.")

    st.markdown("---")

    # Expansor de alcance del sistema
    with st.expander("💡 ¿Qué consultas puedes realizarle a Ori? (Alcance del Sistema)"):
        st.markdown("""
- **Orientación Académica:** Fechas de inscripción, régimen cuatrimestral 2027 y agendamiento de citas.
- **Pensum y Prerrequisitos:** Secuencia curricular de Licenciatura en Informática y materias clave.
- **Servicios Institucionales:** Horarios del centro de información, biblioteca digital y reglamentos.
- **Orientación Vocacional:** Interpretación de resultados del test RIASEC y generación de reportes PDF.
        """)

    # Inicializar historial limpio (v3 para limpiar cualquier caché anterior)
    if "mensajes_ori_v3" not in st.session_state:
        st.session_state.mensajes_ori_v3 = [
            {
                "role": "assistant",
                "content": f"¡Hola **{nombre_estudiante}**! Soy **Ori**, tu asistente inteligente de OriUAFAM AI. ¿En qué puedo apoyarte hoy con tu planificación académica, tus asignaturas o tu orientación vocacional?"
            }
        ]

    # Botones de consultas rápidas contextuales
    st.markdown("**📌 Consultas rápidas sugeridas:**")
    col1, col2, col3, col4 = st.columns(4)

    consulta_boton = None
    with col1:
        if st.button("📚 Prerrequisitos", use_container_width=True):
            consulta_boton = "¿Cuáles son los prerrequisitos de Informática?"
    with col2:
        if st.button("🧭 Test RIASEC", use_container_width=True):
            consulta_boton = "¿Cómo interpreto mi perfil RIASEC?"
    with col3:
        if st.button("📅 Agendar Cita", use_container_width=True):
            consulta_boton = "¿Cómo agendo una cita de orientación académica?"
    with col4:
        if st.button("🏛️ Biblioteca", use_container_width=True):
            consulta_boton = "¿Qué servicios ofrece el Centro de Información?"

    if consulta_boton:
        st.session_state.mensajes_ori_v3.append({"role": "user", "content": consulta_boton})
        respuesta = responder_consulta(consulta_boton, nombre_estudiante)
        st.session_state.mensajes_ori_v3.append({"role": "assistant", "content": respuesta})
        if leer_automatico:
            st.session_state["ultimo_audio_ori"] = generar_audio_espanol(respuesta)
        st.rerun()

    st.markdown("---")

    # Reproductor de audio automático si se activó para la última respuesta
    if leer_automatico and st.session_state.get("ultimo_audio_ori"):
        st.audio(st.session_state["ultimo_audio_ori"], format="audio/mp3", autoplay=True)

    # Renderizar historial de mensajes con opción de escuchar cualquier respuesta
    for idx, mensaje in enumerate(st.session_state.mensajes_ori_v3):
        with st.chat_message(mensaje["role"], avatar="🤖" if mensaje["role"] == "assistant" else "👤"):
            st.markdown(mensaje["content"])
            if mensaje["role"] == "assistant":
                if st.button("🔊 Escuchar respuesta", key=f"btn_audio_{idx}"):
                    audio_bytes = generar_audio_espanol(mensaje["content"])
                    if audio_bytes:
                        st.audio(audio_bytes, format="audio/mp3", autoplay=True)
                    else:
                        st.warning("No se pudo generar el audio en este momento. Verifica que `gTTS` esté instalado y que haya conexión.")

    # Entrada de texto libre del estudiante
    pregunta = st.chat_input(f"Escribe tu consulta para Ori, {nombre_estudiante}...")
    if pregunta:
        st.session_state.mensajes_ori_v3.append({"role": "user", "content": pregunta})
        with st.chat_message("user", avatar="👤"):
            st.markdown(pregunta)

        respuesta_ori = responder_consulta(pregunta, nombre_estudiante)
        st.session_state.mensajes_ori_v3.append({"role": "assistant", "content": respuesta_ori})

        audio_generado = generar_audio_espanol(respuesta_ori) if leer_automatico else None
        if audio_generado:
            st.session_state["ultimo_audio_ori"] = audio_generado

        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(respuesta_ori)
            if audio_generado:
                st.audio(audio_generado, format="audio/mp3", autoplay=True)


# =========================================================================
# Ejecución del módulo
# =========================================================================
if __name__ == "__main__":
    mostrar_asistente_ia()
else:
    usuario_activo = st.session_state.get("usuario_actual") or st.session_state.get("usuario")
    mostrar_asistente_ia(usuario_activo)