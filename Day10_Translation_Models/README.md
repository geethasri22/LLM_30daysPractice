# 📅 Day 10 – Translation Models

## 🎯 Objective

Learn how Transformer-based translation models convert text from one language to another. Build a multilingual translator using Hugging Face pipelines and explore how neural machine translation works.

---

# 🌍 What is Machine Translation?

Machine Translation (MT) is the task of automatically converting text from one language into another while preserving its meaning.

Traditional translation systems relied on rules and dictionaries. Modern systems use Transformer-based neural networks to generate fluent and context-aware translations.

---

# Why Translation Models Matter

Translation models are widely used in:

* Google Translate
* International customer support
* Multilingual chatbots
* Cross-language search
* Education platforms
* Travel applications
* Global business communication

---

# Translation Pipeline

```text
Input Sentence
        │
        ▼
Tokenizer
        │
        ▼
Translation Model
        │
        ▼
Decoder
        │
        ▼
Translated Sentence
```

---

# Popular Translation Models

* Helsinki-NLP OPUS-MT
* mBART
* M2M100
* NLLB (No Language Left Behind)

---

# Hands-on Experiment

In this notebook, I:

* Loaded a pre-trained translation model.
* Translated English text into French.
* Translated English text into German.
* Compared outputs for different languages.
* Built an interactive translator.

---

# Key Learnings

* Translation models use the Transformer architecture.
* Tokenization is required before translation.
* The same sentence can be translated into multiple languages.
* Hugging Face provides pre-trained multilingual models.

---

# What's Next?

➡️ Day 11 – Sentiment Analysis
