
"""
    Convertir texto a voz (TTS) con
    Python usando gTTS
    Ejemplo 1: Escribir hola mundo en un archivo, en idioma español
    @author parzibyte
"""
from gtts import gTTS
tts = gTTS('Persona Desconocida.', lang='es-us')
tts.save("Desconocido.mp3")
