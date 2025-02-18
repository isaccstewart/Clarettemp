import fitz  
import ollama

def extract_text_from_pdf(pdf_path):
   
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text("text") + "\n"
    return text.strip()

def ask_mistral(context, question):
   
    response = ollama.chat(
        model="tinyllama",
        messages=[
            {"role": "system", "content": "You are a helpful AI that answers questions based on a provided document."},
            {"role": "user", "content": f"Here is a document:\n\n{context}\n\nNow, answer this question: {question}"}
        ]
    )
    return response["message"]["content"]

def main():
    pdf_path = input("Enter the path to the PDF file: ")
    
    print("\nExtracting text from the PDF...")
    pdf_text = extract_text_from_pdf(pdf_path)

    if not pdf_text:
        print("No text found in the PDF!")
        return
    
    print("\nChatbot: Ask me anything based on the document! (Type 'exit' to quit)")
    
    while True:
        question = input("\nYou: ").strip()
        if question.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        
        answer = ask_mistral(pdf_text, question)
        print("\nChatbot:", answer)

if __name__ == "__main__":
    main()
