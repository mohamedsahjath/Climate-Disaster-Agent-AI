\# Climate \& Disaster Awareness Assistant



\## Project Description



An Agentic AI assistant that provides climate change and disaster awareness information using Retrieval-Augmented Generation (RAG).



The system helps users understand:

\- Flood safety

\- Cyclone preparedness

\- Drought awareness

\- Climate change information





\## Architecture



User

↓

Router Agent

↓

Retrieval Agent

↓

ChromaDB Vector Database

↓

LLM Agent (Groq)

↓

Final Answer





\## Agents



\### Router Agent

Classifies user questions into disaster-related categories.



\### Retrieval Agent

Searches relevant information from the disaster knowledge base using ChromaDB.



\### LLM Agent

Generates final answers using retrieved context.





\## RAG Pipeline



Documents (PDF)

↓

PDF Loader

↓

Text Chunking

↓

Sentence Transformer Embeddings

↓

ChromaDB

↓

Similarity Search





\## Technologies Used



\- Python

\- Streamlit

\- LangChain

\- ChromaDB

\- Groq API

\- HuggingFace Embeddings





\## Live Demo



(Add Streamlit Cloud URL here)





\## Limitations



\- Answers depend on available documents.

\- Real-time weather alerts are not included.

