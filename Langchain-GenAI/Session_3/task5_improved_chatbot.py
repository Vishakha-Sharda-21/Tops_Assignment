"""
Session 3 - Task 5
Tested the chatbot locally and asked ChatGPT to suggest one improvement
for making its answers more natural/engaging.

ChatGPT's suggestion: "Add light emoji usage tied to the topic (e.g. a
cricket ball emoji for IPL talk) and personalize the closing line using
the team/topic just mentioned, instead of ending every reply the same way."

Implemented below: the response now gets a topic-appropriate emoji appended
and a personalized closing line built from the team name, instead of a
generic LLM reply with no personalization.
"""

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(base_url="http://localhost:11434/v1", api_key="ollama", model="llama3")

prompt = PromptTemplate(
    input_variables=["team"],
    template=(
        "The user's favorite IPL team is {team}. "
        "Respond in a warm, friendly, enthusiastic tone as a cricket-loving chatbot."
    ),
)

chain = LLMChain(llm=llm, prompt=prompt)


def improved_response(team: str) -> str:
    base_response = chain.run(team=team)

    # IMPROVEMENT (from ChatGPT's suggestion): add an emoji + personalized closer
    personalized_closer = f"\n\nGo {team}! 🏏🔥"
    return base_response.strip() + personalized_closer


if __name__ == "__main__":
    print("Improved IPL Buddy Chatbot (type 'quit' to exit)")
    while True:
        team = input("Which IPL team do you support? ")
        if team.strip().lower() == "quit":
            break
        print("Bot:", improved_response(team))
