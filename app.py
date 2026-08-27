import streamlit as st
import tempfile
import os
import hashlib
from main import process_document, get_response

st.title("DocuMind")

uploaded_file = st.file_uploader(
    "Upload your study document",
    type=["pdf", "txt", "docx", "csv"]
)

if uploaded_file is not None:
    file_hash = hashlib.md5(uploaded_file.read()).hexdigest()
    uploaded_file.seek(0)

    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    if "vector_store" not in st.session_state or st.session_state.get("file_hash") != file_hash:
        with st.spinner("Processing document..."):
            st.session_state.vector_store = process_document([tmp_path])
            st.session_state.file_hash = file_hash
            st.session_state.messages = []
        st.success(f"{uploaded_file.name} ready. Ask me anything!")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    user_query = st.chat_input("Ask a question about your document...")

    if user_query:
        st.chat_message("user").write(user_query)
        st.session_state.messages.append({"role": "user", "content": user_query})

        with st.spinner("Thinking..."):
            answer = get_response(st.session_state.vector_store, user_query)

        st.chat_message("assistant").write(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})

else:
    st.info("Please upload a document to get started.")