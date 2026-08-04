# Climate & Disaster Awareness Assistant

## Project Description

An Agentic AI assistant that provides climate change and disaster awareness information using Retrieval-Augmented Generation (RAG).

The system helps users understand:

- Flood safety
- Cyclone preparedness
- Drought awareness
- Landslide safety
- Climate change information

This project uses Sri Lanka-specific disaster and environmental documents as a knowledge base to provide accurate and context-based answers.

---

## System Architecture
User
|
v
Streamlit Interface
|
v
Router Agent
|
v
Retrieval Agent
|
v
ChromaDB Vector Database
|
v
Retrieved Context
|
v
LLM Agent (Groq)
|
v
Final Answer



---

## Agent Components

### 1. Router Agent

The Router Agent identifies the category of the user's question.

Examples:

- Flood-related question → Disaster category
- Climate-related question → Climate category
- Safety guideline question → Safety category

---

### 2. Retrieval Agent

The Retrieval Agent searches the disaster knowledge base and retrieves relevant information using vector similarity search.

Technologies used:

- ChromaDB
- HuggingFace Embeddings
- Sentence Transformers

---

### 3. LLM Agent

The LLM Agent generates the final answer using the retrieved context.

Model:

- Llama 3.3 70B (Groq)

---

# Agent Communication Flow
User Query

|
v

Router Agent

|
| Sends question category

v

Retrieval Agent

|
| Sends retrieved document context

v

LLM Agent

|
v

Final Response


The agents communicate by passing structured information between each stage.

---

# RAG Pipeline

The Retrieval-Augmented Generation pipeline contains the following steps:


PDF Documents

  |

  v

Document Loader

  |

  v

Text Chunking

  |

  v

Sentence Transformer Embeddings

  |

  v

ChromaDB Vector Database

  |

  v

Similarity Search

  |

  v
  LLM Response Generation

  
---

# Dataset

The knowledge base contains climate and disaster-related PDF documents.

Document topics include:

- Flood management
- Cyclone preparedness
- Drought awareness
- Climate change impacts
- Disaster safety guidelines

Sources include:

- Disaster management documents
- Environmental reports
- Climate awareness publications

---

# Technologies Used

- Python
- Streamlit
- LangChain
- ChromaDB
- Groq API
- HuggingFace Embeddings
- Sentence Transformers

---

# Model Selection Strategy

| Task | Model | Reason |
|---|---|---|
| Question Classification | Lightweight LLM model | Low latency and efficient routing |
| Final Answer Generation | Llama 3.3 70B (Groq) | Better reasoning ability and high-quality responses |

---

# Retrieval Evaluation

| Query | Retrieved Context Quality |
|---|---|
| What should people do during floods? | Relevant flood safety information retrieved |
| How to prepare for cyclones? | Relevant cyclone guidelines retrieved |
| Causes of drought | Relevant climate information retrieved |
| Landslide safety steps | Relevant disaster safety information retrieved |
| Climate change impacts | Relevant environmental information retrieved |

---

# Live Demo

Streamlit Cloud URL:
https://climate-disaster-agent-aigit-zzszqnmgnrn5m3xbkej7lj.streamlit.app/

##github URL: 
https://github.com/mohamedsahjath/Climate-Disaster-Agent-AI.git

---

# Limitations

- The assistant depends on available documents in the knowledge base.
- It does not provide real-time emergency alerts.
- Response quality depends on the quality of retrieved documents.

---

# Future Improvements

- Add real-time weather and disaster alerts.
- Support multiple languages including Sinhala and Tamil.
- Improve retrieval accuracy with larger datasets.
- Add more Sri Lanka-specific disaster information.