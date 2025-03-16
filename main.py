import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit import divider
from langchain_anthropic import ChatAnthropic


# Set page configuration
st.set_page_config(
    page_title="DataWhisperer",
    page_icon="🧐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header
st.title(":rainbow[**DataWhisperer**]")

# Initialize chat history
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your DataWhisperer. Upload a CSV file on the sidebar, and I'll help you analyze it."}
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)


if 'df' not in st.session_state:
    st.session_state.df = {}


# Sidebar
with st.sidebar:

    st.title("📄 Data Source")
    path = st.file_uploader("Upload a CSV file to explore.", type=["csv"], accept_multiple_files=True)

    if path is not None:
        try:
            for i in range(len(path)):
                print(i)
                df = pd.read_csv(path[i])
                st.session_state.df.update({path[i].name: df})
                st.success(f"Successfully loaded {path[i].name}")
        except Exception as e:
            st.error(f"Error loading file: {e}")

    if st.session_state.df is not None:
        st.markdown("---")
        st.subheader("📊 Dataset Information")
        for key in st.session_state.df.keys():
            st.write(f"**Name:** {key}")
            st.write(f"**Size:** {st.session_state.df[key].shape[0]} rows, {st.session_state.df[key].shape[1]} columns")
            st.write("**Column Types:**")
            for col, dtype in st.session_state.df[key].dtypes.items():
                st.write(f"- {col}: {dtype}")

    # st.rerun()