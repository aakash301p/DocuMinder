from langchain_text_splitters import RecursiveCharacterTextSplitter

from service.loader import DocumentLoader


class Splitter:

    _CHUNK_SIZE = 2000
    _CHUNK_OVERLAP = 200

    @classmethod
    def get_splitter(cls) -> RecursiveCharacterTextSplitter:
        return RecursiveCharacterTextSplitter(
            chunk_size=cls._CHUNK_SIZE,
            chunk_overlap=cls._CHUNK_OVERLAP
        )

    @classmethod
    def normalize_to_list(cls, files) -> list:

        if isinstance(files, str):
            return [files]
        return files

    @classmethod
    def split_context(cls, files) -> str:

        clean_file_list = cls.normalize_to_list(files)

        loaded_notes = DocumentLoader.load_multiple_files(clean_file_list)

        splitter = cls.get_splitter()
        chunks = splitter.split_documents(loaded_notes)

        context = "\n\n".join(chunk.page_content for chunk in chunks)
        return context

    @classmethod
    def split_to_raw_chunks(cls, files) -> list:

        clean_file_list = cls.normalize_to_list(files)
        loaded_notes = DocumentLoader.load_multiple_files(clean_file_list)
        splitter = cls.get_splitter()

        return splitter.split_documents(loaded_notes)
