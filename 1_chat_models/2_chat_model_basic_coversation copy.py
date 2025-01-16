import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
load_dotenv()


model = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))


messages = [
    SystemMessage(content="You are a math assistant, solve the following math questions?"),
    HumanMessage(content="What is 7 * 5 ?")
]
 

result = model.invoke(messages)

print()
print("Answer from AI: ", result.content)



messages = [
    SystemMessage(content="You are a math assistant, solve the following math questions?"),
    HumanMessage(content="What is 7 * 5 ?"),
    AIMessage(content="35"),
    HumanMessage(content="What is 4 + 3 ?")
]


result = model.invoke(messages)

print()
print("Answer from AI: ", result.content)