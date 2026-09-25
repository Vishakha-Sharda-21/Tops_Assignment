"""
Session 2 - Task 1
A simple LangChain Agent that answers basic questions about IPL teams
using a predefined dictionary of teams and their captains.
"""

from langchain.agents import initialize_agent, AgentType, Tool
from langchain_openai import ChatOpenAI

ipl_captains = {
    "Mumbai Indians": "Hardik Pandya",
    "Chennai Super Kings": "Ruturaj Gaikwad",
    "Gujarat Titans": "Shubman Gill",
    "Royal Challengers Bengaluru": "Rajat Patidar",
    "Kolkata Knight Riders": "Ajinkya Rahane",
}


def ipl_team_lookup(query: str) -> str:
    for team, captain in ipl_captains.items():
        if team.lower() in query.lower():
            return f"{team}'s captain is {captain}."
    return "I don't have data on that IPL team."


ipl_tool = Tool(
    name="IPLTeamLookup",
    func=ipl_team_lookup,
    description="Use this to answer questions about IPL teams and their captains.",
)

llm = ChatOpenAI(base_url="http://localhost:11434/v1", api_key="ollama", model="llama3")

agent = initialize_agent(
    tools=[ipl_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

if __name__ == "__main__":
    print(agent.run("Who is the captain of Gujarat Titans?"))
