import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage



chat_history = []


model = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))


system_message = SystemMessage(content="You are a helpful AI assistant")

chat_history.append(system_message)


while True:
    print()
    query = input("message: ")

    if query == "exit":
        break

    message = HumanMessage(query)

    chat_history.append(message)

    model = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))
    result = model.invoke(chat_history)

    print()
    print("Message from AI: ", result.content)

    ai_message = AIMessage(result.content)
    chat_history.append(ai_message)

print(chat_history)


