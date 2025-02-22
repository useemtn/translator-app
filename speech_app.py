import os
from dotenv import load_dotenv
from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer, ResultReason, CancellationDetails, CancellationReason
import azure.cognitiveservices.speech as speech_sdk
from translator_app import translate

# Definir voces compatibles con los idiomas disponibles
voice_mapping = {
  "en-US": "en-US-GuyNeural",
  "en-GB": "en-GB-RyanNeural",
  "es-ES": "es-ES-AlvaroNeural",
  "es-MX": "es-MX-JorgeNeural",
  "fr-FR": "fr-FR-HenriNeural",
  "de-DE": "de-DE-KlausNeural",
  "it-IT": "it-IT-DiegoNeural",
  "pt-BR": "pt-BR-AntonioNeural",
  "zh-CN": "zh-CN-YunxiNeural",
  "ja-JP": "ja-JP-KeitaNeural",
  "ko-KR": "ko-KR-SunHiNeural",
  "ru-RU": "ru-RU-DmitryNeural",
}

def synthesize_speech(translated_text=None, to_language=None):
  """
  
  Convierte la traducción en voz usando Azure Speech.
  
  """
  
  # Cargar variables de entorno
  load_dotenv()
  key = os.getenv("AZURE_SPEECH_KEY")
  region = os.getenv("REGION")

  # Validar las variables de entorno
  if not all([key, region]):
    raise ValueError("⚠️ Faltan variables de entorno. Verifica tu archivo .env.")

  try:
    # Si translated_text y to_language no se proporcionan, llama a translate() como antes.
    if translated_text is None or to_language is None:
      translation_result, to_language = translate()
      if not translation_result:
        print("La traducción falló, no se puede sintetizar el habla.")
        return None
    else:
      translation_result = translated_text 

    # Seleccionar la voz basada en el idioma traducido
    voice_name = voice_mapping.get(to_language, "en-GB-RyanNeural") 

    # Configurar la síntesis de voz
    speech_config = SpeechConfig(subscription=key, region=region)
    speech_config.speech_synthesis_voice_name = voice_name
    speech_synthesizer = SpeechSynthesizer(speech_config=speech_config)

    # Sintetizar la salida hablada
    speak = speech_synthesizer.speak_text_async(translation_result).get()

    # Verificar el resultado
    if speak.reason == ResultReason.SynthesizingAudioCompleted:
      print(f"Síntesis de voz completada en {to_language}.")
      return translation_result
    # si la sintesis de voz falla muestra error 
    elif speak.reason == ResultReason.Canceled:
      cancellation_details = CancellationDetails.from_result(speak)
      print(f"Error en la síntesis de voz: {cancellation_details.reason}")
      if cancellation_details.reason == CancellationReason.Error:
        print(f"Código de error: {cancellation_details.error_code}")
        print(f"Detalles del error: {cancellation_details.error_details}")

  except Exception as e:
    print(f"❌ Error en la síntesis de voz: {e}")

  return None 

if __name__ == "__main__":
  synthesize_speech()