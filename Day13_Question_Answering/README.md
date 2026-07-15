# 📅 Day 13 – Question Answering (QA)

## 🎯 Objective

Learn how Transformer-based Question Answering (QA) models extract answers from a given context. Build a Question Answering application using Hugging Face Transformers and understand how extractive QA works.

---

# ❓ What is Question Answering?

Question Answering (QA) is a Natural Language Processing (NLP) task where a model answers questions using information from a provided context.

Unlike text generation models that create responses, extractive QA models identify the exact span of text within the context that answers the question.

---

# Why is Question Answering Important?

Question Answering systems are widely used in:

* Search engines
* Virtual assistants
* Educational platforms
* Customer support
* Enterprise knowledge bases
* Healthcare information systems
* Legal document search

---

# QA Workflow

```text
Context Document
        │
        ▼
Tokenizer
        │
        ▼
Question Answering Model
        │
        ▼
Extract Relevant Answer
        │
        ▼
Final Response
```

---

# Types of Question Answering

## 1. Extractive Question Answering

The answer is extracted directly from the provided context.

Example:

Context:

```
Python was created by Guido van Rossum in 1991.
```

Question:

```
Who created Python?
```

Answer:

```
Guido van Rossum
```

---

## 2. Generative Question Answering

The model generates a new answer using its knowledge or retrieved context.

Example:

Question:

```
Explain why Python is popular.
```

Answer:

```
Python is popular because it is easy to learn, has a large ecosystem, and is widely used in AI, web development, and data science.
```

---

# Hands-on Experiment

In this notebook, I:

* Loaded a pre-trained Question Answering model.
* Asked questions based on a context paragraph.
* Retrieved answers with confidence scores.
* Built an interactive QA application.
* Compared multiple questions on the same context.

---

# Key Learnings

* QA models require both a question and a context.
* Extractive QA identifies answers directly from the context.
* Confidence scores indicate how certain the model is.
* QA forms the foundation for Retrieval-Augmented Generation (RAG).

---

# What's Next?

➡️ Day 14 – Retrieval-Augmented Generation (RAG)
