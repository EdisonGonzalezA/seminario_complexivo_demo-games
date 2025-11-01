import os
import pandas as pd
from scripts.data_louder import cargar_datos
from scripts.model_preprocessing import preparar_datos_modelo, dividir_datos
from scripts.model_training import entrenar_y_evaluar_modelo
from scripts.model_saving import guardar_archivos_modelo

# definiendo rutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ruta del dataset limpio (entrada)
DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "games_clean.csv")

# ruta de salida
MODEL_DIR = os.path.join(BASE_DIR, "models")

# ruta del OneHotEncoder
ENCODER_PATH = os.path.join(MODEL_DIR, "onehot_encoder.joblib")

# ruta del modelo LGBM
MODEL_PATH = os.path.join(MODEL_DIR, "lgbm_regressor_default.joblib")


if __name__ == "__main__":
    # indica dónde está el script actual
    print("---INICIANDO PIPELINE DE ENTRENAMIENTO DE MODELO---")

    # llama a la función de arriba para cargar el csv
    df_clean = cargar_datos(DATA_PATH)

    if df_clean is not None:
        print("\n---PREPROCESANDO DATOS PARA EL MODELO---")

        X, y, encoder = preparar_datos_modelo(df_clean)

        print("\n---DIVIDIR DATOS (TRAIN/TEST)---")

        X_train, X_test, y_train, y_test = dividir_datos(X, y)

        print("\n---ENTRENANDO Y EVALUANDO MODELO---")
        modelo = entrenar_y_evaluar_modelo(
            X_train, X_test, y_train, y_test
        )

        print("\n---GUARDANDO ARCHIVOS DEL MODELO---")
        guardar_archivos_modelo(
            modelo,
            encoder,
            MODEL_PATH,
            ENCODER_PATH
        )

        print("\n---PIPELINE DE ENTRENAMIENTO TERMINADO---")

    else:
        print("Error: no se pudo cargar el archivo")
