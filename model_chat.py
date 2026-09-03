import ollama
messages=[]
def chat():
    ollama.create(model='Anteater', system="SYSTEM You are an experienced and patient Code Tutor called Anteater. Your goal is to guide the user through Python programming without giving away full, copy-pasteable code solutions. Explain the underlying issue briefly, provide hints or leading questions to point them in the right direction, and show only short, conceptual snippets. Be concise and professional.",from_="qwen2.5-coder:7b")
    while True:
        user_input = input("You:")
        if user_input.lower() == "exit":
            break
        
        messages.append({"role":"user","content":user_input})
            
        response = ollama.chat(model="Anteater", messages=messages,)
        reply= response["message"]["content"]
        messages.append({"role":"assistant","content":reply})
        print("Bot: ",reply)
        print()
if __name__== "__main__":
    chat()