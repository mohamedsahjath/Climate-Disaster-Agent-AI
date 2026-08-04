# System Architecture

## Climate & Disaster Awareness Assistant

The system follows an Agentic AI architecture with multiple agents and a RAG pipeline.

## Architecture Flow

User

↓

Streamlit Interface

↓

Router Agent

↓

Retrieval Agent

↓

ChromaDB Vector Database

↓

LLM Agent (Groq)

↓

Final Response


## Components

### Router Agent
Identifies the category of the user query.

### Retrieval Agent
Searches relevant information from disaster documents using vector similarity search.

### LLM Agent
Generates the final answer using retrieved context.