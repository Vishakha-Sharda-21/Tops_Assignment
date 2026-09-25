"""
Session 3 - Task 2
A chatbot that takes a user's favorite IPL team as input and generates a
friendly response using an LLM, displaying the conversation in the terminal.
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

if __name__ == "__main__":
    print("IPL Buddy Chatbot (type 'quit' to exit)")
    while True:
        team = input("Which IPL team do you support? ")
        if team.strip().lower() == "quit":
            break
        response = chain.run(team=team)
        print("Bot:", response)
