import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

load_dotenv()


model = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))



# template = "Tell me a joke about {topic}"

# prompt_template = ChatPromptTemplate.from_template(template)

# print("------ PROMPT FROM TEMPLATE -------")
# prompt = prompt_template.invoke({ "topic": "cats" })

# result = model.invoke(prompt)




# print("------ PROMPT FROM TEMPLATE MULTIPLE -------")

# template_multiple = """You are a helpful assistant.
# Human: Tell me a {adjective} story about a {animal}.
# Assistant:"""

# prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
# prompt = prompt_multiple.invoke({ "adjective": "motivational", "animal": "bat"  })

# result = model.invoke(prompt)

# print(result.content)



print("------ PROMPT FROM WITH SYSTEM AND HUMAN MESSAGES -------")

messages = [
    ("system", "You are a comedian that tells jokes about {topic}."),
    ("human", "Tell me {jokes_count} jokes.")
]

prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({ "topic": "bugs", "jokes_count" : 3 })

result = model.invoke(prompt)

print(result.content)
