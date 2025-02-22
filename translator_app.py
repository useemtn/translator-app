import os
from dotenv import load_dotenv
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
from tools.languages import list_available_languages

def translate(text_to_translate=None):
    """
    
    Traduce un texto utilizando Azure Translator, con lista de idiomas local.
    
    """
    
    # Cargar variables de entorno
    load_dotenv()
    key = os.environ.get("AZURE_TRANSLATOR_KEY")
    endpoint = os.environ.get("ENDPOINT")
    region = os.environ.get("REGION")
    
    # Validar las variables de entorno
    credential = TranslatorCredential(key, region)
    text_translator = TextTranslationClient(endpoint=endpoint, credential=credential)

    try:
        # Obtener la lista de idiomas disponibles desde tools.languages
        languages = list_available_languages()
        print("\nIdiomas soportados para traducción: ")
        # Mostrar idiomas desde la lista local
        for code, language_name in languages.items(): 
            print(f"  {code}: {language_name}")

        # Seleccionar idioma de origen
        from_language = input("\nIntroduce el código del idioma de origen: ").strip()
        
        # Validar contra la lista local
        while from_language not in languages: 
            print("Código no válido. Inténtalo de nuevo.")
            from_language = input("Introduce el código del idioma de origen: ").strip()

        # Seleccionar idioma de destino
        to_language = input("Introduce el código del idioma de destino: ").strip()
        while to_language not in languages:
            print("Código no válido. Inténtalo de nuevo.")
            to_language = input("Introduce el código del idioma de destino: ").strip()

        # Introducir el texto a traducir
        prompt = text_to_translate
        if prompt is None:
            prompt = input("\nIntroduce el texto a traducir: ").strip()
            if not prompt:
                print("No se ingresó texto para traducir.")
                return None, None

        # Realizar la traducción
        input_text_elements = [InputTextItem(text=prompt)]
        response = text_translator.translate(
            content=input_text_elements,
            to=[to_language],
            from_parameter=from_language
        )

        # Coge solo el resultado
        translation_result = response[0]

        # Imprimir el resultado
        if translation_result.translations:
            translated_text = translation_result.translations[0].text
            print(f"\nTraducción ({to_language}): {translated_text}")
            return translated_text, to_language

    # Capturar cualquier excepción
    except Exception as exception:
        print(f"Error en la traducción: {exception}")

    return None, None

if __name__ == "__main__":
    translate()