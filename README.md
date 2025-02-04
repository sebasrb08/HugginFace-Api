# Modelo en local


![image](https://github.com/user-attachments/assets/a3cdc3bd-c259-4446-8829-805703adde16)

![image](https://github.com/user-attachments/assets/98590a7f-e8fc-4a2d-af26-0e5607b505ab)

![image](https://github.com/user-attachments/assets/cca201bb-e3fa-4b7a-866e-a7ee53f36650)




# Proyecto 1

Este proyecto consiste en crear una aplicación donde el usuario pueda interactuar con un modelo de lenguaje de gran escala (LLM) a través de una API de Hugging Face. El usuario podrá realizar preguntas, y el modelo proporcionará respuestas detalladas y coherentes en tiempo real.



## Requisitos

Antes de ejecutar la aplicación, asegúrate de tener instalado Python y un entorno virtual configurado. Esta guía te ayudará a instalar y configurar todo lo necesario.

## Instalación

1. **Clona este repositorio** o descarga los archivos.

 
```
git clone https://github.com/sebasrb08/HugginFace-Api.git

cd proyecto1
```

Crea un entorno virtual (opcional pero recomendado)  


2. **Crea un entorno virtual**

  

```
python -m venv venv

venv\Scripts\activate
 ```
  
  

3. **Instalacion de dependencias**

```bash
pip install streamlit python-dotenv hugging
```

4. **Crea un archivo .env**

  

Crea un archivo llamado .env en la raíz de tu proyecto. Este archivo contendrá la API_KEY de huggin face . Configura el archivo .env con tus valores personalizados como se muestra a continuación:

  
```
HUGGINGFACE_API_KEY`= TU_API_KEY
```
  
  

5. **Inicia la aplicación de Streamlit:**

```
streamlit run src/app.py

```

## Modelo

**Modelo usado:** mistralai/Mistral-Nemo-Instruct-2407 

## Ejemplo de uso:

![Captura de pantalla 2025-01-08 155445](https://github.com/user-attachments/assets/fb08152b-b4ba-401e-a5c0-7fbfce3ffb83)


# Proyecto 2

Este proyecto implementa múltiples modelos de lenguaje (LLM) mediante la API de Hugging Face. La aplicación está diseñada para permitir la iteración entre diferentes modelos a través de una clase dedicada.


## Requisitos

Antes de ejecutar la aplicación, asegúrate de tener instalado Python y un entorno virtual configurado. Esta guía te ayudará a instalar y configurar todo lo necesario.

## Instalación

1. **Navega hacia la carpeta del proyecto**

 
```
cd proyecto2
```

Crea un entorno virtual (opcional pero recomendado)  


2. **Crea un entorno virtual**

  

```
python -m venv venv

venv\Scripts\activate
 ```
  
  

3. **Instalacion de dependencias**

```bash
pip install streamlit python-dotenv hugging pillow
```

4. **Crea un archivo .env**

  

Crea un archivo llamado .env en la raíz de tu proyecto. Este archivo contendrá la API_KEY de huggin face . Configura el archivo .env con tus valores personalizados como se muestra a continuación:

  
```
HUGGINGFACE_API_KEY`= TU_API_KEY
```
  
  

5. **Inicia la aplicación de Streamlit:**

```
streamlit run src/app.py
```

## Modelo

**black-forest-labs/FLUX.1-dev**: Para generar la imagen
**Salesforce/blip-image-captioning-large**: Para describir la imagen generada

## Diagrama
![model](https://github.com/user-attachments/assets/4d935bab-e6c3-4f5a-98d3-b46d411f97f5)

## Ejemplo de uso
![image](https://github.com/user-attachments/assets/3811ce5e-1501-4269-8362-5085dae9928f)

