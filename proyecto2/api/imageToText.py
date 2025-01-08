import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Carga el archivo .env
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    res = response.json()
    return res[0]["generated_text"]

