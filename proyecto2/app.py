import streamlit as st
from model import API

def getResponse(texto):
    api = API() 
    try:
        description = api.response(texto)
        
        st.subheader("Imagen Generada")
        st.image("output.jpg",width=300)
        
        st.subheader("Descripción de la imagen generada")
        st.write(description)

    except Exception as e:
        st.error(f"Error al crear la imagen y la descripcion: {e}")

def main():
    
    st.title("Multiples Modelos")
    texto = st.text_input("Ingrese el texto que desea convertir en imagen")
    if st.button("Crear Imagen y descripción" ):
        getResponse(texto)
            

if __name__ == "__main__":
    main()