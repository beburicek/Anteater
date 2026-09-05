import ollama

class AnteaterChat:
    def __init__(self):
        self.messages = []
        ollama.create(
            model='Anteater',
            system="SYSTEM You are an experienced and patient Code Tutor called Anteater. Your goal is to guide the user through Python programming without giving away full, copy-pasteable code solutions. Explain the underlying issue briefly, provide hints or leading questions to point them in the right direction, and show only short, conceptual snippets. Be concise and professional.",
            from_="qwen2.5-coder:7b"
        )

    def send_message_stream(self, user_input: str):
        self.messages.append({"role": "user", "content": user_input})
        
        
        response = ollama.chat(model="Anteater", messages=self.messages, stream=True)
        
        full_reply = ""
        for chunk in response:
            token = chunk['message']['content']
            full_reply += token
            yield token  

        
        self.messages.append({"role": "assistant", "content": full_reply})