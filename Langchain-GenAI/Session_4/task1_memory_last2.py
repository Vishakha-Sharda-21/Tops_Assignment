"""
Session 4 - Task 1
A simple chatbot with conversation memory limited to the last 2 messages,
using LangChain's ConversationBufferWindowMemory (k=2).
"""

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(base_url="http://localhost:11434/v1", api_key="ollama", model="llama3")

# k=2 keeps only the last 2 exchanges in memory
memory = ConversationBufferWindowMemory(k=2)
conversation = ConversationChain(llm=llm, memory=memory)

if __name__ == "__main__":
    turns = [
        "Hi, I'm planning a trip to Goa.",
        "I like beaches and seafood.",
        "What should I pack?",
    ]
    for turn in turns:
        print("User:", turn)
        print("Bot:", conversation.predict(input=turn))
        print()
