# 📅 Day 09 – Conversational Memory in AI Chatbots

## 🎯 Objective

Learn how conversational memory enables AI chatbots to remember previous interactions and generate context-aware responses. Build a chatbot that stores conversation history and uses it to answer follow-up questions more naturally.

---

# 🤖 What is Conversational Memory?

Conversational Memory is the ability of an AI chatbot to remember previous messages during a conversation.

Instead of treating every question as completely independent, the chatbot uses earlier interactions as context to generate more relevant and coherent responses.

---

# Why is Conversational Memory Important?

Without memory:

**User:** My name is Geetha.

**Bot:** Nice to meet you!

**User:** What's my name?

**Bot:** I don't know.

---

With memory:

**User:** My name is Geetha.

**Bot:** Nice to meet you, Geetha!

**User:** What's my name?

**Bot:** Your name is Geetha.

Memory creates a smoother and more natural conversation.

---

# Types of Memory

## 1. Short-Term Memory

* Stores the current conversation.
* Lost when the session ends.
* Useful for ongoing chats.

---

## 2. Long-Term Memory

* Stores information across multiple sessions.
* Saved in files or databases.
* Useful for personalized assistants.

---

# Memory Workflow

```text
User Message
      │
      ▼
Conversation History
      │
      ▼
Append New Message
      │
      ▼
LLM
      │
      ▼
AI Response
      │
      ▼
Store Response
```

---

# Conversation History

The chatbot stores messages in the following format:

```json
[
  {
    "role": "user",
    "content": "My name is Geetha."
  },
  {
    "role": "assistant",
    "content": "Nice to meet you, Geetha!"
  }
]
```

This history is included with each new prompt.

---

# Hands-on Experiment

In this notebook, I:

* Built a chatbot with conversation memory.
* Stored user and assistant messages.
* Used previous messages as context.
* Saved conversation history in a JSON file.
* Created an interactive chat session.

---

# Key Learnings

* Memory helps maintain conversation context.
* Short-term memory improves chat continuity.
* Long-term memory enables personalization.
* Conversation history is the foundation of AI assistants.

---

# What's Next?

➡️ Day 10 – Building AI Agents with Tool Calling
