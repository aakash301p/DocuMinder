from langchain_core.messages import SystemMessage, HumanMessage
from chatmodel.chat import client
from service.system_prompt import prompt
from vector_store.DB import build_vector_store, get_relevant_context


def process_document(file_paths: list[str]):
    vector_store = build_vector_store(file_paths)
    return vector_store


def get_response(vector_store, user_query: str) -> str:
    context = get_relevant_context(vector_store, user_query, k=4)
    messages = [
        SystemMessage(content=prompt + "\n\n" + context),
        HumanMessage(content=user_query),
    ]
    response = client.invoke(messages)
    return response.content