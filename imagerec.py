import ollama


image_path = r"C:\Users\IsaccStewartW\Downloads\45190268992_034426ed7b_q.jpg"


response = ollama.generate(
    model="llava:latest",
    prompt="how many people are there in this image",
    images=[image_path]  
)

print("Caption:", response["response"])
