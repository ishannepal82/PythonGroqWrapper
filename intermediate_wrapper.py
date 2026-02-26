from langchain_groq import ChatGroq
from langchain.messages import SystemMessage, HumanMessage 
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

import os
os.environ["USER_AGENT"] = "Mozilla/5.0 (X11; Linux x86_64)"

load_dotenv(dotenv_path=".env")

base_url = "https://www.saflora.com.np"

loader = WebBaseLoader(base_url)
docs = loader.load()
scraped_html = loader._scrape(base_url)

print(docs)
print(scraped_html)

html = docs[0].page_content
soup = BeautifulSoup(html, "html.parser")

links = []

for a in soup.find_all("a", href=True):
    full_url = urljoin(base_url, a["href"])
    print(full_url)
    if urlparse(full_url).netloc == urlparse(base_url).netloc:
        links.append(full_url)

# Remove homepage duplicate
print(links)

# Load all discovered pages
multi_loader = WebBaseLoader(links)
all_docs = multi_loader.load()
print(f"Loaded {len(all_docs)}: {all_docs} documents")

# splitter = RecursiveCharacterTextSplitter(
#     chunk_size=300,
#     chunk_overlap=50,
# )

# # print(f"formal text {res}")

# html_content = res[0].page_content
# print(f"HTML: {html_content[:2000]}")
# splitted_res = splitter.split_text(html_content)

# print(f"Spillted Text {splitted_res}")

# class SafloraWrapper():
#     def __init__(self, stream = False):
#         self.stream = stream
#         self.llm = ChatGroq(
#             model="llama-3.1-8b-instant",
#             temperature=0.7,
#             streaming=self.stream
#         )
#         self.system = SystemMessage(content="You are a professional ai assistant for Saflora.Your domain is Saflora only if asked about any other subjects you will politely refuse to answer. You will only answer the questions related to Saflora. If the question is not related to Saflora, you will politely refuse to answer.")
#         self.prompt = PromptTemplate.from_template("question:{prompt}")

#         self.history = [self.system]

#     def ask(self, message):
#         formatted = self.prompt.format(
#             prompt=message,
#         )
#         user_message = HumanMessage(content=formatted)

#         self.history.append(user_message)
#         response = self.llm.invoke(self.history)
#         self.history.append(response)

#         return response.content
    

# if __name__ == "__main__":
#     wrapper = SafloraWrapper(
#         stream=False
#     )
#     result1 = wrapper.ask(
#         message="What is Saflora?"
#     )

#     result2 = wrapper.ask(
#         message="Who are the founders?"
#     )

#     print(result1, "\n\n", result2)
    
