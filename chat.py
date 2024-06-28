from langchain_community.llms import Cohere
chat = Cohere(cohere_api_key="YgzcK00WuBRyeyyMrEYsuhc4U7Gail955W0sTfyc")

from langchain.schema.messages import HumanMessage, SystemMessage
messages = [
    SystemMessage(content="Can you tell me a joke?"),
    HumanMessage(content="what is your name?"),
]
response = chat.invoke(messages)
print(response)