from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base")

context = "Distributed scraping with Celery workers"

question = "How does the system scale?"

prompt = f"""
Answer the question using the context.

Context:
{context}

Question:
{question}
"""

inputs = tokenizer(prompt, return_tensors="pt")

outputs = model.generate(
    **inputs,
    max_new_tokens=100
)

answer = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)

print(answer)
