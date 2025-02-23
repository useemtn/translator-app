# Proyecto con Azure y Python

Este proyecto usa Azure AI Cognitive Services junto a Python.

## Próposito del proyecto

Aplicación que conecta con los servicios de Azure para realizar traducciones de texto mediante Inteligencia Artificial, utiliza también el servicio speech que permite pasar este texto a voz.
- tools.languages: lista de idiomas disponibles.
- requirements: dependencias a instalar.
- speech_app: lee la traducción usando una de las voces permitidas.
- speech_to_text: reconoce un texto mediante la voz del usuario, es decir, convierte voz a texto.
- translator_app: traduce los textos de un idioma de origen a uno de destino.
- main: menú de selección para usar todas las funcionalidades previamente creadas.
## Tecnologías

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>
<img src="https://www.vectorlogo.zone/logos/microsoft_azure/microsoft_azure-icon.svg" alt="azure" width="40" height="40"/>

## 🚀 Configuración y ejecución

### 1️⃣ Clonar el repositorio
```sh
git clone https://github.com/useemtn/translator-app.git
```
### 2️⃣ Moverse a la carpeta
```sh
cd translator-app
```
### 3️⃣ Crear entorno virtual
```sh
python -m venv venv
```
### 4️⃣ Activar el entorno virtual
```sh
.\venv\Scripts\activate
```
### 5️⃣ Instalar dependencias
```sh
pip install -r requirements.txt
```
### 6️⃣ Ejecutar programa
```sh
python main.py
```

## 📌 Notas
Asegúrate de tener claves de Azure Translator y Azure Speech.