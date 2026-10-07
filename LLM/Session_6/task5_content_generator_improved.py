"""
Session 6 - Task 5: Improved AI Content Generator

Question asked to the AI tool: "How can I make my GPT-based content generator more engaging for users?"
Main suggestions received: (1) give the model a role, tone and audience, (2) ask for a catchy title,
a hook and a call-to-action, (3) let the user choose the tone, (4) add emojis/hashtags.

Suggestion IMPLEMENTED in this file: let the user pick a TONE, and use a better structured prompt
(catchy title + engaging opening line + call-to-action) instead of a plain prompt.
"""
from openai import OpenAI

client = OpenAI()

TONES = {"1": "fun and friendly", "2": "professional", "3": "youthful and trendy"}


def generate_blog(topic: str, tone: str = "fun and friendly") -> str:
    prompt = (
        f"You are a popular Indian lifestyle blogger. Write a short blog post about '{topic}' "
        f"in a {tone} tone for college students. "
        "Start with a catchy title, then an engaging opening line, "
        "and end with a one-line call-to-action. Use 1-2 emojis."
    )
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,   # slightly higher so title + CTA are not cut off
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    topic = input("Enter a topic: ") or "Best Cafes in Ahmedabad"
    print("Choose tone: 1) Fun  2) Professional  3) Trendy")
    tone = TONES.get(input("Your choice (1/2/3): ").strip(), TONES["1"])
    print("\n" + generate_blog(topic, tone))
