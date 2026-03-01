import asyncio
from wrapper import AIWrapper
import dotenv

dotenv.load_dotenv(dotenv_path=".env")
async def main():
    print("1. Chat with AI")
    print("2. Exit")
    while True:
        user_choice = input("Enter your choice: ")
        if user_choice == "1":
            ai_wrapper = AIWrapper("openai/gpt-oss-20b", 0.7, 1000)
            res =  ai_wrapper.ask_ai(question="Hello")
            print(res)
            json_tree = ai_wrapper.parse_intent(urls=['https://www.saflora.com.np', 'https://www.saflora.com.np/about', 'https://www.saflora.com.np/contact'])
            print(json_tree)
        elif user_choice == "2":
            break
    
    
if __name__ == "__main__":
    asyncio.run(main())
