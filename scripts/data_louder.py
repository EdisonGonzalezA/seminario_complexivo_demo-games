import pandas as pd


# creacion de funcion
def cargar_datos(path):
    print(f"Cargando datos desde {path}...")

    try:
        df = pd.read_csv(path, encoding="latin1")
        print("Datos cargados exitosamente.")
        return df
    except FileNotFoundError:
        print(f"Error: no se encontro el archivo en {path}.")
        print("Por favor, asegurese de que el archivo este en la carpeta 'data'.")
        return None
    except Exception as e:
        print(f"Ocurrio un error inesperado {e}")
        return None
