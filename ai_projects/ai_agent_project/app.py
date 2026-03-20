from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

# import keys from env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
response = llm.invoke("Say hello!")
print(response.content)
