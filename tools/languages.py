def list_available_languages():
    """
    
    Lista los idiomas disponibles para voz o traducción.
    
    """
    speech_languages = {
        "en-US": "English (United States)",
        "en-GB": "English (United Kingdom)",
        "en-AU": "English (Australia)",
        "es-ES": "Español (España)",
        "es-MX": "Español (México)",
        "es-AR": "Español (Argentina)",
        "fr-FR": "Français (France)",
        "fr-CA": "Français (Canada)",
        "fr-CH": "Français (Suisse)",
        "de-DE": "Deutsch (Deutschland)",
        "de-AT": "Deutsch (Österreich)",
        "de-CH": "Deutsch (Schweiz)",
        "it-IT": "Italiano (Italia)",
        "pt-BR": "Português (Brasil)",
        "pt-PT": "Português (Portugal)",
        "zh-CN": "中文 (简体, 中国)",
        "zh-HK": "中文 (繁體, 香港特別行政區)",
        "zh-TW": "中文 (繁體, 台灣)",
        "yue-CN": "Cantonese (Simplified, China)",
        "yue-HK": "Cantonese (Traditional, Hong Kong)",
        "ja-JP": "日本語 (日本)",
        "ko-KR": "한국어 (대한민국)",
        "ru-RU": "Русский (Россия)",
        "ar-EG": "العربية (مصر)",
        "ar-SA": "العربية (المملكة العربية السعودية)",
        "ar-AE": "Arabic (United Arab Emirates)",
        "ca-ES": "Català (Espanya)",
        "cs-CZ": "Čeština (Česká republika)",
        "da-DK": "Dansk (Danmark)",
        "fi-FI": "Suomi (Suomi)",
        "el-GR": "Ελληνικά (Ελλάδα)",
        "he-IL": "עברית (ישראל)",
        "hi-IN": "हिन्दी (भारत)",
        "hu-HU": "Magyar (Magyarország)",
        "id-ID": "Bahasa Indonesia (Indonesia)",
        "ga-IE": "Gaeilge (Éire)",
        "nb-NO": "Norsk bokmål (Norge)",
        "pl-PL": "Polski (Polska)",
        "ro-RO": "Română (România)",
        "sk-SK": "Slovenčina (Slovensko)",
        "sv-SE": "Svenska (Sverige)",
        "th-TH": "ไทย (ประเทศไทย)",
        "tr-TR": "Türkçe (Türkiye)",
        "uk-UA": "Українська (Україна)",
        "vi-VN": "Tiếng Việt (Việt Nam)",
    }
    print("\nIdiomas de Voz Disponibles:")
    for code, name in speech_languages.items():
        print(f"   {code}: {name}")
    return speech_languages

def get_language_code(languages):
    """
    
    Obtiene el código de idioma del usuario.
    
    """
    while True:
        code = input("Introduce el código de idioma: ").strip()
        if code in languages:
            return code
        else:
            print("Código de idioma no válido. Inténtalo de nuevo.")