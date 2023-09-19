import streamlit as st
import os
from information_retrieval import retrieve_info
from save_embeddings import train_and_save_embeddings

# Create the "embeddings" folder if it doesn't exist
EMBEDDINGS_FOLDER = "embeddings"
os.makedirs(EMBEDDINGS_FOLDER, exist_ok=True)


# Create a Streamlit app
st.title("CustomChat AI")

# Add tabs for Training and Chat Interface
tabs = st.sidebar.selectbox("Select a Tab", ["Training", "Chat"])

if tabs == "Training":
    st.write("This is the training tab where you can train the language model.")

    # Upload PDF files
    uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)
    
    if uploaded_files:
        st.write(f"{len(uploaded_files)} PDF files uploaded.")
        train_button = st.button("Train Model")
        
        if train_button:
            with st.spinner("training in progress..."):
                train_and_save_embeddings(uploaded_files)
            st.success("Model trained and embeddings saved successfully!")

elif tabs == "Chat":
    prompt = st.chat_input("Say something")
    if prompt:
        st.write(f"User: {prompt}")
        result = retrieve_info(EMBEDDINGS_FOLDER, prompt)
        final = result.replace("<pad>", "")
        st.write(f"Assistant:{final}")