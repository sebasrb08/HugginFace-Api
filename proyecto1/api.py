from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()  # Carga el archivo .env
def apichat(message):
    
    client = InferenceClient(api_key=os.getenv("HUGGINGFACE_API_KEY"))

    messages = [
        {
            "role": "user",
            "content": message
        }
    ]

    completion = client.chat.completions.create(
        model="mistralai/Mistral-Nemo-Instruct-2407", 
        messages=messages, 
        max_tokens=500
    )

    return completion.choices[0].message.content



# Prueba de la función
