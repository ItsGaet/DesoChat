import streamlit as st
import cohere
from st_pages import Page, Section, show_pages, add_page_title

show_pages([

        Section("RAG Chatbot", icon="🎈️"),
            Page("EGA.py", "C-AGE", "😶‍🌫️"),
            Page("story.py", "About Us", ":books:"),
    ]
)

add_page_title()
st.caption("🚀 Chabot based on Cohere and RAG 🚀")

# Fetch Cohere API key from Streamlit secrets
co = cohere.Client('crAvP7FvQ4yVLw7pju7nAHBy9FZmRB5uY6bxgSFB')

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Process user input
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user input in the chat
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Make request to Cohere API
    cohere_response = co.generate(
        prompt=prompt
    )

    # Display assistant's response in the chat
    with st.chat_message("assistant"):
        st.markdown(cohere_response)

    # Update session state with assistant's response
    st.session_state.messages.append({"role": "assistant", "content": cohere_response})

