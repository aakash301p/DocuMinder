from langchain_chroma import Chroma
from chatmodel.embed import embeddings
from dotenv import load_dotenv
from service.splitter import Splitter

load_dotenv()

def build_vector_store(file_paths: list[str]) -> Chroma:
    chunks = Splitter.split_to_raw_chunks(file_paths)

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name="study_coach",
    )

    return vector_store

def get_relevant_context(vector_store: Chroma, query: str, k: int = 4) -> str:
    results = vector_store.similarity_search(query, k=k)
    return "\n\n".join(doc.page_content for doc in results)