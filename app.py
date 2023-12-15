import streamlit as st
from streamlit_option_menu import option_menu
from src.pages.chatbot import chatbot
from src.pages.term_page import term

def main():
    with st.sidebar:
            selected = option_menu(
                menu_title="Menu",
                options=[ "Konsultasi", "Petunjuk Penggunaan"],
                icons=["robot", "list-task"],
                menu_icon="cast",
                default_index=0
            )
        
    
    if selected == "Konsultasi":
        chatbot()

    elif selected == "Petunjuk Penggunaan":
        term()


if __name__ == "__main__":
    main()