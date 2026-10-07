# SESSION 3 - Open vs Closed Source Models + Ollama

## Task 1: Open source vs closed source LLMs

**Open source / open-weight LLMs**

| LLM | Example app / service that could benefit |
|-----|-------------------------------------------|
| Llama 2 / Llama 3 (Meta) | WhatsApp-style customer support bot that a company hosts on its own server |
| Falcon (TII) | Zomato-type app generating restaurant description/summaries without sending data outside |
| Mistral 7B (Mistral AI) | Small offline Instagram-like caption helper running on a low-cost server |

**Closed source LLMs**

| LLM | Example app / service that could benefit |
|-----|-------------------------------------------|
| GPT-4 (OpenAI) | Instagram - high quality caption and comment-reply suggestions |
| Gemini (Google) | WhatsApp / Google apps - smart replies and summarising long group chats |
| Claude (Anthropic) | Zomato - reading and summarising thousands of reviews and handling complex support queries |

## Task 2: Open source vs closed source comparison

| Point | Open Source (e.g., Llama 2, Falcon) | Closed Source (e.g., GPT-4, Gemini) |
|-------|--------------------------------------|--------------------------------------|
| Cost | Model is free to download; you pay only for hardware/hosting. Cheaper at large scale. | Pay per use (per token/subscription). Easy to start, but cost grows with usage. |
| Customization | High - you can fine-tune the weights, change the model and run it your way. | Limited - mostly prompts, some fine-tuning options given by the provider. |
| Community support | Very strong - Hugging Face, GitHub, forums and many shared fine-tuned versions. | Support mainly from the company's documentation and paid support. |
| Data privacy | Better - can run locally/on-premise, so data stays with you. | Data is sent to the company's servers, which may be a concern for sensitive data. |
| Update frequency | Depends on the community/organisation; updates may be irregular. | Frequent, managed updates by the company (new versions, safety fixes) automatically. |

## Task 3: Installing Ollama and running Llama 2

**Steps:** Download Ollama from https://ollama.com/download and install it. Then open the terminal / command prompt.

**Exact command used:**

```
ollama run llama2
```

(`ollama pull llama2` downloads only the model; `ollama run llama2` downloads it if needed and starts the chat.)

**What I saw (2-3 lines):**
First, Ollama showed "pulling manifest" and progress bars while it downloaded the Llama 2 model (about 3.8 GB), followed by "verifying sha256 digest" and "success". After that, a `>>> Send a message (/? for help)` prompt appeared, which means the local model is ready and I can chat with it directly in the terminal. Type `/bye` to exit.

> Note: Please run this on your own laptop and replace the description above with exactly what you see on your screen (a screenshot is a good proof).

## Task 4: Zomato AI features using local LLM

**Command used:**
```
ollama run llama2
>>> Suggest 5 new features for a food delivery app like Zomato that use AI.
```

**Response (typical response from Llama 2 - replace with your own copy from the terminal):**

```
1. Personalized Meal Recommendations - AI studies your past orders, ratings and
   time of day to suggest dishes you are likely to enjoy.
2. Smart Delivery Time Prediction - Uses traffic, weather and restaurant
   preparation data to give a more accurate delivery time.
3. AI Chat Assistant - A chatbot that handles order tracking, refunds and
   complaints instantly in many languages.
4. Visual Food Search - Upload a photo of a dish and the app finds restaurants
   that serve something similar.
5. Dietary & Health Assistant - Suggests meals based on calories, allergies or
   diet goals (vegetarian, high-protein, etc.).
```

**Idea I find most interesting:** Visual Food Search (idea 4). Many times I see a dish on Instagram but I do not know its name, so being able to just upload the photo and find where to order it in my city would be very useful and makes food discovery fun.
