# Day 03 – Tokens & Tokenization

## 🎯 Objective

Understand how Large Language Models process text by converting it into smaller units called **tokens**. Learn why tokenization is essential for LLMs and explore how Hugging Face tokenizers encode and decode text.

---

# 🤖 What is a Token?

A **token** is the smallest unit of text that a language model processes. Depending on the tokenizer, a token can represent:

* A complete word
* Part of a word
* A punctuation mark
* A number
* A special symbol

Unlike humans, LLMs do not read sentences directly. They first break the input into tokens before processing it.

---

# What is Tokenization?

**Tokenization** is the process of converting raw text into tokens that an LLM can understand.

### Example

Sentence:

```text
Artificial Intelligence is amazing!
```

Possible tokens:

```text
Artificial
Intelligence
is
amazing
!
```

Different models use different tokenization algorithms, so the same sentence may be split differently.

---

# Why is Tokenization Important?

Tokenization enables LLMs to:

* Process text efficiently.
* Build numerical representations of language.
* Handle unknown words by splitting them into smaller pieces.
* Measure input and output lengths using token counts.
* Calculate API usage and costs based on tokens.

---

# Encoding and Decoding

### Encoding

Encoding converts text into numerical token IDs.

```text
Text
   ↓
Tokenizer
   ↓
Token IDs
```

Example:

```text
"Hello AI"

↓

[15496, 9552]
```

---

### Decoding

Decoding converts token IDs back into readable text.

```text
Token IDs
    ↓
Tokenizer
    ↓
Readable Text
```

---

# Hands-on Experiment

In this notebook, I explored:

* Loading a tokenizer
* Encoding text into token IDs
* Decoding token IDs back into text
* Counting tokens
* Comparing tokenization for different sentences

---

# Key Learnings

* LLMs process tokens instead of raw text.
* Tokenizers convert text into numerical IDs.
* Different models may tokenize the same sentence differently.
* Token count affects context limits, response length, and API pricing.

---
1. Tokenization Flow ⭐
Input Text
     │
     ▼
Tokenizer
     │
     ▼
Tokens
     │
     ▼
Token IDs
2. Encoding Process
Hello AI

↓

Tokenizer

↓

["Hello", "AI"]

↓

[15496, 9552]
3. Decoding Process
[15496, 9552]

↓

Tokenizer

↓

Hello AI
4. Notebook Output Screenshot

Capture the output showing:

Tokens
Token IDs
Decoded text
Token count
5. Token Count Comparison
Sentence	Tokens
Hello!	
2 Artificial Intelligence	
3 ChatGPT is amazing!	
5 I love learning LLMs.	6

# What's Next?

➡️ Day 04 – Temperature, Top-k & Top-p Sampling
