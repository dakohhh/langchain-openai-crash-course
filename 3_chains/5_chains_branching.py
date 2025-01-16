import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.messages import SystemMessage, AIMessage
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableBranch
load_dotenv()


model = ChatOpenAI(model="gpt-3.5-turbo", api_key=os.getenv("OPENAI_API_KEY"))


positive_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("human", "Generate a thank you message for customer on his/her positive feedback: {feedback} ")
    ]
)

negative_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("human", "Generate an apology message and request for more details for this customer on his/her this negative feedback: {feedback} ")
    ]
)


neutral_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("human", "Generate a response and request for more details regarding this neutral feedback: {feedback} ")
    ]
)


escalate_feedback_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        ("human", "Generate a message to escalate this feedback to a human agent: {feedback} ")
    ]
)

classification_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant, once give a feedback, classify the feedback into one of these positive, negative, neutral or escalate "),
        ("human", "Classify this feedback: {feedback}")
    ]
)


branches = RunnableBranch(
    (
        lambda x: "positive" in x.lower(),
        positive_feedback_template | model | StrOutputParser()
    ),

    (
        lambda x: "negative" in x.lower(),
        negative_feedback_template | model | StrOutputParser()
    ),

    (
        lambda x: "neutral" in x.lower(),
        neutral_feedback_template | model | StrOutputParser()
    ),
    
    escalate_feedback_template | model | StrOutputParser()
)


classification_chain = classification_template | model | StrOutputParser()

chain = classification_chain | branches


response = chain.invoke({ "feedback": "I dont like this product" })


print(response)