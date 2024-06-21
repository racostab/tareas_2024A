# convertir_a_bmp.py
import sys
import os

# Añadir el directorio principal al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# convertir_a_bmp.py
from Patrones_BMP.conversion import convertir_a_bmp

# Ejemplo de uso
archivo_exe = "./HelloWorld.exe"
nombre_imagen = "./HelloWorld.img"

convertir_a_bmp(archivo_exe, nombre_imagen)
