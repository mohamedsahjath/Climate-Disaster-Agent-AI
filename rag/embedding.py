from loader import load_documents
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


def create_embeddings():

    print("Loading documents...")
    documents = load_documents()

    print("Splitting documents...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    print("Total chunks:", len(chunks))


    print("Creating embeddings...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


    print("Saving to ChromaDB...")

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="../chroma_db"
    )

    db.persist()

    print("Embedding completed successfully!")


if __name__ == "__main__":
    create_embeddings()