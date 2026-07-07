from langchain_core.documents import Document

from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_resume_document(
    resume_text
):

    document = Document(

        page_content=resume_text,

        metadata={

            "source": "Resume"

        }

    )

    return document


def split_document(

    document,

    chunk_size=500,

    chunk_overlap=50

):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=chunk_size,

        chunk_overlap=chunk_overlap

    )

    chunks = splitter.split_documents(

        [document]

    )

    return chunks