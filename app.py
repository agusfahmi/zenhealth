import streamlit as st
from streamlit_option_menu import option_menu
from src.pages.chatbot import chatbot
from src.pages.map import find_hospitals_nearby

def main():
    with st.sidebar:
            selected = option_menu(
                menu_title="Menu",
                options=[ "Konsultasi", "Map"],
                icons=["robot", "geo-alt"],
                menu_icon="cast",
                default_index=0
            )
    
    if selected == "Konsultasi":
        chatbot()

    elif selected == "Map":
        find_hospitals_nearby()


if __name__ == "__main__":
    main()