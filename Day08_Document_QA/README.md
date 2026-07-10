# 📅 Day 08 – Document Question Answering with RAG

## 🎯 Objective

Build a Document Question Answering (Document QA) system that allows users to ask natural language questions about a document. The system retrieves the most relevant document chunks using semantic search and generates context-aware answers using a Large Language Model.

---

# 🤖 What is Document Question Answering?

Document Question Answering is an AI application where users ask questions about one or more documents, and the system returns answers based only on the document content.

Instead of relying solely on the LLM's training data, the system first retrieves relevant information from the uploaded document and then uses it as context for answer generation.

---

# Why is Document QA Useful?

Document QA is widely used in:

* Research assistants
* Enterprise knowledge bases
* Customer support systems
* Legal document analysis
* Medical document search
* Educational assistants
* Company policy assistants

---

# System Workflow

```text
User Uploads Document
         │
         ▼
Extract Text
         │
         ▼
Split into Chunks
         │
         ▼
Generate Embeddings
         │
         ▼
Store in FAISS
         │
         ▼
User Question
         │
         ▼
Semantic Retrieval
         │
         ▼
Relevant Chunks
         │
         ▼
LLM
         │
         ▼
Final Answer
```

---

# Components

### 1. Document Loader

Reads PDF or text files.

### 2. Text Chunker

Splits large documents into smaller chunks.

### 3. Embedding Model

Converts chunks into numerical vectors.

### 4. Vector Database

Stores embeddings for fast similarity search.

### 5. Retriever

Finds the most relevant chunks.

### 6. Generator

Produces answers using the retrieved context.

---

# Hands-on Experiment

In this notebook, I:

* Loaded a PDF document.
* Extracted its text.
* Split the document into chunks.
* Generated embeddings using Sentence Transformers.
* Indexed embeddings using FAISS.
* Retrieved relevant chunks for user queries.
* Generated answers using a Hugging Face language model.

---

# Key Learnings

* Large documents should be chunked before embedding.
* Semantic retrieval finds relevant passages without exact keyword matches.
* Retrieved context helps LLMs generate grounded responses.
* Document QA is one of the most common real-world applications of RAG.

---

# What's Next?

➡️ Day 09 – Conversational Memory in AI Chatbots
