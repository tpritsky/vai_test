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
            <df-messenger-chat-bubble chat-title="cqa-test"></df-messenger-chat-bubble>
        </df-messenger>
    </div>
"""

st.title("Streamlit App")

# Create Streamlit columns
col1, col2 = st.columns([1, 1])

# Display Dialogflow Messenger in the second column
with col2:
    st.components.v1.html(dialogflow_code, height=650)
