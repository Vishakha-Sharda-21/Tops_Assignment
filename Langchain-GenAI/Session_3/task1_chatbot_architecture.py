"""
Session 3 - Task 1
Prints a simple text-based flow diagram of how user input is processed
by an LLM-based chatbot.
"""

def print_architecture():
    diagram = """
    +-------------------+
    |    User Input      |
    |  "Recommend a      |
    |   song for me"     |
    +---------+----------+
              |
              v
    +-------------------+
    |  Prompt Template    |
    |  (formats input     |
    |   into a structured |
    |   prompt string)    |
    +---------+----------+
              |
              v
    +-------------------+
    |  (Optional) Memory  |
    |  injects past       |
    |  conversation turns |
    +---------+----------+
              |
              v
    +-------------------+
    |     LLM Call        |
    |  (LangChain -> LLM  |
    |   e.g. GPT / Llama) |
    +---------+----------+
              |
              v
    +-------------------+
    |  (Optional) Tools /  |
    |  Agent decides if a  |
    |  tool call is needed |
    +---------+----------+
              |
              v
    +-------------------+
    |   Response Parsed   |
    |   & Returned to      |
    |   the User           |
    +-------------------+
    """
    print(diagram)


if __name__ == "__main__":
    print_architecture()
