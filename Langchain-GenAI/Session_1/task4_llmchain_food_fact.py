"""
Session 1 - Task 4
Build a simple LangChain chain that takes a user's favorite food and uses
an LLMChain to generate a fun fact about it.
"""

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="http://localhost:11434/v1",  # or https://api.openai.com/v1
    api_key="ollama",
    model="llama3",
)

prompt = PromptTemplate(
    input_variables=["food"],
    template="Tell me one fun, surprising fact about {food}. Keep it to one sentence.",
)

fact_chain = LLMChain(llm=llm, prompt=prompt)

favorite_food = "pani puri"
result = fact_chain.run(food=favorite_food)

print(f"Fun fact about {favorite_food}: {result}")
