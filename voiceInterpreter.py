from gtts import gTTS
import os
import pygame

class TextoAVoz:
    def __init__(self, texto, idioma='es-us'):
        self.texto = texto
        self.idioma = idioma
        self.archivo_audio = "salida.mp3"

    def convertir_texto_a_audio(self):
        tts = gTTS(text=self.texto, lang=self.idioma)
        tts.save(self.archivo_audio)

    def reproducir_audio(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.archivo_audio)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

# Uso de la clase
texto = "Hola, este es Chawimi bienvenido al Hackathon del 2024"
texto_a_voz = TextoAVoz(texto)
texto_a_voz.convertir_texto_a_audio()
texto_a_voz.reproducir_audio()
