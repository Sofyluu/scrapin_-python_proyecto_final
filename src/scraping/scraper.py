import requests  # sirve para hacer las solicitudes HTTP
from bs4 import BeautifulSoup  # sirve para analizar los documentos HTML
import pandas as pd  # maneja los datos en los DataFrames


def fetch_page(url):
    """Obtenemos el contenido de una pagina."""
    # Realizamos una solicitud GET a la URL proporcionada
    response = requests.get(url)
    if response.status_code == 200:  # Comparamos el status code con el 200 que significa que fue una peticion exitosa
        return response.content  # Devuelve el contenido de la pag si la solicitud fue exitosa
    else:
        # Lanzamos una excepcion por si la solicitud falla
        raise Exception(f"Failes to fetch page: {url}")


def parse_product(product):
    """Analizamos los detalles de un producto"""
    # Encontramos y obtenemos el titulo, la descripcion y el precio  del producto
    title = product.find(
        "a", class_="product-item-link").text.strip()
    price = product.find(
        "span", class_="price").text.strip()
    return {  # retornamos un diccionaro con el titulo, descripcion y precio
        "title": title,
        # "description": description,
        "price": price,
    }


def scrape(url):
    """Funcion principal del scraping"""
    page_content = fetch_page(url)  # obtenemos el codigo base de la pagina
    # Analizamos el contenido de la pagina con BS
    soup = BeautifulSoup(page_content, "html.parser")
    # Encontramos todos los elementos con la clase que representan productos
    products = soup.find_all(
        "div", class_="product-item-info")
    products_data = []  # Inicializamos una lista para almacenar los datos de los productos

    for product in products:
        # Analizamos cada producto encontrado
        product_info = parse_product(product)
        # Agregamos los datos del producto a la lista
        products_data.append(product_info)
    return pd.DataFrame(products_data)


def scrape_all(base_url):
    products_page1 = scrape(base_url)
    page = 2
    while True:
        url_page = f"{base_url}?p={page}"
        all_products = scrape(url_page)
        if all_products.empty:
            break
        products_page1 = pd.concat(
            [products_page1, all_products], ignore_index=True)
        page += 1
    return products_page1


# Definimos el URL base para el Scraping
base_url = "https://coralhipermercados.com/audio-y-video.html"

# Llamamos a la funcion scrape para obtener los datos de los productos

df = scrape_all(base_url)

# Imprimimos el Df resultante
print(df)

# Guardamos los datos en un archivo CSV sin incluir el indice
df.to_csv("data/raw/products.csv", index=False)
