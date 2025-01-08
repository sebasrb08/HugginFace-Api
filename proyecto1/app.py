import streamlit as st
from api import apichat

def main():
    st.title("Chat Bot")

    if 'messages' not in st.session_state:
        st.session_state.messages = []
        st.session_state.userMessage = []

    new_message = st.text_input("Mensaje")

    if st.button("Enviar"):
        if new_message:
            try:
                st.session_state.userMessage.append(new_message)  
                st.session_state.messages.append(apichat(new_message))
            except:
                st.error("Error en el servidor")
            st.rerun()
            
            
    for i in range(len(st.session_state.messages)):
        with st.container(border=True):
            st.text(f"Tu:   {st.session_state.userMessage[i]}")
        with st.container(border=True):
            st.text(f"Bot:   {st.session_state.messages[i]}")
            

if __name__ == "__main__":
    main()