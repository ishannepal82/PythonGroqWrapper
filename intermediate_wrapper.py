from langchain_groq import ChatGroq
from langchain.messages import SystemMessage, HumanMessage 
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from crawl4ai import AsyncWebCrawler
import os
os.environ["USER_AGENT"] = "Mozilla/5.0 (X11; Linux x86_64)"

load_dotenv(dotenv_path=".env")

base_url = "https://www.saflora.com.np"

class Parser():
    def parse_links(self, html):
        parsed = BeautifulSoup(html, "html.parser")
        return [link["href"] for link in parsed.find_all("a", href=True)]


class Crawler():
    async def crawl(self, url):
        async with AsyncWebCrawler() as crawler:
            res = await crawler.arun(url=url)
            return res
    
class Splitter():
    def __init__(self):
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100,
            separators=["\n\n", "\n", " ", ""],
            length_function=len
        )
        self.splitter = splitter
    def split_text(self, text):
       res = self.splitter.split_text(text)
       return res

class SafloraWrapper():
    def __init__(self, stream = False):
        self.stream = stream
        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0.7,
            streaming=self.stream
        )
        self.system = SystemMessage(content="You are a professional ai assistant for Saflora.Your domain is Saflora only if asked about any other subjects you will politely refuse to answer. You will only answer the questions related to Saflora. If the question is not related to Saflora, you will politely refuse to answer.")
        self.prompt = PromptTemplate.from_template("question:{prompt}")

        self.history = [self.system]

    def ask(self, message):
        formatted = self.prompt.format(
            prompt=message,
        )
        user_message = HumanMessage(content=formatted)

        self.history.append(user_message)
        response = self.llm.invoke(self.history)
        self.history.append(response)

        return response.content
    

if __name__ == "__main__":
    import asyncio

    async def main():
        crawler = Crawler()
        res = await crawler.crawl("https://www.saflora.com.np")
        print(res.html)
        parser = Parser()
        parsed_res = parser.parse_links(res.html)
        print(parsed_res)
    
    asyncio.run(main())