from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()  # Carga el archivo .env
def textImage(message):

    client = InferenceClient("black-forest-labs/FLUX.1-dev", token=os.getenv("HUGGINGFACE_API_KEY"))  # Crea un cliente de inferencia

    image = client.text_to_image(message)
    image_path = "output.jpg"
    image.save("output.jpg")  # Guarda la imagen en un archivo .jpg
    return image_path
    
