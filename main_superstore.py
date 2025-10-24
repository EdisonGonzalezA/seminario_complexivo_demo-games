# %%
import os
from script_superstore.data_louder import cargar_datos_excel

# RUTA ABSOLUTA DE LA CARPETA DONDE ESTA EL SCRIPT (.../SCRIPT/)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Ceonstruir la ruta del archivo csv de data
EXCEL_PATH = os.path.join(SCRIPT_DIR, ".", "data", "Sample - Superstore.xls")

# ¿Este archivo se esta ejecuntamndo directamente por el usuario o esta siendo importado por otro dscript?
if __name__ == "__main__":
    # indica donde esta el script actual
    print(f"Ejecutando script desde:  {os.path.abspath(__file__)}")

    hojas = ["Orders", "People", "Returns"]

    # llama a la funcion de arriba para cargar el csv
    diccionario_dataframes = cargar_datos_excel(EXCEL_PATH, hojas)

    if diccionario_dataframes is not None:
        for nombre_hoja, df in diccionario_dataframes.items():
            print("\n---Primeras 5 Filas de {nombre_hoja} ---")
            print(df.head())

            print("\n---Informacion del DataFrame de {nombre_hoja} ---")
            df.info(show_counts=True)
