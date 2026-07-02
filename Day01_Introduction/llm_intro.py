from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

prompt = "Artificial Intelligence is transforming"

result = generator(
    prompt,
    max_new_tokens=50,
    do_sample=True,
    temperature=0.7
)

print("Prompt:")
print(prompt)

print("\nGenerated Text:")
print(result[0]["generated_text"])
