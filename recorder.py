import sounddevice as sd
import wavio as wv
import datetime
import os
import numpy as np

class AudioRecorder:
    def __init__(self, freq=44100, duration=3600):
        self.freq = freq
        self.duration = duration

    def record(self):
        if not os.path.exists("./recordings"):
            os.makedirs("./recordings")

        print('Presiona Enter para comenzar a grabar...')
        input()  # Espera hasta que el usuario presione Enter

        print('Grabando...')

        ts_start = datetime.datetime.now()
        filename = ts_start.strftime("%Y-%m-%d%H.%M.%S")

        # Iniciar grabación con los valores dados de duración y frecuencia de muestreo
        recording = sd.rec(int(self.duration * self.freq), samplerate=self.freq, channels=1, blocking=False)

        print('Presiona Enter para detener la grabación...')
        input()  # Espera hasta que el usuario presione Enter para detener la grabación

        ts_stop = datetime.datetime.now()
        print('Grabación detenida...')

        # Calcular la duración real de la grabación
        duration_actual = (ts_stop - ts_start).total_seconds()

        # Truncar la grabación a la duración real
        recording_truncated = recording[:int(duration_actual * self.freq)]

        # Normalizar los datos de audio
        max_amplitude = np.max(np.abs(recording_truncated))
        if max_amplitude > 1.0:
            recording_truncated /= max_amplitude

        # Convertir la matriz NumPy a archivo WAV y guardar
        wv.write(f"./recordings/{filename}.wav", recording_truncated, self.freq, sampwidth=2)

        print(f'Grabación guardada como {filename}.wav')

# Ejemplo de uso
if __name__ == "__main__":
    recorder = AudioRecorder()
    recorder.record()
