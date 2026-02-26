from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

class ChatGroqWrapper:
    def __init__(self, stream = False):
        self.stream = stream
        self.model = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0.7,
            streaming=self.stream
        )

        self.system = SystemMessage(
            content ="You are a helpful assistant. You will be given a topic and a style, and you will explain the tpic in a given style.Your domain are philosophy and psychology.You will only answer the questions related to these domains. If the question is not related to these domains, you will politely refuse to answer."
            )
        
        self.prompt = PromptTemplate.from_template("{prompt}")
        
        self.history = [self.system]

    def ask(self, prompt: str) -> str:

        formatted = self.prompt.format(
            prompt=prompt
        )
        user_message = HumanMessage(content=formatted)

        self.history.append(user_message)
        response = self.model.invoke(self.history)
        self.history.append(response)

        return response.content


if __name__ == "__main__":
    wrapper = ChatGroqWrapper(
        stream=False
    )
    result1 = wrapper.ask(
        prompt="Explain the Concept of Free will in Philosophy in a concise and formal style"
    )

    result2 = wrapper.ask(
        prompt="No Make it more Humorous and Informal, feel free to use jokes and even be agressive if you want to."
    )

    print(result1, "\n\n", result2)