import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage
load_dotenv()


messages = [
    SystemMessage(content="You are a math assistant, solve the following math questions?"),
    HumanMessage(content="What is 7 * 5 ?")
]


# ChatGPT Model
model = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))
result = model.invoke(messages)
print()
print("Answer from AI: ", result.content)


# Anthropic Chat Model
model = ChatAnthropic(model="claude-3-sonnet-20240229", api_key=os.getenv("ANTHROPIC_API_KEY"))
result = model.invoke(messages)
print()
print("Answer from AI: ", result.content)


# Google Chat Model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=os.getenv("GOOGLE_GENAI_API_KEY"))
result = model.invoke(messages)
print()
print("Answer from AI: ", result.content)