# Session 1 - Task 5
Three ways using chains in LangChain can improve an AI-powered app like
Zomato's food recommendation chatbot, compared to making direct LLM API calls:

1. **Reusable, structured prompts** - a chain wraps a PromptTemplate, so the
   "recommend a dish based on X" logic is defined once and reused with
   different inputs (cuisine, budget, mood) instead of rebuilding prompt
   strings by hand every time, which reduces bugs and inconsistent phrasing.

2. **Composability / multi-step workflows** - chains can be linked together
   (e.g. first classify the user's craving, then retrieve matching
   restaurants, then generate a friendly recommendation), so the app can do
   multi-step reasoning instead of being limited to one flat prompt-in,
   text-out API call.

3. **Easier integration with memory and tools** - a chain plugs naturally
   into LangChain's memory classes (so the bot remembers your cuisine
   preference across a session) and tools (so it can call a live restaurant
   API), which would all have to be built manually on top of a raw API call.
