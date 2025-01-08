from huggingface_hub import InferenceClient

def textImage(message):

    client = InferenceClient("black-forest-labs/FLUX.1-dev", token="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")

    # output is a PIL.Image object
    image = client.text_to_image(message)
    image_path = "output.jpg"
    image.save("output.jpg")  # Guarda la imagen en un archivo .jpg
    return image_path
    
