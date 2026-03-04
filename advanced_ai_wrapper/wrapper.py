from langchain_groq import ChatGroq
from langchain.messages import SystemMessage, HumanMessage

class AIWrapper():
    def __init__(self, model_name, temperature, max_tokens):
        self.llm = ChatGroq(
            model=model_name,
            temperature=temperature,
            max_tokens=max_tokens
        )

        self.system = SystemMessage(content="You are a helpful assistant.")
    
        self.history = [self.system]

    def clear_history():
        pass 

    def ask_ai(self, question):
        prompt = HumanMessage(content=question)
        self.history.append(prompt)
        print(self.history)
        return self.llm.invoke(self.history)
        

