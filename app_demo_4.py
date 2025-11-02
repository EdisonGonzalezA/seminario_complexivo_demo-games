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

# st.selectbox
opcion_sb = st.selectbox(" ¡Escoge una opción! (Selectbox)", [
    "Opción A", "Opción B", "Opción C"])

# st.radio
opcion_r = st.radio("¡Escoge una opcion! (Radio)", [
    "Opción A", "Opción B", "Opción C"])
st.write(f"Selectbox: {opcion_sb}, Radio: {opcion_r}")

# st.multiselect
opciones_multi = st.multiselect(
    "Elige tu genero de videojuego favorito:",
    ["Accion", "Puzzle", "Stragy", "Shooter"],
    default=["Accion"]
)
st.write(f"Sewleccionado: {opciones_multi}")

# st.slider con dos valores
st.header("Seleccion de rango: Slider tipo tupla")

rango_anios = st.slider(
    "Seleccioona un rango de años",
    # valor minimo, valor maximo, default del rango
    2000, 2023, (2010, 2015)
)
st.write(f"eL sLIDER DEVUELVE UNA TUPLA: {rango_anios}")


# st.code
st.write("Aqui estoy mosdtrando un codigo de Pandas")
st.code(
    "pd.read_csv(ruta)",
    language="Python"
)

# Elementos de notificaciones
st.header("Notificacxiones")

# Notificaciones visuales
st.success("Los datos fueron cargadoos correctamente")
st.warning("El dataset tiene valores nulos")
st.error("No se pudo conectar a la base de datos")

# st.metric
st.metric(
    label="Ventas Totales",
    value="$1,220,000",
    delta="$50,000 vs mes anterior"
)
