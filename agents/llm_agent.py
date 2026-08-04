import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_answer(question, context):

    prompt = ChatPromptTemplate.from_template(
        """
You are a Climate and Disaster Awareness Assistant.

Answer the user question using only the provided information.

Context:
{context}

Question:
{question}

Give a clear and helpful answer.
"""
    )


    chain = prompt | llm


    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )


    return response.content



if __name__ == "__main__":

    answer = generate_answer(
        "What should people do during floods?",
        "Move to higher ground. Avoid flood water."
    )

    print(answer)