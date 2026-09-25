"""
Session 1 - Task 2
Send a prompt to OpenAI's GPT-3.5 API DIRECTLY (no LangChain), print the
response, and list two problems with this direct-API approach.
"""

from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")  # replace with your key

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Why do you support Gujarat Titans in IPL?"}],
)

print("Response:", response.choices[0].message.content)

# ---------------------------------------------------------------
# Two problems with calling the API directly like this:
#
# 1. No built-in prompt management - if I want reusable prompt templates
#    (e.g. swapping the team name for different users), I have to hand-roll
#    my own string formatting / f-strings everywhere instead of using a
#    proper PromptTemplate abstraction. This gets messy fast in a real app.
#
# 2. No easy error handling / retry / fallback logic - if the API call
#    fails (rate limit, timeout, network blip), there's nothing here to
#    retry, fall back to a cached answer, or swap providers. At scale
#    (e.g. hundreds of users) this direct call also doesn't compose well
#    with memory, tools, or multi-step chains - I'd have to build all of
#    that myself instead of getting it from a framework.
# ---------------------------------------------------------------
