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

st.write("Seleccione su nivel de español:")
spanish_beginner = st.checkbox("Principiante", key="spanish_beginner")
spanish_intermediate = st.checkbox("Intermedio", key="spanish_intermediate")
spanish_advanced = st.checkbox("Avanzado", key="spanish_advanced")
spanish_native = st.checkbox("Nativo/Fluido", key="spanish_native")

st.write("Seleccione su nivel de inglés:")
english_beginner = st.checkbox("Principiante", key="english_beginner")
english_intermediate = st.checkbox("Intermedio", key="english_intermediate")
english_advanced = st.checkbox("Avanzado", key="english_advanced")
english_native = st.checkbox("Nativo/Fluido", key="english_native")

# Notificación sobre el Proceso de Evaluación
st.header("Notificación sobre el Proceso de Evaluación")
screening_ack = st.checkbox(
    "Reconozco que podrían requerirse evaluaciones adicionales (por ejemplo, pruebas de traducción, entrevistas)."
)

# Validar selección de niveles
def validate_language_levels(*args):
    return sum(args) == 1

spanish_valid = validate_language_levels(spanish_beginner, spanish_intermediate, spanish_advanced, spanish_native)
english_valid = validate_language_levels(english_beginner, english_intermediate, english_advanced, english_native)

# Botón de Envío
if st.button("Enviar Solicitud"):
    if (
        full_name and email and phone and screening_ack
        and spanish_valid and english_valid
    ):
        st.success("¡Gracias por su solicitud! Revisaremos su información y nos pondremos en contacto para los próximos pasos.")
    else:
        st.error("Por favor complete todos los campos requeridos, seleccione un nivel para cada idioma y reconozca el proceso de evaluación.")

# Opcional: Mostrar entrada del usuario para confirmación (para pruebas)
st.write("### Su Entrada:")
st.write(f"Nombre Completo: {full_name}")
st.write(f"Correo Electrónico: {email}")
st.write(f"Número de Teléfono: {phone}")
st.write(f"País de Residencia: {country}")
# st.write(f"Autorizado para trabajar: {authorized}")

# Mostrar niveles seleccionados
st.write("Nivel de Español:")
if spanish_beginner: st.write("- Principiante")
if spanish_intermediate: st.write("- Intermedio")
if spanish_advanced: st.write("- Avanzado")
if spanish_native: st.write("- Nativo/Fluido")

st.write("Nivel de Inglés:")
if english_beginner: st.write("- Principiante")
if english_intermediate: st.write("- Intermedio")
if english_advanced: st.write("- Avanzado")
if english_native: st.write("- Nativo/Fluido")

st.write(f"Proceso de Evaluación Reconocido: {'Sí' if screening_ack else 'No'}")
