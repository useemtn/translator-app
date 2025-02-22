from translator_app import translate
from speech_to_text import speech_to_text_and_translate
from speech_app import synthesize_speech

def main_menu():
    """
    
    Función que presenta el menú principal y gestiona las opciones del usuario.
    
    """
    while True:
        print("\n--- Menú Principal ---")
        print("1. Traducir texto a texto")
        print("2. Traducir voz a texto")
        print("3. Salir")

        option = input("Selecciona una opción (1-3): ")

        if option == '1':
            # Opción 1: Traducción de texto a texto
            print("\n--- Traducción de texto a texto ---")
            # Llama a la función translate de translator_app.py
            translated_text, to_language = translate() 
            # Verifica si la traducción fue exitosa
            if translated_text: 
                synthesize_option = input("\n¿Quieres escuchar la traducción en voz? (s/n): ").lower()
                if synthesize_option == 's':
                    synthesize_speech(translated_text=translated_text, to_language=to_language) # Llama a synthesize_speech con el texto traducido

        elif option == '2':
            # Opción 2: Traducción de voz a texto
            print("\n--- Traducción de voz a texto ---")
            # Llama a speech_text y guarda el resultado
            result = speech_to_text_and_translate() 
            # Verifica si el resultado es una tupla de 2 elementos
            if isinstance(result, tuple) and len(result) == 2:
                translated_text, to_language = result
            else:
                translated_text, to_language = None, None 
                # mensaje de error en caso contrario
                print("Error al obtener traducción de voz.")
            # Verifica si la traducción fue exitosa     
            if translated_text: 
                synthesize_option = input("\n¿Quieres escuchar la traducción en voz? (s/n): ").lower()
                if synthesize_option == 's':
                    # Llama a synthesize_speech con el texto traducido
                    synthesize_speech(translated_text=translated_text, to_language=to_language) 
        # Sale del programa
        elif option == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main_menu()