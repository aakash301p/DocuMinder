from langchain_mistralai.chat_models import ChatMistralAI
from langchain_community.document_loaders import PyPDFLoader

from langchain_core.messages import SystemMessage, HumanMessage
import os
from service.system_prompt import prompt
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

doc = PyPDFLoader("document/DA_GATE2027_Syllabus.pdf")

client = ChatMistralAI(model='mistral-small-2506',temperature=0.9,max_tokens=512)

