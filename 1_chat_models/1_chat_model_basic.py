import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
load_dotenv()


model = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))


result = model.invoke("What is 81 divided by 9?")

print()
print("Full Result: ", result)
print()
print("Result: ", result.content)

 
