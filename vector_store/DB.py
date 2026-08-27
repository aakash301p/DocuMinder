from langchain_chroma import Chroma
from chatmodel.embed import embeddings
from dotenv import load_dotenv
from service.splitter import Splitter

load_dotenv()

PERSIST_DIR = "/home/tx1026/PycharmProjects/AI-Study-Coach/vector_store/chroma_langchain_db/"

def build_vector_store(file_paths: list[str]) -> Chroma:
    chunks = Splitter.split_to_raw_chunks(file_paths)

    vector_store = Chroma(
        collection_name="study_coach",
        embedding_function=embeddings,
        persist_directory=PERSIST_DIR,
    )

    vector_store.reset_collection()
    vector_store.add_documents(chunks)

    return vector_store

def get_relevant_context(vector_store: Chroma, query: str, k: int = 4) -> str:
    results = vector_store.similarity_search(query, k=k)
    return "\n\n".join(doc.page_content for doc in results)