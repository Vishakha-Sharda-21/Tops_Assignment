"""
Session 2 - Task 5
Used ChatGPT to generate a first draft of a LangChain agent that combines
the Calculator tool and a Search tool. Domain chosen: FOOD DELIVERY.

Prompt given to ChatGPT:
    "Write a LangChain agent in Python that uses both the built-in
    llm-math calculator tool and a custom search tool, using
    ZERO_SHOT_REACT_DESCRIPTION."

ChatGPT's draft used a generic "search anything" tool with no real data
behind it, and didn't handle the case where the search term wasn't found -
it just returned an empty string, which confused the agent. Modified it
below for the food-delivery domain: the search tool now looks up mock
restaurant data, and returns a clear "not found" message instead of an
empty string.
"""

from langchain.agents import initialize_agent, AgentType, Tool, load_tools
from langchain_openai import ChatOpenAI

# Mock restaurant data for the food-delivery domain
restaurants = {
    "pizza": ["Domino's", "Pizza Hut", "La Pino'z"],
    "biryani": ["Paradise Biryani", "Behrouz Biryani", "Biryani By Kilo"],
    "chinese": ["Wow! Momo", "Mainland China", "China Bistro"],
}


def restaurant_search(query: str) -> str:
    query_lower = query.lower()
    for cuisine, places in restaurants.items():
        if cuisine in query_lower:
            return f"Top {cuisine} places near you: {', '.join(places)}"
    # MODIFIED: ChatGPT's original version returned "" here, which made the
    # agent loop confusingly. Returning a clear message fixes that.
    return "No matching restaurants found for that cuisine."


search_tool = Tool(
    name="RestaurantSearch",
    func=restaurant_search,
    description="Use this to find restaurants for a given cuisine (pizza, biryani, chinese).",
)

llm = ChatOpenAI(base_url="http://localhost:11434/v1", api_key="ollama", model="llama3")

math_tools = load_tools(["llm-math"], llm=llm)  # built-in calculator tool
all_tools = math_tools + [search_tool]

agent = initialize_agent(
    tools=all_tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

if __name__ == "__main__":
    print(agent.run("If I order 3 pizzas at 250 rupees each, what's the total? Also suggest some pizza places."))
