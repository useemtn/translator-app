import os
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk
from translator_app import translate

def speech_text():
    """
    
    Captura audio del micrófono, lo transcribe a texto y luego lo traduce.
    
    """
    
    # Cargar variables de entorno
    load_dotenv()
    speech_key = os.environ.get("AZURE_SPEECH_KEY")
    speech_region = os.environ.get("REGION")

    
    # Validar las variables de entorno 
    if not all([speech_key, speech_region]):
        raise ValueError("Faltan variables de entorno para Speech. Verifica tu archivo .env.")

    # Configurar el reconocimiento de voz
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
    speech_config.speech_recognition_language = "es-ES" 

    # Configurar la captura de audio
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    print("Habla al micrófono...")

    try:
        # Realizar el reconocimiento de voz
        speech_recognition_result = speech_recognizer.recognize_once_async().get()

        # Procesar el resultado, en caso de éxito lo guarda, en caso contrario imprime el error
        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            texto_transcrito = speech_recognition_result.text
            print(f"Texto reconocido: {texto_transcrito}")
            return texto_transcrito
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            print("No se pudo reconocer el habla.")
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            print(f"Reconocimiento de voz cancelado: {cancellation_details.reason}")
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print(f"   Error code: {cancellation_details.error_code}")
                print(f"   Error details: {cancellation_details.error_details}")
    except Exception as e:
        print(f"Error en el reconocimiento de voz: {e}")

    return None

def speech_to_text_and_translate():
    """
    
    Realiza el proceso completo de voz a texto y traducción.
    
    """
    # Obtener el texto transcrito del reconocimiento de voz
    texto_transcrito = speech_text()

    # Traducir el texto
    if texto_transcrito:
        print("\n--- Traduciendo el texto ---")
        translated_text, to_language = translate(text_to_translate=texto_transcrito) 

        # Imprimir el resultado
        if translated_text:
            print(f"\n--- Proceso completado ---")
            print(f"Texto original: {texto_transcrito}")
            print(f"Texto traducido ({to_language}): {translated_text}")
            return translated_text, to_language
        # mensaje de error
        else:
            print("La traducción falló.")
    else:
        print("No se pudo obtener texto del reconocimiento de voz.")


if __name__ == "__main__":
    speech_to_text_and_translate()