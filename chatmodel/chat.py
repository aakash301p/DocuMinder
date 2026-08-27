from langchain_mistralai.chat_models import ChatMistralAI
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

client = ChatMistralAI(
    model_name="mistral-small-2506",
    temperature=0.9,
    max_tokens=512,
    api_key =os.getenv("MISTRAL_API_KEY") or st.secrets.get("MISTRAL_API_KEY")
)
