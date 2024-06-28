from langchain_community.llms import Cohere
llm = Cohere(cohere_api_key="YgzcK00WuBRyeyyMrEYsuhc4U7Gail955W0sTfyc")

response = llm.invoke("List the seven wonders of the world.")
print(response)