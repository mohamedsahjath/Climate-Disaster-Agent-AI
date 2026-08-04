# RAG Pipeline Documentation

## Overview

The Climate & Disaster Awareness Assistant uses Retrieval-Augmented Generation (RAG) to provide accurate answers based on disaster and climate documents.

## RAG Process

The pipeline contains the following steps:

1. PDF Document Collection
2. Document Loading
3. Text Chunking
4. Embedding Generation
5. Vector Storage using ChromaDB
6. Similarity Search
7. Context-based Answer Generation


## Document Processing

PDF documents are loaded from the knowledge base.

The documents are divided into smaller text chunks to improve retrieval accuracy.


## Embedding Generation

Sentence Transformer models are used to convert text chunks into numerical vector representations.


## Vector Database

ChromaDB stores document embeddings and performs similarity search to find relevant information.


## Response Generation

The retrieved context is provided to the LLM Agent.

The LLM generates a final answer based on the retrieved disaster information.