import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableSequence

load_dotenv()


model = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))


messages = [
    ("system", "You are a comedian that tells jokes about {topic}."),
    ("human", "Tell me {jokes_count} jokes.")
]


prompt_template = ChatPromptTemplate.from_messages(messages)

uppercase_output = RunnableLambda(lambda x: x.upper())

word_count = RunnableLambda(lambda x: f"Word count: {len(x.split())} \n {x} ")


chain =  prompt_template | model | StrOutputParser() | uppercase_output | word_count

response = chain.invoke({ "topic": "bugs", "jokes_count" : 3 })


print(response)



