"""
Session 4 - Task 2
A Zomato-style food ordering chatbot that remembers the user's chosen
restaurant and cuisine across the conversation using ConversationBufferMemory.
"""

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

SYSTEM_TEMPLATE = """You are Zomato's food ordering assistant. Once the user tells you
their chosen restaurant and cuisine preference, remember them for the rest of the
conversation and reference them naturally in later replies.

Conversation so far:
{history}
Human: {input}
Zomato Bot:"""

prompt = PromptTemplate(input_variables=["history", "input"], template=SYSTEM_TEMPLATE)

llm = ChatOpenAI(base_url="http://localhost:11434/v1", api_key="ollama", model="llama3")
memory = ConversationBufferMemory(memory_key="history")
conversation = ConversationChain(llm=llm, memory=memory, prompt=prompt)

if __name__ == "__main__":
    turns = [
        "I want to order from Paradise Biryani.",
        "I prefer Hyderabadi cuisine.",
        "What would you recommend from there?",
    ]
    for turn in turns:
        print("User:", turn)
        print("Zomato Bot:", conversation.predict(input=turn))
        print()
