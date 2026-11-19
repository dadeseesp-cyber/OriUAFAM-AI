"""
login.py
Pantalla de registro e inicio de sesión — RF-01.
"""

import streamlit as st
from config import ROLES_PERMITIDOS
from modelos.usuario import crear_usuario, verificar_credenciales, obtener_usuario_por_correo


def mostrar_login():
    st.header("Acceso a OriUAFAM AI")

    pestaña_ingreso, pestaña_registro = st.tabs(["Iniciar sesión", "Registrarme"])

    # -------------------- Iniciar sesión --------------------
    with pestaña_ingreso:
        with st.form("formulario_login"):
            correo = st.text_input("Correo", key="login_correo")
            contrasena = st.text_input("Contraseña", type="password", key="login_contrasena")
            enviado = st.form_submit_button("Entrar")

        if enviado:
            if not correo or not contrasena:
                st.warning("Completa correo y contraseña.")
            else:
                correo_limpio = correo.strip().lower()
                
                # Acceso directo para tu correo principal
                if correo_limpio == "dadeseesp@gmail.com":
                    usuario = obtener_usuario_por_correo(correo_limpio)
                    if usuario is None:
                        crear_usuario("Fe Wendy Esperanza", correo_limpio, contrasena, "estudiante")
                        usuario = obtener_usuario_por_correo(correo_limpio)
                    
                    usuario_dict = dict(usuario)
                    st.session_state["usuario"] = usuario_dict
                    st.session_state["usuario_actual"] = usuario_dict
                    st.session_state["rol"] = usuario_dict.get("rol", "estudiante")
                    st.success("¡Acceso concedido con éxito!")
                    st.rerun()
                else:
                    usuario = verificar_credenciales(correo, contrasena)
                    if usuario is None:
                        st.error("Correo o contraseña incorrectos.")
                    else:
                        usuario_dict = dict(usuario)
                        st.session_state["usuario"] = usuario_dict
                        st.session_state["usuario_actual"] = usuario_dict
                        st.session_state["rol"] = usuario_dict.get("rol", "estudiante")
                        st.success(f"Bienvenido/a, {usuario_dict['nombre']}")
                        st.rerun()

    # -------------------- Registrarme --------------------
    with pestaña_registro:
        with st.form("formulario_registro"):
            nombre = st.text_input("Nombre completo")
            correo_nuevo = st.text_input("Correo", key="reg_correo")
            contrasena_nueva = st.text_input("Contraseña", type="password", key="reg_pass1")
            contrasena_confirmar = st.text_input("Confirmar contraseña", type="password", key="reg_pass2")
            rol = st.selectbox("Rol", ROLES_PERMITIDOS, index=0)
            registrar = st.form_submit_button("Crear cuenta")

        if registrar:
            if not nombre or not correo_nuevo or not contrasena_nueva:
                st.warning("Completa todos los campos.")
            elif contrasena_nueva != contrasena_confirmar:
                st.warning("Las contraseñas no coinciden.")
            elif obtener_usuario_por_correo(correo_nuevo.strip().lower()) is not None:
                st.error("Ya existe una cuenta registrada con ese correo.")
            else:
                crear_usuario(nombre, correo_nuevo.strip().lower(), contrasena_nueva, rol)
                st.success("Cuenta creada correctamente. Ya puedes iniciar sesión.")
                st.balloons()