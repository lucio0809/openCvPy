
"""
    Convertir texto a voz (TTS) con
    Python usando gTTS
    Ejemplo 4: Escribir hola mundo en un archivo, en idioma español
    y después reproducirlo
    @author parzibyte
"""
from ReconocimientoFacial import imagePaths
from gtts import gTTS
from playsound import playsound
NOMBRE_ARCHIVO = "sonido_generado.mp3"
tts = gTTS('Hola mundo. Estamos convirtiendo texto a voz con Python.', lang='es-us')
# Nota: podríamos llamar directamente a save
with open(NOMBRE_ARCHIVO, "wb") as archivo:
    tts.write_to_fp(archivo)

playsound(NOMBRE_ARCHIVO)