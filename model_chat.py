import ollama
messages=[]
def chat():
    while True:
        user_input = input("You:")
        if user_input.lower() == "exit":
            break
        
        messages.append({"role":"user","content":user_input})
            
            
        response = ollama.chat(
            model="qwen2.5-coder:7b",
            messages=messages
        )
        reply= response["message"]["content"]
        messages.append({"role":"assistant","content":reply})
        print("Bot: ",reply)
        print()
if __name__== "__main__":
    chat()