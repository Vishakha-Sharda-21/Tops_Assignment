"""
Session 3 - Task 4
Modify the IPL chatbot to handle follow-up questions like 'Who is the
captain?' after the user mentions an IPL team, using conversation memory.
"""

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# small lookup the LLM can lean on for factual captain questions
ipl_captains = {
    "mumbai indians": "Hardik Pandya",
    "chennai super kings": "Ruturaj Gaikwad",
    "gujarat titans": "Shubman Gill",
    "royal challengers bengaluru": "Rajat Patidar",
}

SYSTEM_TEMPLATE = """You are a friendly cricket chatbot. If the user mentions an
IPL team, remember it for follow-up questions like "who is the captain?".
Known captains: {captains_info}

Conversation so far:
{history}
Human: {input}
Bot:"""

prompt = PromptTemplate(
    input_variables=["history", "input"],
    template=SYSTEM_TEMPLATE.replace(
        "{captains_info}",
        ", ".join(f"{team.title()} -> {cap}" for team, cap in ipl_captains.items()),
    ),
)

llm = ChatOpenAI(base_url="http://localhost:11434/v1", api_key="ollama", model="llama3")
memory = ConversationBufferMemory(memory_key="history")
conversation = ConversationChain(llm=llm, memory=memory, prompt=prompt)

if __name__ == "__main__":
    turns = [
        "I support Gujarat Titans.",
        "Who is the captain?",  # follow-up, needs memory of the team just mentioned
    ]
    for turn in turns:
        print("User:", turn)
        print("Bot:", conversation.predict(input=turn))
        print()
