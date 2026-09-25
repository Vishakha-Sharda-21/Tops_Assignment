"""
Session 2 - Task 3
A mock "Search" tool that lets an agent fetch trending movies from a
Python dictionary simulating BookMyShow data.
"""

from langchain.agents import initialize_agent, AgentType, Tool
from langchain_openai import ChatOpenAI

trending_movies = {
    "bollywood": ["Jawan 2", "Singham Again 2", "Pathaan Returns"],
    "hollywood": ["Avatar 3", "Deadpool 4", "Mission Impossible 9"],
    "south": ["Pushpa 3", "KGF 3", "Salaar 2"],
}


def search_trending_movies(query: str) -> str:
    query_lower = query.lower()
    for category, movies in trending_movies.items():
        if category in query_lower:
            return f"Trending {category} movies on BookMyShow: {', '.join(movies)}"
    # no category matched - return everything
    all_movies = [m for movies in trending_movies.values() for m in movies]
    return f"Trending movies on BookMyShow: {', '.join(all_movies)}"


movie_search_tool = Tool(
    name="TrendingMoviesSearch",
    func=search_trending_movies,
    description="Use this to find trending movies on BookMyShow, optionally filtered by category (bollywood/hollywood/south).",
)

llm = ChatOpenAI(base_url="http://localhost:11434/v1", api_key="ollama", model="llama3")

agent = initialize_agent(
    tools=[movie_search_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

if __name__ == "__main__":
    print(agent.run("Show me trending movies on BookMyShow"))
