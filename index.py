from langchain_community.llms import Cohere
llm = Cohere(cohere_api_key="your_cohere_api_key")

response = llm.invoke("List the seven wonders of the world.")
print(response)
