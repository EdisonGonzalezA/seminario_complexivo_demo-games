import streamlit as st
import time
import datetime

# titulo
st.title("Este es un titulo")

st.write("Este es un texto")

# la hora actual
ahora = datetime.datetime.now()

hora_formateada = ahora.strftime("%H:%M:%S")

st.write(f"Hora actual: {hora_formateada}")

st.write(f"Timestand: {time.time()}")

# st.slider() un widget deslizable
valor_slider = st.slider("Mueve este slider", 0, 100, 25)
st.write(f"EI valor seleccionado es {valor_slider}")

# st.button()
if st.button("Predecir datos"):
    st.write("Se han predecido los datos")

st.header("Selección única: Selectbox vs. Radio")

opcion_sb = st. selectbox(" i Escoge una opción! (Selectbox)", [
                          "Opción A", "Opción B", "Opción C"])

opcion_r = st.radio("¡Escoge una opcion! (Radio)", [
                    "Opción A", "Opción B", "Opción C"])
st.write(f"Selectbox: {opcion_sb}")
