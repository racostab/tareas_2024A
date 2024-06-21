# conversion.py
import numpy as np
from PIL import Image


def convertir_a_bmp(archivo_exe, nombre_imagen):
    """
    Convierte un archivo ejecutable a una imagen BMP.

    Args:
        archivo_exe: Ruta al archivo ejecutable.
        nombre_imagen: Nombre de la imagen BMP a crear.
    """
    with open(archivo_exe, "rb") as f:
        bytes_exe = f.read()

    # Calcular el tamaño de la imagen
    long = len(bytes_exe)
    width = int(long ** 0.5)
    height = (long + width - 1) // width  # Para asegurar que cubra todo el archivo

    # Convertir bytes a matriz de valores RGB
    imagen = []
    for i in range(height):
        fila = []
        for j in range(width):
            index = i * width + j
            if index + 2 < long:
                byte_rojo = bytes_exe[index]
                byte_verde = bytes_exe[index + 1]
                byte_azul = bytes_exe[index + 2]
                fila.append((byte_rojo, byte_verde, byte_azul))
            else:
                fila.append((0, 0, 0))  # Rellenar con negro si no hay suficiente data
        imagen.append(fila)

    # Convertir a array de numpy y guardar como imagen BMP
    img = np.array(imagen, dtype=np.uint8)
    imagen_bmp = Image.fromarray(img, "RGB")
    imagen_bmp.save(f"{nombre_imagen}.bmp")
