from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


def retrieve_information(query):

    print("Loading embedding model...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


    print("Loading Chroma database...")

    db = Chroma(
        persist_directory="../chroma_db",
        embedding_function=embeddings
    )


    print("Searching documents...")

    results = db.similarity_search(
        query,
        k=3
    )


    context = ""

    for doc in results:
        context += doc.page_content
        context += "\n\n"


    return context



if __name__ == "__main__":


    question = "What should people do during floods?"


    answer = retrieve_information(question)


    print("\n===== RESULT =====\n")

    print(answer)