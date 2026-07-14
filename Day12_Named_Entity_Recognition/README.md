# 📅 Day 12 – Named Entity Recognition (NER)

## 🎯 Objective

Learn how Transformer-based models identify and classify important entities such as people, organizations, locations, dates, and monetary values within text. Build a Named Entity Recognition (NER) application using Hugging Face Transformers and explore its real-world applications.

---

# 🏷️ What is Named Entity Recognition (NER)?

Named Entity Recognition (NER) is a Natural Language Processing (NLP) task that identifies and classifies meaningful entities in text.

Instead of simply reading words, NER recognizes that certain words refer to specific real-world objects such as:

* 👤 Person
* 🏢 Organization
* 🌍 Location
* 📅 Date
* 💰 Money
* 📈 Percentage
* ⏰ Time
* 🧪 Miscellaneous Entities

---

# Why is NER Important?

NER is used in many AI applications, including:

* Search engines
* Resume parsing
* Medical record analysis
* News article processing
* Legal document analysis
* Customer support automation
* Knowledge graph creation
* Information extraction

---

# NER Workflow

```text
Input Sentence
      │
      ▼
Tokenizer
      │
      ▼
Transformer Model
      │
      ▼
Entity Detection
      │
      ▼
Person | Organization | Location | Date | Money
```

---

# Common Entity Types

| Entity | Description   | Example      |
| ------ | ------------- | ------------ |
| PER    | Person        | Elon Musk    |
| ORG    | Organization  | OpenAI       |
| LOC    | Location      | Hyderabad    |
| MISC   | Miscellaneous | Olympics     |
| DATE   | Date          | 10 July 2026 |
| MONEY  | Currency      | $500         |

---

# Hands-on Experiment

In this notebook, I:

* Loaded a pre-trained NER model.
* Identified entities in sentences.
* Classified entities into different categories.
* Processed multiple paragraphs.
* Built an interactive entity recognizer.

---

# Key Learnings

* NER extracts structured information from unstructured text.
* Transformer models recognize context rather than simple keywords.
* Multiple entity types can exist in a single sentence.
* NER is an essential component of many enterprise AI systems.

---

# What's Next?

➡️ Day 13 – Question Answering
