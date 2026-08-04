# Agent Communication Documentation

## Overview

The Climate & Disaster Awareness Assistant uses multiple AI agents that work together to answer user queries.

The agents communicate in a sequential workflow to provide accurate disaster and climate information.

---

## Agent Workflow
User Query

|

v

Router Agent

|

v

Retrieval Agent

|

v

LLM Agent

|

v

Final Answer


---

## Router Agent

The Router Agent receives the user question and identifies the relevant category.

Examples:

- Flood questions → Disaster category
- Climate questions → Climate category
- Safety questions → Safety category

The category information is passed to the Retrieval Agent.

---

## Retrieval Agent

The Retrieval Agent searches the knowledge base using:

- ChromaDB Vector Database
- HuggingFace Embeddings
- Sentence Transformer models

It retrieves the most relevant document information.

---

## LLM Agent

The LLM Agent receives:

- User question
- Retrieved context

It generates the final response using the Groq Llama model.

---

## Agent Communication Flow

1. User submits a question through Streamlit.
2. Router Agent identifies the question type.
3. Retrieval Agent finds relevant information from documents.
4. LLM Agent generates a context-based answer.
5. Final answer is displayed to the user.