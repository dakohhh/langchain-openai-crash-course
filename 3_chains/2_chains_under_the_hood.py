import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableSequence

load_dotenv()


model = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))


messages = [
    ("system", "You are a comedian that tells jokes about {topic}."),
    ("human", "Tell me {jokes_count} jokes.")
]


prompt_template = ChatPromptTemplate.from_messages(messages)



# Create Individual runnables (steps in the chain)

format_prompt = RunnableLambda(lambda x: prompt_template.format_prompt(**x))
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages()))
parse_output = RunnableLambda(lambda x: x.content)


# Create a runnable Sequence (equivalent to the LCEL chain)
chain = RunnableSequence(first=format_prompt, middle=[invoke_model], last=parse_output)

response = chain.invoke({ "topic": "bugs", "jokes_count" : 3 })


print(response)



