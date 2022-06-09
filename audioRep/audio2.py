"""
    Convertir texto a voz (TTS) con
    Python usando gTTS
    Ejemplo 2: Escribir hola mundo en un archivo abierto con open, 
    en idioma español
    @author parzibyte
"""
from gtts import gTTS
tts = gTTS('Hola mundo. Estamos convirtiendo texto a voz con Python.', lang='es-us')

with open("2_hola_mundo.mp3", "wb") as archivo:
    tts.write_to_fp(archivo)