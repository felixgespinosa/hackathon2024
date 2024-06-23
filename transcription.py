import whisper
import os
import glob

class Transcriber:
    def __init__(self):
        self.recordings_dir = 'Recordings/*' # Directorio donde se encuentran los archivos de audio
        self.transcript_file = 'transcribedText.txt' # Archivo donde se guardará la transcripción
        self.transcribed = [] # Lista para almacenar qué archivos de audio ya han sido transcritos
        self.model = whisper.load_model("base") # Modelo de transcripción de audio

    def transcribe_latest_recording(self):
        files = sorted(glob.iglob(self.recordings_dir), key=os.path.getctime, reverse=True)
        if len(files) < 1:
            return
        
        latest_recording = files[0]
        latest_recording_filename = latest_recording.split('/')[0]

        if os.path.exists(latest_recording) and not latest_recording in self.transcribed:
            audio = whisper.load_audio(latest_recording)
            audio = whisper.pad_or_trim(audio)
            mel = whisper.log_mel_spectrogram(audio).to(self.model.device)
            options = whisper.DecodingOptions(language='spanish', fp16=False)

            result = whisper.decode(self.model, mel, options)

            if result.no_speech_prob < 0.5:


                # Append text to transcript file
                with open(self.transcript_file, 'a') as f:
                    f.write(result.text)
            
                # Save list of transcribed recordings so that we don't transcribe the same one again
                self.transcribed.append(latest_recording)

if __name__ == "__main__":
    transcriber = Transcriber()
    while True:
        transcriber.transcribe_latest_recording()
