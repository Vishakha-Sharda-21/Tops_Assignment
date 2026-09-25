"""
Session 3 - Task 3
Add a prompt template so that when a user asks for a song recommendation,
the chatbot responds in the style of a Spotify playlist curator.
"""

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(base_url="http://localhost:11434/v1", api_key="ollama", model="llama3")

song_prompt = PromptTemplate(
    input_variables=["mood"],
    template=(
        "You are a Spotify playlist curator with a fun, trendy, upbeat voice. "
        "A user is in the mood for: {mood}. "
        "Recommend 3 songs that fit that mood, and give a short punchy one-line "
        "description for each, the way a Spotify 'Made For You' playlist blurb reads."
    ),
)

song_chain = LLMChain(llm=llm, prompt=song_prompt)

if __name__ == "__main__":
    mood = "a relaxed rainy evening"
    print(song_chain.run(mood=mood))
