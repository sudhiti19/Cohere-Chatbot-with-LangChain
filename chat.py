from langchain_community.llms import Cohere
chat = Cohere(cohere_api_key="your_cohere_api_key")

from langchain.schema.messages import HumanMessage, SystemMessage
messages = [
    SystemMessage(content="Can you tell me a joke?"),
    HumanMessage(content="what is your name?"),
]
response = chat.invoke(messages)
print(response)
