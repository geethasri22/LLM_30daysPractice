# Day 05 – Embeddings & Vector Representations

## 🎯 Objective

Learn how Large Language Models convert text into numerical vectors called **embeddings**. Explore how embeddings capture semantic meaning and how they are used for similarity search, Retrieval-Augmented Generation (RAG), recommendation systems, and AI-powered search engines.

---

# 🤖 What are Embeddings?

Embeddings are **dense numerical vector representations** of text that capture its semantic meaning.

Unlike one-hot encoding or simple word indexes, embeddings place similar words or sentences close together in a high-dimensional vector space.

For example:

* "Dog" and "Puppy" have similar embeddings.
* "Car" and "Vehicle" are close together.
* "Dog" and "Laptop" are far apart.

This allows AI systems to understand meaning rather than relying only on exact keyword matches.

---

# Why are Embeddings Important?

Embeddings power many modern AI applications, including:

* Semantic Search
* Retrieval-Augmented Generation (RAG)
* Chatbots
* Recommendation Systems
* Document Search
* Question Answering
* Duplicate Detection
* Clustering and Classification

---

# How Embeddings Work

```text
Text
   │
   ▼
Embedding Model
   │
   ▼
Vector Representation
   │
   ▼
Similarity Search / AI Task
```

Each sentence is converted into a list of numbers (a vector). These vectors can then be compared using similarity measures such as cosine similarity.

---

# Semantic Similarity

Embeddings help determine how similar two pieces of text are.

### Example

Sentence A:

```text
Artificial Intelligence is transforming healthcare.
```

Sentence B:

```text
AI is changing the medical industry.
```

Although the wording is different, their embeddings are close because they express similar ideas.

---

# Cosine Similarity

Cosine Similarity measures the angle between two vectors.

* **1.0** → Identical meaning
* **0.0** → Unrelated
* **-1.0** → Opposite direction (rare in text embeddings)

A higher cosine similarity indicates greater semantic similarity.

---

# Hands-on Experiment

In this notebook, I:

* Generated sentence embeddings
* Compared similar and unrelated sentences
* Calculated cosine similarity
* Visualized how embeddings capture semantic meaning

---

# Key Learnings

* Embeddings represent semantic meaning as numerical vectors.
* Similar text produces similar vectors.
* Cosine similarity measures semantic closeness.
* Embeddings are essential for RAG, vector databases, and semantic search.


What I Learned

Embeddings capture semantic meaning instead of exact words.
Cosine similarity helps compare the meaning of text.
Semantic search retrieves relevant documents even when they don't contain the exact query words.
Embeddings are the backbone of Retrieval-Augmented Generation (RAG), recommendation systems, and modern AI search applications.

---

# What's Next?

➡️ Day 06 – Vector Databases & Semantic Search
