# 📅 Day 06 – Vector Databases & Semantic Search

## 🎯 Objective

Learn how vector databases store and retrieve embeddings efficiently. Build a semantic search engine using **Sentence Transformers** and **FAISS** to understand how Retrieval-Augmented Generation (RAG) systems retrieve relevant information.

---

# 🤖 What is a Vector Database?

A **Vector Database** stores numerical vectors (embeddings) instead of plain text.

Unlike traditional databases that search using exact keywords, vector databases search using **semantic similarity**, allowing them to retrieve information based on meaning rather than exact word matches.

Examples of Vector Databases include:

* FAISS
* ChromaDB
* Pinecone
* Milvus
* Weaviate
* Qdrant

---

# Why Do We Need Vector Databases?

Imagine storing one million document embeddings.

Without a vector database:

* Every query compares against every document.
* Search becomes slow.
* Computational cost increases significantly.

A vector database builds specialized indexes that allow similarity searches to be performed efficiently, even across millions of vectors.

---

# How Semantic Search Works

```text
User Query
      │
      ▼
Embedding Model
      │
      ▼
Query Vector
      │
      ▼
Vector Database
      │
      ▼
Nearest Embeddings
      │
      ▼
Relevant Documents
```

---

# Traditional Search vs Semantic Search

| Traditional Search   | Semantic Search                    |
| -------------------- | ---------------------------------- |
| Keyword matching     | Meaning matching                   |
| Exact words required | Similar ideas accepted             |
| Misses synonyms      | Understands semantic relationships |
| SQL databases        | Vector databases                   |

---

# What is FAISS?

**FAISS (Facebook AI Similarity Search)** is an open-source library developed by Meta for efficient similarity search over dense vectors.

It is widely used in:

* RAG systems
* AI search engines
* Chatbots
* Recommendation systems
* Document retrieval

---

# Hands-on Experiment

In this notebook, I:

* Generated embeddings using Sentence Transformers.
* Stored embeddings in a FAISS index.
* Performed semantic searches.
* Retrieved the Top-K most relevant documents based on cosine similarity.

---

# Key Learnings

* Vector databases store embeddings instead of raw text.
* FAISS enables efficient nearest-neighbor search.
* Semantic search retrieves information based on meaning.
* Vector databases are fundamental to Retrieval-Augmented Generation (RAG).

---

# What's Next?

➡️ Day 07 – Building a Retrieval-Augmented Generation (RAG) Pipeline
