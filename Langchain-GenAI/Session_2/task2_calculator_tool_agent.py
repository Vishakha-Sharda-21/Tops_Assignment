"""
Session 2 - Task 2
Integrate LangChain's built-in Calculator (llm-math) tool into an agent so
it can answer math questions like 'What is 12 times 8?'.
"""

from langchain.agents import initialize_agent, AgentType, load_tools
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(base_url="http://localhost:11434/v1", api_key="ollama", model="llama3")

# "llm-math" is LangChain's built-in calculator tool
tools = load_tools(["llm-math"], llm=llm)

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

if __name__ == "__main__":
    print(agent.run("What is 12 times 8?"))
