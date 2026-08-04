import streamlit as st
import sys
import os

# Connect agents folder
sys.path.append("agents")

from retrieval_agent import retrieve_information
from router_agent import route_question
from llm_agent import generate_answer


# Page configuration
st.set_page_config(
    page_title="Climate Disaster AI Assistant",
    page_icon="🌍"
)


# Title
st.title("🌍 Climate & Disaster Awareness Assistant")


st.write(
    "Ask questions about climate change, floods, "
    "cyclones, droughts and safety guidelines."
)


# User input
question = st.text_input(
    "Enter your question:"
)


if question:

    # Step 1: Router Agent
    category = route_question(question)

    st.info(f"Agent Category: {category}")


    # Step 2: Retrieval Agent + ChromaDB
    context = retrieve_information(question)


    # Step 3: LLM Agent + Groq
    answer = generate_answer(
        question,
        context
    )


    # Display AI answer
    st.subheader("🤖 AI Answer")

    st.write(answer)



    # Display source information
    st.subheader("📄 Source Information")

    with st.expander("View Retrieved Documents"):

        st.write(context)