# %%
import pandas as pd
import os

# RUTA ABSOLUTA DE LA CARPETA DONDE ESTA EL SCRIPT (.../SCRIPT/)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Ceonstruir la ruta del archivo csv de data
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "data", "games.csv")

# creacion de funcion


def cargar_datos(path):
    print(f"Cargando datos desde {path}...")

    try:
        df = pd.read_csv(path)
        print("Datos cargados exitosamente.")
        return df
    except FileNotFoundError:
        print(f"Error: no se encontro el archivo en {path}.")
        print("Por favor, asegurese de que el archivo este en la carpeta 'data'.")
        return None
    except Exception as e:
        print(f"Ocurrio un error inesperado {e}")
        return None


# ¿Este archivo se esta ejecuntamndo directamente por el usuario o esta siendo importado por otro dscript?
if __name__ == "__main__":
    # indica donde esta el script actual
    print(f"Ejecutando script desde:  {os.path.abspath(__file__)}")

    # llama a la funcion de arriba para cargar el csv
    dataframe_juegos = cargar_datos(DATA_PATH)

    if dataframe_juegos is not None:
        print("\n---Primeras 5 filas---")
        print(dataframe_juegos.head())

        print("\n---Informacion del Dataframe---")
        dataframe_juegos.info(show_counts=True)
