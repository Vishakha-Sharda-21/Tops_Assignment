"""
Session 6 - Task 3: AI Content Generator
Takes a topic (e.g., 'Best Cafes in Ahmedabad') and uses OpenAI's GPT API to write
a short blog post (max_tokens = 100).

Setup:  pip install openai
        set OPENAI_API_KEY=your_key      (Windows)  |  export OPENAI_API_KEY=your_key (Mac/Linux)

NOTE: The hint uses openai.Completion.create(), which was the OLD style (openai < 1.0)
and is now removed. The same idea in the new library is client.chat.completions.create().
The old-style version is kept below in comments for reference.
"""
from openai import OpenAI

client = OpenAI()   # reads OPENAI_API_KEY from the environment


def generate_blog(topic: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Write a short blog post about: {topic}"}],
        max_tokens=100,          # short output, as required
    )
    return response.choices[0].message.content.strip()


# ---- OLD STYLE (openai==0.28), as in the hint ----
# import openai
# openai.api_key = "YOUR_KEY"
# response = openai.Completion.create(
#     model="gpt-3.5-turbo-instruct",
#     prompt=f"Write a short blog post about: {topic}",
#     max_tokens=100,
# )
# return response.choices[0].text.strip()

if __name__ == "__main__":
    topic = input("Enter a topic: ") or "Best Cafes in Ahmedabad"
    print("\n" + generate_blog(topic))
