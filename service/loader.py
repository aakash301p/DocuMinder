import os
from typing import Dict, Type, List
from langchain_core.documents import Document

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
    CSVLoader,
    UnstructuredExcelLoader,
    UnstructuredFileLoader
)


class DocumentLoader:

    REGISTRY: Dict[str, Type] = {
        ".pdf": PyPDFLoader,
        ".txt": TextLoader,
        ".docx": Docx2txtLoader,
        ".csv": CSVLoader,
        ".xlsx": UnstructuredExcelLoader
    }

    _FALLBACK = UnstructuredFileLoader

    @classmethod
    def load_file(cls, file_path: str) -> List[Document]:

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found at path: {file_path}")
        ext = os.path.splitext(file_path)[1].lower()
        loader_class = cls.REGISTRY.get(ext, cls._FALLBACK)

        loader = loader_class(file_path)
        return loader.load()

    @classmethod
    def load_multiple_files(cls, file_paths: List[str]) -> List[Document]:

        all_documents = []
        for path in file_paths:
            try:
                docs = cls.load_file(path)
                all_documents.extend(docs)
            except Exception as e:
                print(f"{os.path.basename(path)}: {e}")
        return all_documents
