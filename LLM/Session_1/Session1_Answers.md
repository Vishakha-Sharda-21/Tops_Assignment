# SESSION 1 - Overview of LLMs

## Task 1: Three popular LLMs

| # | LLM | Company / Organization | Real-world use case |
|---|-----|------------------------|---------------------|
| 1 | GPT-4 / ChatGPT | OpenAI | Content writing and customer-support chatbots (e.g., drafting emails, answering FAQs on a website) |
| 2 | Gemini | Google (Google DeepMind) | Search assistance and summarising documents/emails inside Google Workspace |
| 3 | Claude | Anthropic | Coding help and analysing long documents such as contracts or reports |

(Another good example: Llama by Meta - open source, used for building custom chatbots.)

---

## Task 2: How does an LLM like ChatGPT reply on WhatsApp or a website chatbot? (4-5 sentences)

When I type a question in a WhatsApp or website chatbot, my message is sent to the LLM's server, where the text is first broken into small pieces called tokens and converted into numbers. The model, which is a huge neural network (a Transformer) trained on a lot of text, uses an attention mechanism to understand how the words in my question relate to each other and what I actually mean. It then predicts the most likely next token, adds it to the text, and repeats this step again and again to build the full answer word by word. The model uses patterns it learned during training, along with the earlier chat messages, to keep the reply relevant. Finally, the generated tokens are converted back into normal text and sent back to my chat window within a few seconds.

---

## Task 3: Rule-based chatbot vs LLM-powered chatbot

| Point | Traditional Rule-Based Chatbot (old IRCTC help bot) | Modern LLM-Powered Chatbot (ChatGPT / Bard) |
|-------|------------------------------------------------------|---------------------------------------------|
| Handling user queries | Works only on fixed keywords/menus ("Press 1 for PNR status"). If the question is outside the script it fails. | Understands natural sentences and can answer many types of questions, even ones it was never explicitly programmed for. |
| Language flexibility | Limited to a few pre-written languages and exact phrases; spelling mistakes or Hinglish confuse it. | Handles many languages, mixed languages (Hinglish), slang and typing mistakes quite well. |
| Learning capability | Does not learn; developers must manually add new rules. | Learned from huge data during training and can adapt to context in the conversation (can be fine-tuned for new needs). |
| Conversation / context | Treats each message separately, so it forgets what was said earlier. | Remembers earlier messages in the chat and gives follow-up answers. |
| Cost & setup | Cheap and simple to build, predictable answers. | Costlier to run (API/compute), and answers can sometimes be wrong (hallucination). |
| Response style | Fixed, robotic replies. | Natural, human-like and can be creative. |

---

## Task 4: How an LLM can improve an app - Zomato

**App chosen: Zomato**

Zomato could add an LLM-powered "Food Assistant" where I can simply type something like "I want a spicy, vegetarian dinner under Rs 300 that is healthy". The LLM would understand this natural sentence, check the menus and reviews, and suggest the best restaurants and dishes instead of me scrolling through filters for a long time. It could also summarise thousands of customer reviews into 2-3 lines (for example, "Great taste, but delivery is sometimes late") so that I can decide quickly. This will save time, make ordering easier and make the app feel more personal.

---

## Task 5: Asking an LLM about advantages and limitations in business

**Question asked:** "What are two advantages and two limitations of using LLMs in business applications?"

**Answer received (from an AI chatbot - Claude):**

> **Advantages**
> 1. **Productivity and automation at scale** - LLMs can draft emails, summarise documents, answer customer queries and write code in seconds, which reduces repetitive manual work and lowers support costs.
> 2. **Flexibility across tasks** - One model can handle many tasks (support, content creation, data extraction, translation) in many languages, without building a separate system for each.
>
> **Limitations**
> 1. **Accuracy and hallucinations** - LLMs can produce confident but wrong or made-up information, so important outputs (legal, financial, medical) need human review.
> 2. **Bias, privacy and cost concerns** - Models can reflect biases in their training data, sending sensitive company data to third-party APIs raises privacy risks, and large-scale usage can become expensive.

*(If your instructor wants the answer from ChatGPT specifically, ask the same question there and paste its reply in place of the box above. The content will be similar.)*

**My opinion (in my own words):**

I agree with the limitation about accuracy and hallucinations. When I use an LLM for studies, it sometimes gives an answer that sounds very sure but is actually wrong, for example a wrong formula or a made-up reference. In a business, a wrong answer to a customer about refunds or a wrong number in a report can cause real loss, so a human must always check important outputs. That is why I think LLMs should assist employees rather than replace their judgement completely.
