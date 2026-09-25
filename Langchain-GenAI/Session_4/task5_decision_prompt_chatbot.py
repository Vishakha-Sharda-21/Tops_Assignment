"""
Session 4 - Task 5
Used ChatGPT to generate a prompt template that helps the chatbot decide
when to use the calculator tool vs. answer normally, then tested it with
two different user queries.

Prompt given to ChatGPT:
    "Write a system prompt for a LangChain agent that has a calculator tool,
    telling it to only use the tool for arithmetic questions and answer
    conversationally otherwise."
"""

from langchain.agents import initialize_agent, AgentType
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from task3_custom_calculator_tool import calculator_tool

# AI-generated decision prompt (used as the agent's prefix)
DECISION_PROMPT = """You are a helpful assistant with access to a Calculator tool.
- If the user's message involves arithmetic (addition, subtraction, multiplication,
  division, or numbers being combined mathematically), use the Calculator tool to
  compute the exact answer rather than guessing.
- If the user's message is conversational and does NOT require arithmetic,
  answer normally in plain, friendly language without using any tool.
"""

llm = ChatOpenAI(base_url="http://localhost:11434/v1", api_key="ollama", model="llama3")

agent = initialize_agent(
    tools=[calculator_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    agent_kwargs={"prefix": DECISION_PROMPT},
    verbose=True,
)

if __name__ == "__main__":
    test_queries = [
        "What is 15 * 3?",              # should trigger the calculator tool
        "What's a good IPL team to follow this season?",  # should NOT use the tool
    ]
    for q in test_queries:
        print("User:", q)
        print("Bot:", agent.run(q))
        print()
