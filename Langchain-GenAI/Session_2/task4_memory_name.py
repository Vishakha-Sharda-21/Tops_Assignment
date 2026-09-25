"""
Session 2 - Task 4
Add conversational memory to an agent/chain so it remembers the user's
name after they introduce themselves and uses it in later responses.
"""

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(base_url="http://localhost:11434/v1", api_key="ollama", model="llama3")

memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory, verbose=False)

if __name__ == "__main__":
    turns = [
        "Hi, my name is Aarav.",
        "What's a good IPL team to follow?",
        "Can you say my name back to me?",
    ]
    for turn in turns:
        print("User:", turn)
        print("Bot:", conversation.predict(input=turn))
        print()
