from api.textToImage import textImage
from api.imageToText import query
class API:
    def response(self,message):
        image_path = textImage(message)
        if not image_path:
            return "No se pudo generar la imagen"
        
        description = query(image_path)
        if not description:
            return "No se pudo generar la descripción"
        return description