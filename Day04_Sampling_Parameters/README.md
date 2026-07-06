# Day 04 – Temperature, Top-k & Top-p Sampling

## 🎯 Objective

Learn how Large Language Models generate text using different sampling strategies. Explore how **Temperature**, **Top-k**, and **Top-p (Nucleus Sampling)** influence the creativity, randomness, and quality of generated responses.
---
# 🤖 Why Sampling Matters
When an LLM predicts the next token, it doesn't always choose the most probable one. Instead, it can sample from multiple possible tokens to produce more natural and diverse responses.
Sampling strategies help balance:
* Creativity
* Accuracy
* Diversity
* Consistency
---
# 🌡️ Temperature
Temperature controls how random the model's predictions are.
* **Low Temperature (0.1–0.3):**
  * More deterministic
  * Predictable responses
  * Best for factual tasks
* **Medium Temperature (0.5–0.8):**
  * Balanced creativity
  * Good for most applications
* **High Temperature (1.0–1.5):**
  * More creative
  * More diverse responses
  * Higher chance of mistakes or repetition
### Example
**Prompt:**
```text
The future of Artificial Intelligence is
```
**Temperature = 0.2**
> The future of Artificial Intelligence is focused on improving automation and decision-making across industries.
**Temperature = 1.2**
> The future of Artificial Intelligence is an exciting blend of creativity, autonomous systems, and technologies we have yet to imagine.
---
# 🔝 Top-k Sampling
Top-k limits the model to selecting the next token from only the **k most probable tokens**.
Example:
Predicted probabilities:
| Token   | Probability |
| ------- | ----------: |
| AI      |        0.35 |
| Machine |        0.25 |
| Future  |        0.18 |
| Robot   |        0.12 |
| Space   |        0.10 |
If **Top-k = 3**, only:
* AI
* Machine
* Future
are considered.
Higher values increase diversity, while lower values make responses more focused.
---
# 🎯 Top-p (Nucleus Sampling)

Top-p selects the smallest group of tokens whose cumulative probability reaches a chosen threshold.

Example:

| Token   | Probability | Cumulative |
| ------- | ----------: | ---------: |
| AI      |        0.35 |       0.35 |
| Machine |        0.25 |       0.60 |
| Future  |        0.18 |       0.78 |
| Robot   |        0.12 |       0.90 |
| Space   |        0.10 |       1.00 |

If **Top-p = 0.90**, the model samples from:

* AI
* Machine
* Future
* Robot

Top-p adapts dynamically based on the probability distribution.

---

# 🔍 Comparison

| Parameter   | Controls                         | Typical Use                 |
| ----------- | -------------------------------- | --------------------------- |
| Temperature | Randomness                       | Creativity vs. consistency  |
| Top-k       | Number of candidate tokens       | Restrict token choices      |
| Top-p       | Cumulative probability threshold | Dynamic candidate selection |

---
# 🧪 Hands-on Experiment

In this notebook, I generated text using different combinations of:

* Temperature
* Top-k
* Top-p

and compared how each parameter changes the model's responses.
---
# 📚 Key Learnings

* Lower temperature produces more predictable text.
* Higher temperature increases creativity and diversity.
* Top-k restricts the model to the most likely next tokens.
* Top-p dynamically adjusts the candidate token pool based on probabilities.
* Combining these parameters allows developers to tune model behavior for different tasks.
---

# 🚀 What's Next?

➡️ Day 05 – Embeddings & Vector Representations
