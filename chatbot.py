import ollama

def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break

        response = ollama.chat(model="mistral", mwhat is todays delattr": user_input}])
        print("Chatbot:", response["message"]["content"])

chat()
