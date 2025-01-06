import streamlit as st

# Título de la aplicación
st.title("Formulario de Reclutamiento de Traductores")
st.subheader("Posición: Traductor de Español a Inglés")

# Sección de Información Personal
st.header("Información Personal")
full_name = st.text_input("Nombre Completo")
email = st.text_input("Correo Electrónico")
phone = st.text_input("Número de Teléfono")
country = st.text_input("País de Residencia")
# authorized = st.radio("¿Está legalmente autorizado para trabajar en este país?", ("Sí", "No"))

# Sección de Competencia Lingüística
st.header("Competencia Lingüística")
spanish_level = st.selectbox(
    "¿Cómo calificaría su nivel de español?",
    ["Principiante", "Intermedio", "Avanzado", "Nativo/Fluido"]
)
english_level = st.selectbox(
    "¿Cómo calificaría su nivel de inglés?",
    ["Principiante", "Intermedio", "Avanzado", "Nativo/Fluido"]
)

# Notificación sobre el Proceso de Evaluación
st.header("Notificación sobre el Proceso de Evaluación")
screening_ack = st.checkbox(
    "Reconozco que podrían requerirse evaluaciones adicionales (por ejemplo, pruebas de traducción, entrevistas)."
)

# Botón de Envío
if st.button("Enviar Solicitud"):
    if full_name and email and phone and screening_ack:
        st.success("¡Gracias por su solicitud! Revisaremos su información y nos pondremos en contacto para los próximos pasos.")
    else:
        st.error("Por favor complete todos los campos requeridos y reconozca el proceso de evaluación.")

# Opcional: Mostrar entrada del usuario para confirmación (para pruebas)
st.write("### Su Entrada:")
st.write(f"Nombre Completo: {full_name}")
st.write(f"Correo Electrónico: {email}")
st.write(f"Número de Teléfono: {phone}")
st.write(f"País de Residencia: {country}")
# st.write(f"Autorizado para trabajar: {authorized}")
st.write(f"Nivel de Español: {spanish_level}")
st.write(f"Nivel de Inglés: {english_level}")
st.write(f"Proceso de Evaluación Reconocido: {'Sí' if screening_ack else 'No'}")
