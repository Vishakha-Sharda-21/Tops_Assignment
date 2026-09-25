"""
Session 4 - Task 4
Connect the custom calculator tool to a chatbot so that when a user types
a calculation request (like 'What is 15*3?'), the chatbot uses the tool.
"""

from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain_openai import ChatOpenAI

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from task3_custom_calculator_tool import calculator_tool

llm = ChatOpenAI(base_url="http://localhost:11434/v1", api_key="ollama", model="llama3")

agent = initialize_agent(
    tools=[calculator_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

if __name__ == "__main__":
    print(agent.run("What is 15 multiply 3?"))
