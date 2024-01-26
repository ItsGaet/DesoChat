import streamlit as st
import cohere

st.title("Deso Chatbot") 
st.link_button(":fire: Desotech", "https://deso.tech")
st.link_button(":cloud: Linkedin", "https://www.linkedin.com/company/desotech/mycompany/")

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
    cohere_response = co.embed(
        texts=[prompt],
        model='embed-multilingual-v3.0',
        input_type='search_query',
        truncate='END'
    )

    # Display assistant's response in the chat
    with st.chat_message("assistant"):
        st.markdown(cohere_response)

    # Update session state with assistant's response
    st.session_state.messages.append({"role": "assistant", "content": cohere_response})


