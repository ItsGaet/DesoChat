import streamlit as st
import streamlit_authenticator as stauth
import yaml
import cohere
from yaml.loader import SafeLoader
from st_pages import Page, Section, show_pages, add_page_title
from pyexpat.errors import messages


with open('config/utenti.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authenticator.login()

if st.session_state["authentication_status"]:
    add_page_title()
    show_pages([
        Page("login.py", "C-AGE", "😶‍🌫️"),
        Page("story.py", "About Us", ":books:")
    ])  
    st.caption("🚀 Chabot based on Cohere and RAG 🚀")
    authenticator.logout()
    co = cohere.Client('crAvP7FvQ4yVLw7pju7nAHBy9FZmRB5uY6bxgSFB')

    preamble_override = "You are Cage, an expert IT consultant and trainer"

    deso_tech_connector = {
        "id": "web-search",
        "options": {
            "site": "deso.tech/en"
        }
    }

    # Initialize session state variables
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    connectors = [deso_tech_connector]
    
    # Process user input
    if prompt := st.chat_input("What is up?"):
        # Display user input in the chat
        with st.chat_message("user"):
            st.markdown(prompt)

        # Make request to Cohere API
        cohere_response = co.chat(
            message=prompt,
            model="command-nightly",
            preamble_override=preamble_override,
            connectors=connectors
            )

        # Display assistant's response in the chat
        with st.chat_message("assistant"):
            st.markdown(cohere_response.text)

        # Update session state with both user input and assistant's response
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "assistant", "content": cohere_response.text})
      

elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')