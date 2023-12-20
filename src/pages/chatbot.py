import google.generativeai as palm
import streamlit as st

def chatbot():
    palm.configure(api_key='AIzaSyAJpaLmBLtTB4AwEAG4-WlcikCvbHAWUIs')
    model = "models/gemini-pro"   
    st.header('Chatbot Kesehatan')
    def clear_chat_history():
        st.session_state.messages = [{"role": "doctor", "content": "Ada yang bisa AI Bantu?"}]
    st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "doctor", "content": "Ada yang bisa AI Bantu?"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input("Kirim pesan"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("doctor"):
            with st.spinner("Thinking..."):
                message_placeholder = st.empty()
                response = palm.chat(
                        context='You are an AI-based Doctor Assistant, you will not respond to queries other than this strictly,you will not respond to words that are not relevant to health',
                        messages=prompt
                        )
                full_response = response.last
                message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "doctor", "content": full_response})