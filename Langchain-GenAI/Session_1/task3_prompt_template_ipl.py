"""
Session 1 - Task 3
Use LangChain's PromptTemplate to dynamically build a question from a
user's favorite IPL team.
"""

from langchain.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["team"],
    template="Why do you support {team} in IPL?",
)

final_prompt = template.format(team="Gujarat Titans")
print("Final prompt:", final_prompt)
