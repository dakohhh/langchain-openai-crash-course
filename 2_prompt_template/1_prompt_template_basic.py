from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage



# template = "Tell me a joke about {topic}"

# prompt_template = ChatPromptTemplate.from_template(template)

# print("------ PROMPT FROM TEMPLATE -------")
# prompt = prompt_template.invoke({ "topic": "cats" })
# print(prompt)


# template_multiple = """You are a helpful assistant.
# Human: Tell me a {adjective} story about a {animal}.
# Assistant:"""


# prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
# prompt = prompt_multiple.invoke({ "adjective": "sad", "animal": "bat"  })
# print("------ PROMPT FROM TEMPLATE MULTIPLE -------")
# print(prompt)




messages = [
    ("system", "You are a comedian that tells jokes about {topic}."),
    ("human", "Tell me {jokes_count} jokes.")
]


prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({ "topic": "bugs", "jokes_count" : 3 })
print(prompt)

