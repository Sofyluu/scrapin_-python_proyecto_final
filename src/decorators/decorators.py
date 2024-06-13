import time  # Importamos el modulo time para medir el tiempo de ejecucion
import logging  # Sirve para registrar mensajes

# Configuramos el logger

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


"""
Configuramos el registro de mensajes (LOGGING) para que muestre mensajes de nivel INFO y superior
Definimos el formato de los mensajes de registro, incluyendo la marca del tiempo (asctime), el nivel de mensaje (levelname), y el mensaje(message)
"""


def timeit(func):
    """Decorador para medir el tiempo de ejecucion en una funcion"""
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Registramos el tiempo de inicio
        result = func(*args, **kwargs)  # Ejecutamos la funcion decoradora.
        end_time = time.time()  # Registramos el tiempo de finalizacion
        # Calculamos el tiempo transcurrido.
        elapsed_time = end_time - start_time
        # Registramos el tiempo de ejecucion
        logging.info(f"{func .__name__} ejecutada en {elapsed_time: .4f} seconds")
        return result  # Retornamos el resultado de la funcion
    return wrapper  # Devolvemos el decorador


def logit(func):
    """Decorador para registrar la ejecucion de una funcion"""
    def wrapper(*args, **kwargs):
        # Registramos el inicio de la ejecucion
        logging.info(f"Corriendo {func .__name__}")
        result = func(*args, **kwargs)  # Ejecutamos la funcion decoradora
        logging.info(f"Completado {func .__name__}")  # Registramos
        return result  # Devolvemos el resultado de la funcion
    return wrapper
