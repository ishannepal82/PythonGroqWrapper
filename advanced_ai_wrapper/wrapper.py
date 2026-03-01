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
        self.ai_intent_parser_message = SystemMessage(content="You are a helpful assistant, your role is to generate the meeaning of a provided list of urls. You have only one job to generate the json like structures of the urls: {urls: [{title: '', description_of_the_page_from_the_url: '', url: ''} ...]}.You cannot add the description you are not sure about, you cannot create your own salfora for matching the request.You can add void entries like saflora is a brand or let's say for contact pages: this page include contacts and info for saflora. Description can be short and keep them short.")
    
        self.history = [self.system]

    def clear_history():
        pass 

    def ask_ai(self, question):
        self.history.append(HumanMessage(content=question))
        return self.llm.invoke(self.history)
    
    def parse_intent(self, urls):
        return self.llm.invoke([self.ai_intent_parser_message, HumanMessage(content=str(urls))])

        

