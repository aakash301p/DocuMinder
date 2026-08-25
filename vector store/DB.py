from langchain_chroma import Chroma
from chatmodel.embed import embeddings
from dotenv import load_dotenv
from service.splitter import Splitter
from service.loader import DocumentLoader

notes = DocumentLoader.load_file(file_path)
load_dotenv()
chunks = Splitter().split_context(files)

vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",
)

