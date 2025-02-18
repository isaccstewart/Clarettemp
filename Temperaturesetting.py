import ollama

response = ollama.chat(model='mistral', messages=[{"role": "user", "content": "whats the most creative thing you can do?"}], options={"temperature": 0.7, "top_p": 0.9})
print(response['message']['content'])


# 1️⃣ Temperature (0 to 1) → Controls general randomness (Lower = more predictable, Higher = more creative