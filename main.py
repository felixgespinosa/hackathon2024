from recorder import AudioRecorder
from transcription import Transcriber
from first_API_request import GPT3Chatbot
from voice_interpretation import TextoAVoz
def main():
    # Crear una instancia de AudioRecorder
    recorder = AudioRecorder()
    # Llamar al método para grabar audio
    recorder.record()
    api_request=GPT3Chatbot(api_key='')
    # Crear una instancia de Transcriber
    transcriber = Transcriber()
    transcriber.transcribe_latest_recording()
    # Llamar al método para transcribir el último archivo de audio
    with open("./transcribedText.txt", 'r') as file:
        file_content = file.read()
    response = api_request.start_chat(initial_prompt=file_content)    

    voice = TextoAVoz(response)
    voice.convertir_texto_a_audio()
    voice.reproducir_audio()

    with open("./transcribedText.txt", 'w') as file:
        file.write('')

if __name__ == "__main__":
    main()

