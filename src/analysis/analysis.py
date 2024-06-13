import pandas as pd  # importamos pandas para manejar y analizar datos
import os  # sirve para interactuar con el sistema operativo
# Importamos los decoradores personalizados
from ..decorators.decorators import timeit, logit


@logit  # Añadimos el loggin a la funcion
@timeit  # Medimos el tiempo de ejecucion de la funcion
def load_data(data_path):
    """Cargar los datos desde un archivo CSV o excel, en este caso archivo product.csv"""
    if data_path.endswith(".csv"):
        df = pd.read_csv(data_path)  # Cargamos datos de archivo csv
    elif data_path.endswith("xlsx"):  # Cargamos datos de archivo excel
        df = pd.read_excel(data_path)
    else:
        # Error si el formato del archivo no es compatible
        raise ValueError("Unsupported file format")
    # Imprimimos mensaje indicando que los datos se cargaron correctamente
    print("Data loaded successfully")
    return df  # Devolvemos DF con datos cargados


@logit  # Añadimos el loggin a la funcion
@timeit  # Medimos el tiempo de ejecucion de la funcion
def clean_data(df):
    """Limpiamos los datos"""
    df["price"] = df["price"].replace(
        r"[\$,]", "", regex=True).replace(",", ".").astype(float)
    print("Data cleaned Successfully")
    return df  # Devolvemos el DF con los datos formateados


@logit  # Añadimos el loggin a la funcion
@timeit  # Medimos el tiempo de ejecucion de la funcion
def analyze_data(df):
    """Realizamos un analisis basico de datos"""
    print("Basic Data Analysys: ")  # Imprimimos un encabezado para el analisis de datos
    print(df.describe())  # Imprimimos un resumen estadistico de los datos
    # Imprimimos un encabezado para los productos con precios mas altos
    print("\nProducts with highest prices: ")
    highestPrices = df.nlargest(5, "price")
    print(highestPrices)  # Imprimimos los 5 productos con precios mas altos
    return highestPrices


@logit  # Añadimos el loggin a la funcion
@timeit  # Medimos el tiempo de ejecucion de la funcion
def save_clean_data(df, outputh_path):
    """Guardamos los datos limpios en un archivo CSV"""
    if outputh_path.endswith(".csv"):
        # Guardamos los datos en un archivo CSV
        df.to_csv(outputh_path, index=False)
    elif outputh_path.endswith(".xlsx"):
        # Guadamos los datos en el archivo Excel
        df.to_excel(outputh_path, index=False)
    else:
        # Lanzamos un error si el formato del archivo no es compatible
        raise ValueError("Unsupported file format")
    print(f"Clean data saved to {outputh_path}")


if __name__ == "__main__":  # Permitimos que el script solo se ejecute este archivo

    # Definimos la ruta del archivo de datos sin procesar
    data_path = "data/raw/products.csv"
    # Definimos la ruta del archivo de datos procesados
    outputh_path = "data/processed/cleaned_products.csv"

    # Cargamos  los datos de un archivo especifico (datos en bruto)
    df = load_data(data_path)
    df = clean_data(df)  # Limpiamos los datos cargados
    df = analyze_data(df)  # Realizamos un analisis basico de la data
    # Creamos el directorio para los datos procesados si no existe
    os.makedirs("data/processed", exist_ok=True)
    # Gurdamos los datos limpios en el archivo especifico
    save_clean_data(df, outputh_path)
