import os
import uuid
import psycopg
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_postgres import PostgresChatMessageHistory

load_dotenv()

SESSION_ID = str(uuid.uuid4())
TABLE_NAME = "chat_history"



print("Initializing PostgreSQL Chat Message History")
sync_connection = psycopg.connect("postgresql://postgres:wisdom@localhost/langchain")

chat_history = PostgresChatMessageHistory(TABLE_NAME, "e7a215d0-872b-46a8-8ff8-b9a88ae4565c", sync_connection=sync_connection)


print("Chat history initialized")
print("Current Chat Messages", chat_history.messages)



system_message = SystemMessage("You are a helpful math AI assistant")

chat_history.add_message(system_message)


while True:
    print()
    message_input = input("Human: ")

    model = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-3.5-turbo")

    human_message = HumanMessage(message_input)

    chat_history.add_message(human_message)


    result = model.invoke(chat_history.messages)

    print()
    print(result.content)

    chat_history.add_message(AIMessage(result.content))












