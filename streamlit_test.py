import streamlit as st
import pandas as pd
import numpy as np



# Your Streamlit content goes here

# Inject HTML and JavaScript for Dialogflow Messenger
dialogflow_code = """
    <style>
        .chatbot-container {
            display: flex;
            flex-direction: column-reverse;
            align-items: flex-end;
            position: absolute;
            z-index: 999;
            bottom: 0;
            right: 0;
            padding: 10px;
        }
    </style>
    <div class="chatbot-container">
        <link rel="stylesheet" href="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/themes/df-messenger-default.css">
        <script src="https://www.gstatic.com/dialogflow-console/fast/df-messenger/prod/v1/df-messenger.js"></script>
        <df-messenger
            location="us-central1"
            project-id="gred-ptddtalak-sb-001-e4372d8c"
            agent-id="94d1a3fb-2068-439e-8a1c-293afb924030"
            language-code="en"
            max-query-length="-1">
            <df-messenger-chat-bubble chat-title="cqa2-test"></df-messenger-chat-bubble>
        </df-messenger>
    </div>
"""

st.title("Vertex AI chatbot demo")

# Display Dialogflow Messenger in the second column

# Create Streamlit columns
col1, col2 = st.columns([1, 1])
with col1:
    uploaded_files = st.file_uploader("Choose a PDF file", accept_multiple_files=True)
with col2:
    st.components.v1.html(dialogflow_code, height=650)

for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)